# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: Thời gian xem lại trung vị mỗi yêu cầu (phút/ca) | `median(review_duration_sec) ÷ 60` trên các yêu cầu có xem lại (`agent_ui.review_submitted`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ sai lệch đối soát sổ cái và hoàn trùng | Số lệnh hoàn có (`customer_notified = true` và `ledger_status ≠ ok`) hoặc (`payout_count > 1`), chia tổng số lệnh chi hoàn | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `claim.submitted` | Cổng CSKH / App khách | `request_id`, `depot`, `loai`, `so_tien_vnd`, `pilot_group`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí mới |
| `assistant.attempt_finished` | Dịch vụ trợ lý hoàn phí | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `policy_version`, `trace_id` | Ngay sau mỗi lần chạy trợ lý (kể cả khi `loi`) |
| `assistant.escalated` | Dịch vụ trợ lý hoàn phí | `request_id`, `escalation_reason`, `attempt_count`, `trace_id` | Khi trợ lý dừng và chuyển hồ sơ cho nhân viên |
| `agent_ui.review_submitted` | Màn hình CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `review_duration_sec`, `trace_id` | Khi nhân viên xem gợi ý xong và bấm xác nhận |
| `agent_ui.rework_logged` | Màn hình CSKH | `request_id`, `staff_id`, `rework_duration_sec`, `error_tag`, `trace_id` | Khi nhân viên hoàn tất xử lý lại một ca sai |
| `payout.ledger_reconciled` | Dịch vụ thanh toán / Kế toán | `request_id`, `idempotency_key`, `ledger_status`, `customer_notified`, `payout_count`, `trace_id` | Khi ghi sổ cái hoàn tiền và đối soát với thông báo gửi khách |
| `claim.resolved` | Hệ thống quản lý phiếu | `request_id`, `resolved_at`, `resolution_channel`, `trace_id` | Khi phiếu hoàn phí được đóng |
| `claim.reopened` | Cổng CSKH / App khách | `request_id`, `reopened_at`, `reopen_reason`, `days_since_close`, `trace_id` | Khi phiếu đã đóng bị mở lại |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (`% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày`)**: ghép qua `trace_id` giữa `claim.submitted` (`created_at`, mẫu số), `claim.resolved` (`resolved_at − created_at ≤ 24h`) và không phát sinh `claim.reopened` với `days_since_close ≤ 7`.
- **Chỉ số dùng 1 (`Tỉ lệ bỏ qua gợi ý`)**: đếm `agent_ui.review_submitted` có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số `agent_ui.review_submitted`.
- **Chỉ số an toàn 1 (`Tỉ lệ lỗi lọt đến khách`)**: đếm `claim.reopened` có `days_since_close ≤ 7`, chia tổng số `claim.submitted`.
- **Chỉ số dùng 2 (tự đề xuất — `Thời gian xem lại trung vị mỗi yêu cầu`)**: tính `median(review_duration_sec) ÷ 60` từ `agent_ui.review_submitted` (đồng thời cùng `agent_ui.rework_logged` dùng đo thật để thay thế 2 cột `_simulated` từ tuần 1 pilot).
- **Chỉ số an toàn 2 (tự đề xuất — `Tỉ lệ sai lệch đối soát sổ cái và hoàn trùng`)**: đếm `payout.ledger_reconciled` có (`customer_notified = true` và `ledger_status ≠ ok`) hoặc (`payout_count > 1`), chia tổng số `payout.ledger_reconciled`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: 6.787 đ/việc thành công, tăng 51,8% so với mốc A2 trên toàn bộ mẫu (simulated). | Tỉ lệ yêu cầu phải làm lại trong nhóm dùng trợ lý vượt 7% trong một tuần. Mốc chạy thử của `noi_dia` và `hang_nang` là 48/982 (4,9%). | Rà 20 trace làm lại để tìm nguyên nhân. Nếu lỗi tập trung ở `hang_nang`, thu hẹp bước tiếp theo về `noi_dia` và kiểm tra lại tỉ lệ sau một tuần. | PM trợ lý hoàn phí |
| Phải duy trì xem lại thủ công gần như toàn bộ | B4: Xem lại 100% trong phạm vi `noi_dia` và `hang_nang`, với 5 phút xem lại mỗi yêu cầu có lượt `ok`, cho 11.743 đ/việc (0,98× mốc 12.000 đ) nếu làm lại mất 9 phút/ca và 12.415 đ/việc (1,03×) nếu mất 15,3 phút/ca (simulated). | Cuối bước triển khai 25%, hơn 50% yêu cầu có lượt `ok` vẫn cần xem lại. Theo dõi thêm số phút xem lại và làm lại thực tế mỗi tuần. | Giữ quy mô hiện tại và tính lại chi phí với số phút thực tế. Thử giảm xem lại theo từng bước khi tỉ lệ sửa hoặc bỏ gợi ý dưới 15% và chỉ số an toàn đạt ngưỡng pilot. | Trưởng nhóm CSKH |
