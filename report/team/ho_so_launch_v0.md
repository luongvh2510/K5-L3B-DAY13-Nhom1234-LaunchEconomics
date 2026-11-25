# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom1234 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] = 4.373.585 đ tổng chi phí ÷ 978 việc thành công; gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); khoản lớn nhất là làm lại, 51,8% tổng chi phí | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Theo B1 [simulated], so với gốc 4.472 đ: 1. số ca làm lại gấp đôi +51,8% (6.787 đ); 2. tỉ lệ xem lại gấp đôi +40,7% (6.292 đ); 3. lương nhân viên tăng 25% +23,1% (5.506 đ). Giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ/yêu cầu) | Theo loại, mỗi việc thành công [simulated]: noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×), doi_tac 10.215 đ (0,85×), quoc_te 22.515 đ (1,88×, loại khỏi pilot). Chi phí cả hệ thống (gồm 12.000 đ cho mỗi yêu cầu không thành công, B3) với giới hạn 3 lần: 7.037.585 đ ÷ 1.200 yêu cầu ≈ 5.865 đ/yêu cầu ≈ 0,49× của 12.000 đ; giới hạn 2 lần rẻ nhất: 6.901.220 đ ≈ 5.751 đ/yêu cầu ≈ 0,48×. Chưa gồm chi phí cố định 40 triệu đ/tháng (chờ A4) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đã đặc tả (chính: % đóng trong 24 giờ và không mở lại trong 7 ngày; dùng: tỉ lệ bỏ qua gợi ý; an toàn: tỉ lệ mở lại trong 7 ngày) và thêm 2 chỉ số tự đề xuất (thời gian xem lại trung vị, tỉ lệ sai lệch sổ cái và hoàn trùng), 8 event có `trace_id`. Số tính thử trên 1.200 yêu cầu: chờ TV2 (E1). Chi tiết: `chi_so.md` | Chưa | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận nhãn 16/20 = 80%; 4 ca lệch (5, 9, 13, 17) đã thống nhất kèm quy tắc; bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có ngưỡng và một vai trò phụ trách (ngưỡng là đề xuất, chưa đo từ dữ liệu). Chi tiết: `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | (chờ D: BTC chưa thông báo) | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Hai rủi ro [simulated], số lấy từ bảng độ nhạy: (1) số ca làm lại gấp đôi: 6.787 đ/việc (+51,8%), theo dõi khi tỉ lệ làm lại vượt 7% mỗi tuần (mốc chạy thử 48/982 = 4,9%); (2) phải xem lại gần như toàn bộ: 11.743 đ/việc (0,98× của 12.000 đ) đến 12.415 đ/việc (1,03×), theo dõi khi hơn 50% yêu cầu vẫn cần xem lại ở cuối bước 25%. Chi tiết: `chi_so.md` | Giả lập | PM trợ lý hoàn phí (rủi ro 1), Trưởng nhóm CSKH (rủi ro 2) |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
