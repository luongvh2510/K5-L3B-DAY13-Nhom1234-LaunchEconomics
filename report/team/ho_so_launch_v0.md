# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom1234 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] = 4.373.585 đ tổng chi phí ÷ 978 việc thành công; gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); khoản lớn nhất là làm lại, 51,8% tổng chi phí | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Theo B1 [simulated], so với gốc 4.472 đ: 1. số ca làm lại gấp đôi +51,8% (6.787 đ); 2. tỉ lệ xem lại gấp đôi +40,7% (6.292 đ); 3. lương nhân viên tăng 25% +23,1% (5.506 đ). Giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ/yêu cầu) | Theo loại, mỗi việc thành công [simulated]: noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×), doi_tac 10.215 đ (0,85×), quoc_te 22.515 đ (1,88×, loại khỏi pilot). Chi phí cả hệ thống (gồm 12.000 đ cho mỗi yêu cầu không thành công, B3) với giới hạn 3 lần: 7.037.585 đ ÷ 1.200 yêu cầu ≈ 5.865 đ/yêu cầu ≈ 0,49× của 12.000 đ; giới hạn 2 lần rẻ nhất: 6.901.220 đ ≈ 5.751 đ/yêu cầu ≈ 0,48×. Chưa gồm chi phí cố định 40 triệu đ/tháng (chờ A4) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (1.200 yêu cầu, chưa có nhóm đối chứng): chính 82,83% (994/1.200) đóng trong 24 giờ và không mở lại trong 7 ngày; dùng 27,12% (48/177) gợi ý bị sửa hoặc bỏ; an toàn 4,25% (51/1.200) mở lại trong 7 ngày. Thêm 2 chỉ số tự đề xuất (thời gian xem lại trung vị, tỉ lệ sai lệch sổ cái và hoàn trùng) và 8 event có `trace_id`. Chi tiết: `chi_so.md` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận nhãn 16/20 = 80%; 4 ca lệch (5, 9, 13, 17) đã thống nhất kèm quy tắc; bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có ngưỡng và một vai trò phụ trách (ngưỡng là đề xuất, chưa đo từ dữ liệu). Chi tiết: `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên, 20 người dùng trợ lý và 20 người đối chứng, bốc thăm ngẫu nhiên cùng tuần; phạm vi `noi_dia` + `hang_nang` (A3, simulated). Cỡ mẫu: 299 đơn mỗi người, 859 đơn hiệu dụng mỗi nhóm (hệ số thiết kế 6,96), thấy được mức hơn 6 điểm; nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64. 4 luật dừng có ngưỡng và người có quyền dừng (mở lại vượt 6%, lệch đối chứng 2 điểm từ bước 10 người, chi phí vượt 8.000 đ, bỏ qua gợi ý vượt 40%). Ngày quyết định 2027-01-14 (giả định bắt đầu 2026-12-14). Chi tiết: `pilot_plan.yaml` | Giả lập | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Hai rủi ro [simulated], số lấy từ bảng độ nhạy: (1) số ca làm lại gấp đôi: 6.787 đ/việc (+51,8%), theo dõi khi tỉ lệ làm lại vượt 7% mỗi tuần (mốc chạy thử 48/982 = 4,9%); (2) phải xem lại gần như toàn bộ: 11.743 đ/việc (0,98× của 12.000 đ) đến 12.415 đ/việc (1,03×), theo dõi khi hơn 50% yêu cầu vẫn cần xem lại ở cuối bước 25%. Chi tiết: `chi_so.md` | Giả lập | PM trợ lý hoàn phí (rủi ro 1), Trưởng nhóm CSKH (rủi ro 2) |

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`. Cơ sở: chi phí mỗi việc thành công 4.472 đ, thấp hơn 12.000 đ nhân viên tự làm, và chi phí cả hệ thống khoảng 0,49× (simulated). Số bất lợi: xem lại 100% đẩy chi phí lên 11.743–12.415 đ, tức 0,98–1,03× (simulated); power chỉ khoảng 0,64 nếu tác động thật là 5 điểm; với 4 người dùng thì 40 triệu đ tiền thuê cố định kéo chi phí lên khoảng 15.300 đ. Gate 2a chỉ duyệt kế hoạch pilot. Các mốc ngày dưới đây tính từ ngày bắt đầu giả định 2026-12-14.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Chặn hoàn trùng bằng khoá chống trùng và đối soát sổ cái hằng giờ trước khi bắt đầu (luật dừng 1) | Kỹ sư trưởng agent | 2026-12-13 |
| Ký chấp nhận mức chênh 6 điểm và power khoảng 0,64 ở mức 5 điểm | Giám đốc vận hành | 2026-12-13 |
| Bật đủ 8 event có `trace_id`; sau tuần 1 thay phút xem lại và làm lại simulated bằng phút đo thật rồi tính lại chi phí | PM trợ lý hoàn phí | 2026-12-21 |
| Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% không còn tiết kiệm; giảm khi tỉ lệ sửa hoặc bỏ gợi ý dưới 15% | Trưởng nhóm CSKH | 2026-12-27 |
| Xem lại hợp đồng chi phí cố định 40 triệu đ mỗi tháng nếu số việc thành công mỗi tuần dưới 50% kế hoạch | PM trợ lý hoàn phí | 2026-12-27 |
