# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đoàn Anh Hùng · Người gắn nhãn 2: Võ Hồng Lương (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Hệ thống | Không | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Ngầm | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Hệ thống | Ngầm | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 5: 14 đơn có mã giảm giá bị hoàn thừa mà không khách nào báo và không cảnh báo nào kích, chỉ lộ ra nhờ kiểm tra mẫu cuối tuần, nên là Ngầm. Hệ thống chỉ dùng khi sai đã lộ ra và có người nhìn thấy.
- Ca 17: trợ lý dùng bảng giá cũ trong bộ nhớ đệm, lệch 212 đơn trong 9 ngày mà không ai mở lại hay nhận ra, nên là Ngầm. Hệ thống chỉ dùng khi sai đã lộ ra và có người nhìn thấy.
- Ca 9: nguyên nhân gốc là khách nhập mã đơn sàn thay vì mã vận đơn, nên là Do người dùng. Việc trợ lý không gợi ý chỉ là chỗ cần cải thiện, ghi ở cột khắc phục.
- Ca 13: yêu cầu hoàn phí bảo hiểm nằm ngoài phạm vi trợ lý, nên là Giới hạn hệ thống. Trả lời chung chung kém chỉ là cách xử lý giới hạn chưa tốt, gốc vẫn là ngoài phạm vi.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Mỗi ngày tính tỉ lệ yêu cầu đóng bằng "Xác nhận đã nhận tiền" mà không có `refund_ledger_write` ok cùng `trace_id`, trên tổng yêu cầu đóng trong ngày; cảnh báo khi vượt 0,5% | Thêm bước xác nhận hiện trạng tiền trước khi đóng ("Tiền chưa về, vẫn xác nhận?") và cho mở lại yêu cầu trong 7 ngày | PM trợ lý hoàn phí |
| 15 | Hệ thống | Mỗi tuần đếm `staff_review_decision` = sửa với lý do sai tỉ lệ hoàn; cảnh báo khi vượt 3% gợi ý được xem lại | Thêm cổng kiểm tra tỉ lệ hoàn theo số giờ trễ (24–48 giờ = 50%) trước khi hiện gợi ý; gợi ý không khớp bảng chính sách thì chuyển nhân viên | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Đếm thông báo hoàn tiền gửi trong khung 22:00–06:00 theo ngày; cảnh báo khi vượt 1% tổng thông báo hoặc có từ 3 phản ánh về thông báo ngoài giờ trong một tuần | Hẹn giờ gửi thông báo trong khung 07:00–21:00, thông báo phát sinh ban đêm giữ lại gửi sáng hôm sau | PM trợ lý hoàn phí |
| 11 | Giới hạn hệ thống | Đếm `handoff_to_staff` với lý do đầu vào không hỗ trợ (âm thanh) theo ngày; cảnh báo khi vượt 5% số yêu cầu | Chuyển ngay cho nhân viên kèm tóm tắt thay vì yêu cầu khách nhập lại; ghi nhận loại đầu vào để cân nhắc hỗ trợ giọng nói ở giai đoạn sau | Trưởng nhóm CSKH |
| 5 | Ngầm | Kiểm tra mẫu hằng tuần 150 đơn có mã giảm giá, so số hoàn với giá sau giảm (`audit_sample_checked`); cảnh báo khi có từ 1 đơn lệch trở lên. Cỡ mẫu 150 chọn để bắt được lỗi từ 2% với xác suất 95% | Tính hoàn theo giá sau giảm trong bản ghi đơn; thêm kiểm thử cho đơn có mã giảm giá và ghi giá tính hoàn vào trace | Kế toán trưởng |
