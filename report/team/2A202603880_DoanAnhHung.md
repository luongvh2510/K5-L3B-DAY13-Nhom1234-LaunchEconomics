# Báo cáo cá nhân — Đoàn Anh Hùng - 2A202603880

## 1. Thông tin thành viên

- Họ tên: Đoàn Anh Hùng
- MSSV: 2A202603880
- Email: hungdoan772@gmail.com
- Vai trong nhóm: Người gắn nhãn 1 (Nhóm 1234 · Lớp L3B)

## 2. Phần việc phụ trách

- **TV3-01 (Cài đặt & quy tắc):** Đọc đề bài, theo dõi điều kiện "Xong khi" từng checkpoint và kiểm soát 5 quy tắc bắt buộc cho nhóm.
- **TV3-02, TV3-03, TV3-04 (CP1–CP2):** Đối chiếu kết quả A1–A3 từ TV1, phát hiện lỗi định dạng/nhãn, và rà soát toàn bộ phần A & B trong [bang_chi_phi.md](./bang_chi_phi.md).
- **TV3-05, TV3-06 (CP3):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR và so nhãn/chốt đồng thuận cùng TV4 trong [bang_loi.md](./bang_loi.md).
- **TV3-07 (CP5 · E1):** Đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, thiết kế danh sách ≥ 6 event có `trace_id` và kiểm tra chéo chỉ số–event trong [chi_so.md](./chi_so.md).
- **TV3-10 (CP4 · D2):** Trả lời 5 câu "tách được tác động", ghi rõ đánh đổi cỡ mẫu khớp với D1 của TV2 và tính tỉ lệ mở lại hiện tại từ dữ liệu chạy thử trong [pilot_plan.yaml](./pilot_plan.yaml).
- **TV3-08 (Duyệt chéo Gate 2a):** Đọc hồ sơ Nhóm 101 (`K5-L3B-DAY13-Nhom101-LaunchEconomics`), chấm 3 tiêu chí hội đồng (30 điểm) kèm lý do bằng số và câu hỏi phản biện trong [phieu_cham.md](./phieu_cham.md).
- **TV3-09 (Nộp bài):** Hoàn thiện báo cáo cá nhân này và nộp link repo nhóm lên LMS trước 23h59 GMT+7.

## 3. Đóng góp cụ thể

- **Rà soát chi phí (CP1–CP2):** Đối chiếu số liệu A1–A3 của TV1 (bắt lỗi dán nhầm output thô ở bullet 2 A2 trước khi merge), và sau khi PR #3 của TV2 merge vào `main` đã rà toàn bộ [bang_chi_phi.md](./bang_chi_phi.md): xác nhận đủ nhãn `simulated` trên mọi số tính từ hai cột `_simulated`, mọi câu trả lời ≤ 3 dòng có số, và không xuất hiện từ cấm.
- **Gắn nhãn độc lập 20 ca lỗi (CP3):** Hoàn thành và chốt độc lập cột `Nhãn người 1` cho 20 ca lỗi theo nguyên nhân gốc (phân bổ: 4 Do người dùng, 7 Hệ thống, 4 Ngữ cảnh, 3 Giới hạn hệ thống, 2 Ngầm — điều chỉnh riêng Ca 13 và Ca 17 về `Hệ thống` trước khi so), push riêng [bang_loi.md](./bang_loi.md) để TV4 điền độc lập cột `Nhãn người 2` và đối chiếu đồng thuận.
- **Thiết kế chỉ số & event E1 (CP5):** Tự đề xuất 2 chỉ số mới gắn trực tiếp vào điểm mù của pilot:
  - Chỉ số dùng: *Thời gian xem lại trung vị mỗi yêu cầu (phút/ca)* (gắn với ngưỡng hòa vốn ~5 phút/ca của B4 và thay thế dữ liệu `simulated`).
  - Chỉ số an toàn: *Tỉ lệ sai lệch đối soát sổ cái và hoàn trùng* (chặn lỗi báo hoàn giả khi sổ cái lỗi 503 ở ca 7 và hoàn tiền 2 lần ở ca 20).
  - Thiết kế 8 event theo vòng đời yêu cầu (`claim.submitted`, `assistant.attempt_finished`, `assistant.escalated`, `agent_ui.review_submitted`, `agent_ui.rework_logged`, `payout.ledger_reconciled`, `claim.resolved`, `claim.reopened`), mọi event đều có `trace_id` và kiểm tra chéo khớp 5/5 chỉ số ở bảng E1.
- **Phân tích tách tác động D2 & ngưỡng an toàn (CP4):** Trả lời đủ 5 câu D2 (mỗi câu 1 dòng, có số) khớp phương án chia 20+20 nhân viên, MDE 6 điểm (`n` hiệu dụng = 859/nhóm, `m ≥ 299`, `DE = 6,96`) của TV2; tính trực tiếp tỉ lệ `mo_lai_trong_7_ngay` từ [logix_requests.csv](../../src/logix_requests.csv) ra `51/1.200 = 4,25%` toàn mẫu và `39/982 = 3,97%` trong phạm vi `noi_dia + hang_nang` (`noi_dia` `3,16%`, `hang_nang` `8,23%`) làm căn cứ tránh đặt ngưỡng tuyệt đối 3% gây dừng giả.
- **Duyệt chéo Gate 2a:** Kiểm tra toàn bộ hồ sơ của Nhóm 101 theo 3 tiêu chí C6–C8 (chấm 30/30, quyết định *Go có điều kiện* kèm lý do bằng số và 1 câu hỏi về cơ chế giảm xem lại tuần 1–2) vào [phieu_cham.md](./phieu_cham.md).

## 4. Bằng chứng

- Commit `0ea6022`: điền 20 nhãn độc lập cột `Nhãn người 1` vào [bang_loi.md](./bang_loi.md).
- Commit `ec1b608`: hoàn thiện 2 chỉ số tự đề xuất, 8 event có `trace_id` và kiểm tra chéo trong [chi_so.md](./chi_so.md).
- Commit `d088139`: hoàn thiện phiếu chấm Gate 2a (30/30, *Go có điều kiện*) cho Nhóm 101 trong [phieu_cham.md](./phieu_cham.md).
- Cập nhật phần chú thích D2, đánh đổi MDE 6 điểm và tỉ lệ mở lại (`4,25%` toàn mẫu / `3,97%` phạm vi pilot) trong [pilot_plan.yaml](./pilot_plan.yaml) (commit hoàn thiện TV3-10 và báo cáo cá nhân này).
- Báo cáo cá nhân: `report/team/2A202603880_DoanAnhHung.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Antigravity (Gemini) tích hợp trong IDE.
- **Mục đích sử dụng:**
  - Tóm tắt yêu cầu đề bài, đối chiếu checklist 5 quy tắc và kiểm tra tiến độ nhánh Git của nhóm.
  - Gợi ý phân tích nguyên nhân gốc cho 20 ca lỗi Google PAIR (tôi tự duyệt từng ca và chủ động điều chỉnh Ca 13, Ca 17 theo nhận định cá nhân trước khi so với TV4).
  - Thảo luận và thiết kế mới 2 chỉ số tự đề xuất cùng 8 event riêng (không chép nguyên ví dụ trong tài liệu hướng dẫn) và đối chiếu khả năng đo cho từng chỉ số.
  - Chạy lệnh Python đọc trực tiếp cột `mo_lai_trong_7_ngay` từ `src/logix_requests.csv` để tính chính xác tỉ lệ mở lại và rà soát hồ sơ Nhóm 101 theo 3 tiêu chí C6–C8.
- **Cách tự kiểm tra:**
  - Kiểm tra lại trực tiếp từng số liệu A1–A3, B1–B4, D1 và tỉ lệ mở lại trên file CSV/repo thay vì tin số ước đoán.
  - Rà lại toàn bộ file đã sửa để chắc chắn không có từ cấm, đầy đủ nhãn `simulated`, câu trả lời ≤ 3 dòng, mọi event đều có `trace_id` và chỉ commit đúng file phụ trách để tránh xung đột với các thành viên khác.

## 6. Tự đánh giá

- Hoàn thành đầy đủ các đầu việc được phân công (`TV3-01` đến `TV3-10`) đúng tiến độ, phối hợp Git gọn gàng và không gây xung đột nhánh với 3 thành viên còn lại.
- Điểm cần tiếp tục theo dõi sau buổi học: bổ sung phần ghi lại câu trả lời của Nhóm 101 vào dòng cuối [phieu_cham.md](./phieu_cham.md) nếu có trao đổi Q&A trực tiếp, và cùng nhóm xác nhận file [pilot_plan.yaml](./pilot_plan.yaml) không còn dấu `?` và đọc được bằng `yaml.safe_load` sau khi TV4 điền xong phần D3.
