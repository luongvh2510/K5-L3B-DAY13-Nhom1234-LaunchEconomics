# Team

## Thông tin nhóm

- Tên nhóm: Nhom1234
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom1234-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/luongvh2510/K5-L3B-DAY13-Nhom1234-LaunchEconomics · nhánh `main` · commit chốt: `51ec3fb`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Đức Nhật | 2A202603812 |       | NguyenDucNhat3006 | Người viết code |
|   2 | Hồ Anh Tú       | 2A202603811 |       | HoAnhTu245 | Người kiểm số |
|   3 | Đoàn Anh Hùng   | 2A202603880 | hungdoan772@gmail.com | doananhhung | Người gắn nhãn 1 |
|   4 | Võ Hồng Lương   | 2A202603839 | 26ai.luongvh@vinuni.edu.vn | luongvh2510 | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## DoanAnhHung-2A202603880

### Phần việc phụ trách

- Người gắn nhãn 1 (Nhóm 1234 · Lớp L3B): đọc đề, theo dõi điều kiện "Xong khi" và kiểm soát 5 quy tắc bắt buộc của lab (`TV3-01`).
- Đối chiếu kết quả A1–A3 từ TV1 và rà soát toàn bộ phần A & B trong [report/team/bang_chi_phi.md](./report/team/bang_chi_phi.md) (`TV3-02`, `TV3-03`, `TV3-04`).
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR và so nhãn chốt đồng thuận cùng TV4 trong [report/team/bang_loi.md](./report/team/bang_loi.md) (`TV3-05`, `TV3-06`).
- Đề xuất 2 chỉ số mới (1 dùng, 1 an toàn), thiết kế 8 event có `trace_id` và kiểm tra chéo chỉ số–event trong [report/team/chi_so.md](./report/team/chi_so.md) (`TV3-07`).
- Trả lời 5 câu D2 "tách được tác động", ghi rõ đánh đổi MDE 6 điểm khớp D1 của TV2 và tính tỉ lệ mở lại hiện tại trong [report/team/pilot_plan.yaml](./report/team/pilot_plan.yaml) (`TV3-10`).
- Chấm chéo Gate 2a hồ sơ Nhóm 101 vào [report/team/phieu_cham.md](./report/team/phieu_cham.md) (`TV3-08`) và viết báo cáo cá nhân [report/team/2A202603880_DoanAnhHung.md](./report/team/2A202603880_DoanAnhHung.md) (`TV3-09`).

### Đóng góp cụ thể

- Bắt lỗi dán nhầm dữ liệu thô ở bullet 2 A2 trước khi gộp và rà soát trọn vẹn [report/team/bang_chi_phi.md](./report/team/bang_chi_phi.md) sau PR #3 (đủ nhãn `simulated`, mọi câu trả lời ≤ 3 dòng có số, không có từ cấm).
- Gắn độc lập 20 ca lỗi vào cột `Nhãn người 1` (4 Do người dùng, 7 Hệ thống, 4 Ngữ cảnh, 3 Giới hạn hệ thống, 2 Ngầm) và phối hợp TV4 đạt đồng thuận 16/20 = 80% trong [report/team/bang_loi.md](./report/team/bang_loi.md).
- Thiết kế riêng 2 chỉ số tự đề xuất (*Thời gian xem lại trung vị mỗi yêu cầu* và *Tỉ lệ sai lệch đối soát sổ cái và hoàn trùng*) cùng 8 event có `trace_id` (`claim.submitted`, `assistant.attempt_finished`, `assistant.escalated`, `agent_ui.review_submitted`, `agent_ui.rework_logged`, `payout.ledger_reconciled`, `claim.resolved`, `claim.reopened`) khớp 5/5 chỉ số trong [report/team/chi_so.md](./report/team/chi_so.md).
- Điền đủ 5 câu D2 (mỗi câu 1 dòng có số), ghi đánh đổi MDE 6 điểm (`n` hiệu dụng = 859/nhóm, `m ≥ 299`, `DE = 6,96`) và đo trực tiếp tỉ lệ `mo_lai_trong_7_ngay` từ [src/logix_requests.csv](./src/logix_requests.csv) (`51/1.200 = 4,25%` toàn mẫu; `39/982 = 3,97%` phạm vi `noi_dia + hang_nang`) vào [report/team/pilot_plan.yaml](./report/team/pilot_plan.yaml).
- Kiểm tra hồ sơ Nhóm 101 (`K5-L3B-DAY13-Nhom101-LaunchEconomics`) theo 3 tiêu chí C6–C8, chấm 30/30 (*Go có điều kiện*) kèm lý do có số và câu hỏi phản biện trong [report/team/phieu_cham.md](./report/team/phieu_cham.md).

### Bằng chứng

- Commit `0ea6022`: điền 20 nhãn độc lập cột `Nhãn người 1` trong [report/team/bang_loi.md](./report/team/bang_loi.md).
- Commit `ec1b608`: hoàn thiện 2 chỉ số tự đề xuất, 8 event có `trace_id` và kiểm tra chéo trong [report/team/chi_so.md](./report/team/chi_so.md).
- Commit `d088139`: hoàn thiện phiếu chấm Gate 2a cho Nhóm 101 trong [report/team/phieu_cham.md](./report/team/phieu_cham.md).
- Commit `493d3e1`: hoàn thiện D2, đánh đổi cỡ mẫu, tỉ lệ mở lại trong [report/team/pilot_plan.yaml](./report/team/pilot_plan.yaml) và tạo báo cáo cá nhân [report/team/2A202603880_DoanAnhHung.md](./report/team/2A202603880_DoanAnhHung.md).

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
