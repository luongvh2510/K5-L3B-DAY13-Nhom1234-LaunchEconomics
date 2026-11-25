# Báo cáo cá nhân — Võ Hồng Lương - 2A202603839

## 1. Thông tin thành viên

- Họ tên: Võ Hồng Lương
- MSSV: 2A202603839
- Email: 26ai.luongvh@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ (Nhóm 1234 · Lớp L3B)

## 2. Phần việc phụ trách

- **TV4-01 (Cài đặt):** điền `TEAM.md`, kiểm repo nhóm đúng tên `K5-L3B-DAY13-Nhom1234-LaunchEconomics`.
- **TV4-02, TV4-05 (hồ sơ launch v0):** điền dần `ho_so_launch_v0.md` từ đầu buổi cho đến khi đủ bảy mục và dòng đề xuất cuối.
- **TV4-03, TV4-04 (CP3 · C):** gắn nhãn 20 ca lỗi (bộ nhãn 2), so nhãn với TV3, thống nhất ca lệch và lập bảng khắc phục 5 ca trong `bang_loi.md`.
- **TV4-10 (CP4 · D3):** điền `pilot_plan.yaml`: phạm vi, cách chia, bốn luật dừng, rollback, ngày quyết định.
- **TV4-07 (nộp bài):** điền `group_report.md`.
- **TV4-06, TV4-08, TV4-09:** trình bày trước hội đồng, commit và push cuối, báo cáo cá nhân này và nộp link repo lên LMS.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0:** điền từng mục khi có số từ các bạn: mục 1, 2, 3 từ A2, A3, B1, B3 của TV1; mục 4 từ ba chỉ số E1 của TV2; mục 5 từ phần C; mục 6 từ `pilot_plan.yaml`; mục 7 từ E2 của TV1. Viết dòng đề xuất **Go có điều kiện** kèm các số bất lợi (xem lại 100% gần bằng nhân viên tự làm, power khoảng 0,64) và 5 điều kiện có người phụ trách và ngày kiểm tra.
- **Nhiệm vụ C:** gắn bộ nhãn 2 (20 ca), so với bộ nhãn 1 của TV3, đồng thuận 16/20 = 80%; cùng TV3 chốt nhãn thống nhất cho 4 ca lệch (5, 9, 13, 17) và viết quy tắc phân biệt. Lập bảng khắc phục 5 ca (14, 15, 16, 11, 5), mỗi dòng có ngưỡng và một vai trò phụ trách.
- **Pilot (D3):** điền `pilot_plan.yaml` từ kết quả D1 của TV2 và D2 của TV3: chia theo nhân viên 20 + 20, 299 đơn mỗi người, mức chênh 6 điểm, bốn luật dừng, ngày quyết định 2027-01-14.
- **Gộp và kiểm tra nhánh:** theo dõi các nhánh của TV1 và TV2, gộp nhánh của TV1 vào `main`, lấy riêng commit E1 và D1 của TV2 bằng `git cherry-pick` để giữ đúng tác giả.
- **Quản lý tiến độ:** lập checklist 4 thành viên trên Google Sheet, cập nhật trạng thái theo lịch sử git, soạn tin nhắn giao việc cho nhóm.

## 4. Bằng chứng

- `TEAM.md`: commit `db37375`.
- `ho_so_launch_v0.md`: các commit `fa6d8d1`, `e917a96`, `9bfea21`, `f04ca91`, `a04d4ed`, `1aee917`, `0a1e3bc`, `0a81827`, `94dda92`.
- `bang_loi.md`: các commit `f070866` (nhãn người 2), `a61325a` (4 ca lệch và quy tắc), `6cfa396` (bảng khắc phục).
- `pilot_plan.yaml`: commit `3ab5747`.
- `group_report.md`: commit `3e398e8`.
- Gộp nhánh: merge `b42a5a0` (TV1), cherry-pick `65f9c64` (E1 của TV2) và `5069476` (D1 của TV2).
- Báo cáo cá nhân: `report/team/2A202603839_VoHongLuong.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Anthropic), chạy trong app máy tính.
- **Mục đích sử dụng:**
  - Đọc repo và đề bài, giải thích khái niệm (cách tính chi phí mỗi việc thành công, cỡ mẫu hiệu dụng khi chia theo cụm, năm loại lỗi Google PAIR).
  - Soạn nháp các phần hồ sơ (các mục của hồ sơ launch v0, bảng khắc phục 5 ca, `pilot_plan.yaml`, `group_report.md`) từ số liệu của nhóm; tôi đọc lại, chọn hoặc sửa trước khi commit.
  - Hướng dẫn cách đọc đề và quy trình gắn nhãn lỗi; công cụ không gắn nhãn hộ tôi. Tôi đã tự gắn bộ nhãn 2.
  - Kiểm tra nhánh, chạy `lab13.py` của các thành viên trong bản sao tạm, kiểm tra khả năng gộp và thực hiện `git merge`, `cherry-pick`, `push` theo yêu cầu của tôi.
- **Cách tự kiểm tra:**
  - Đối chiếu số trong hồ sơ với bảng A2, A3, B1, B3 của TV1 và chạy lại `lab13.py` trên `main` (ba phép thử ĐẠT, D1 ra 1.251 và 299 đơn mỗi người).
  - Tính lại ba chỉ số E1 (82,83%, 27,12%, 4,25%) trực tiếp từ `logix_requests.csv` và so với số của TV2.
  - Kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích, và không có từ cấm trong các file hồ sơ.
  - Các ngưỡng trong bảng khắc phục và luật dừng là đề xuất của nhóm, chưa đo từ dữ liệu; tôi đã ghi điều này trong hồ sơ.

## 6. Tự đánh giá

- Hoàn thành các đầu việc TV4 theo checklist. Hồ sơ launch v0 đủ bảy mục và đề xuất cuối, `pilot_plan.yaml` đọc được và không còn dấu `?`.
- Hạn chế: các ngưỡng cảnh báo là đề xuất chưa có dữ liệu đo; ngày bắt đầu và ngày quyết định của pilot là giả định.
- Điều học được: chi phí chủ yếu đến từ giờ nhân viên chứ không phải token, và với 40 nhân viên thì không cách chia nào đủ mẫu cho mức chênh 5 điểm, nên phải nói rõ đánh đổi 6 điểm trước khi chạy.
