# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom1234
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN để trả lời bốn câu hỏi: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra quyết định. Dữ liệu là 1.200 yêu cầu và 1.624 lần chạy giả lập. Cách làm: tính chi phí từ trace bằng `src/lab13.py`, đối chiếu từng con số bằng tay hoặc chạy lại, gắn nhãn `simulated` cho mọi số từ hai cột `_simulated`, rồi ghép thành hồ sơ một trang.

## 3. Giải pháp

- **A, B · Chi phí và độ nhạy:** `src/lab13.py` (ba phép thử A1, `mo_hinh`, 9 kịch bản, giới hạn số lần chạy, cỡ mẫu D1) và `report/team/bang_chi_phi.md` (A2, A3, A4, B1 đến B4).
- **C · Bảng lỗi:** hai người gắn nhãn 20 ca theo năm loại của Google PAIR, so nhãn, thống nhất 4 ca lệch và lập bảng khắc phục 5 ca, trong `report/team/bang_loi.md`.
- **D · Pilot:** `report/team/pilot_plan.yaml`: chia theo nhân viên, 20 người mỗi bên, bốn luật dừng, ngày quyết định.
- **E · Chỉ số, rủi ro, hồ sơ:** `report/team/chi_so.md` (ba chỉ số, hai chỉ số tự đề xuất, 8 event có `trace_id`, hai rủi ro kinh tế) và `report/team/ho_so_launch_v0.md` (bảy mục và đề xuất).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** 4.472 đ (simulated), gấp 16,3 lần hoá đơn token và tool trên mỗi yêu cầu (274,7 đ). Làm lại là khoản lớn nhất, 51,8% tổng chi phí.
- **Theo loại:** `noi_dia` 2.696 đ (0,22×) và `hang_nang` 8.221 đ (0,69×) so với 12.000 đ; `quoc_te` 22.515 đ (1,88×) và `doi_tac` 10.215 đ (0,85×) bị loại khỏi pilot (simulated).
- **Độ nhạy:** ba yếu tố mạnh nhất là số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%) và lương nhân viên (+23,1%); giá token gấp đôi chỉ +5,6% (simulated). Xem lại 100% làm chi phí lên 11.743 đến 12.415 đ, tức 0,98 đến 1,03× (simulated).
- **Chỉ số trong đợt chạy thử:** chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200). Đợt chạy thử không có nhóm đối chứng.
- **Bảng lỗi:** đồng thuận nhãn 16/20 = 80%.
- **Pilot:** 299 đơn mỗi người, 859 đơn hiệu dụng mỗi nhóm, thấy được mức hơn 6 điểm; power khoảng 0,64 nếu tác động thật là 5 điểm.
- **Đề xuất cuối:** Go có điều kiện cho `noi_dia` + `hang_nang`, kèm 5 điều kiện có người phụ trách và ngày kiểm tra.
- **Kết quả duyệt chéo nhóm nhận được:** (điền sau khi nhận phiếu từ nhóm hội đồng).

## 5. Khó khăn và cách xử lý

- **Nhãn lỗi không hoàn toàn độc lập:** người gắn nhãn 2 đã xem bảng nhãn của người gắn nhãn 1 qua tin nhắn trước khi gắn của mình. Nhóm ghi nhận điều này, giữ nguyên hai bộ nhãn đã commit, tính đồng thuận 16/20 và chỉ điền nhãn thống nhất cho 4 ca lệch (5, 9, 13, 17) kèm quy tắc phân biệt.
- **Gộp nhánh:** nhánh của một thành viên chứa các commit bị tạo lại, nên nhóm chỉ lấy đúng các commit cần thiết (E1, D1) bằng `git cherry-pick`, giữ nguyên tên tác giả.
- **Đẩy lên `main` bị từ chối** do có commit mới của thành viên khác; nhóm gộp `main` về rồi đẩy lại, không viết lại lịch sử.
- **Đúng cỡ mẫu và ngày quyết định:** phạm vi chỉ gồm khoảng 82% số đơn nên bước 20 người cần khoảng 10 ngày thay vì 8; nhóm đặt ngày quyết định sau 7 ngày theo dõi mở lại.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`. Tóm tắt theo lịch sử git:

- **Nguyễn Đức Nhật:** `lab13.py` (A1 đến A3, B1, B3) và rủi ro kinh tế E2.
- **Hồ Anh Tú:** A4, B2, B4, ba chỉ số E1 và cỡ mẫu D1.
- **Đoàn Anh Hùng:** nhãn người 1, chỉ số và 8 event E1, D2, phiếu chấm duyệt chéo.
- **Võ Hồng Lương:** `TEAM.md`, hồ sơ launch v0, nhãn người 2 và bảng khắc phục, `pilot_plan.yaml` (D3), gộp và kiểm tra các nhánh.

## 7. Hạn chế và hướng cải thiện

- Mọi chi phí liên quan giờ nhân viên là số giả lập; sau tuần 1 của pilot cần thay bằng phút đo thật.
- Các ngưỡng cảnh báo trong bảng khắc phục và luật dừng (0,5%, 3%, 6%, 8.000 đ, 40%) là đề xuất của nhóm, chưa đo từ dữ liệu.
- Ngày bắt đầu pilot 2026-12-14 và ngày quyết định 2027-01-14 là giả định.
- Số đơn có mã giảm giá mỗi tuần chưa biết; nếu dưới 150 thì kiểm tra hết nhóm đó.
- Với 20 cụm mỗi nhóm, pilot không đủ mẫu để thấy mức hơn 5 điểm, chỉ thấy mức hơn 6 điểm.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, lớp `NormalIndPower`
- Slide D1 của ban tổ chức (ba cách chia ai được dùng trợ lý)
