# Báo cáo cá nhân — Nguyễn Đức Nhật (2A202603812)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Nhật
- MSSV: 2A202603812
- Email:
- Lớp và nhóm: L3B · Nhom1234
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

Em phụ trách A1–A3, B1, B3 và E2 (TV1-08). Phần việc gồm kiểm tra công thức chạy lại, tính chi phí từ hai bảng dữ liệu, phân tích theo loại yêu cầu, so sánh các kịch bản chi phí và đề xuất cách theo dõi rủi ro kinh tế cho pilot.

## 3. Đóng góp cụ thể

- A1: Hoàn thiện ba phép thử và cho chương trình in cả ba giá trị để đối chiếu với bảng báo cáo.
- A2–A3: Dùng `request_id` để nối lượt chạy với nhóm yêu cầu cần tính. Cộng token, tool, phút xem lại và phút làm lại, rồi tính chi phí trên mỗi yêu cầu thành công. Tách kết quả theo bốn loại yêu cầu và kiểm tra tỉ lệ `ok` của từng lượt chạy cho `quoc_te`.
- B1: Chạy 9 kịch bản và tính phần trăm thay đổi so với A2 trước khi làm tròn. Với yêu cầu vượt giới hạn lượt chạy, tính 0 phút xem lại và làm lại vào chi phí trợ lý theo quy tắc của đề.
- B3: So sánh giới hạn 1, 2 và 3 lượt. Tính chi phí cả hệ thống bằng cách cộng 12.000 đ cho mỗi yêu cầu trợ lý xử lý không thành công.
- E2: Dùng B1 và kết quả B4 của Hồ Anh Tú để chọn hai rủi ro. Làm lại tăng gấp đôi là kịch bản làm chi phí tăng mạnh nhất ở B1. Duy trì xem lại thủ công gần như toàn bộ có thể đẩy chi phí pilot tới hoặc vượt mốc 12.000 đ/việc. Với mỗi rủi ro, em đề xuất dấu hiệu theo dõi, hành động và vai trò phụ trách.

## 4. Bằng chứng

- [Mã tính và in kết quả A1–A3, B1, B3](../../src/lab13.py) và [bảng chi phí của nhóm](bang_chi_phi.md).
- A1 đạt cả ba phép thử với kết quả 1,20 lần, 1,25 lần và hệ số 1,25×.
- A2 ghi nhận 978 yêu cầu thành công, với chi phí 4.472 đ/việc thành công (simulated). Ở A3, `quoc_te` có chi phí 22.515 đ/việc thành công (simulated) và chỉ 2/93 lượt thứ ba có trạng thái `ok`.
- B1 cho thấy số ca làm lại gấp đôi làm chi phí tăng 51,8% (simulated). B3 cho thấy giới hạn 2 lượt có chi phí cả hệ thống thấp nhất, 6.901.220 đ (simulated).
- [Bảng rủi ro kinh tế E2](chi_so.md#e2--rủi-ro-kinh-tế) dùng mốc 6.787 đ/việc khi số ca làm lại gấp đôi và 11.743–12.415 đ/việc khi xem lại 100% yêu cầu có lượt `ok` trong phạm vi pilot (simulated).

## 5. Công cụ AI đã dùng

Em dùng Codex để giải thích công thức, tham khảo code Python, bổ sung phần in bảng và diễn giải hai rủi ro E2. Kết quả được kiểm tra bằng cách chạy `lab13.py` trên hai CSV của nhóm, đối chiếu số in ra với bảng chi phí và kiểm tra số B4 trên nhánh `hoanhtu`.

## 6. Tự đánh giá

Qua B3, em hiểu vì sao phương án có chi phí thấp nhất trên mỗi việc thành công có thể làm tổng chi phí tăng. Giới hạn 1 lượt để lại thêm 85 yêu cầu cho nhân viên so với giới hạn 2 lượt. Qua E2, em hiểu cách dùng số liệu độ nhạy để chọn tín hiệu cần theo dõi và quyết định khi nào nên giữ nguyên quy mô pilot để đo lại chi phí.
