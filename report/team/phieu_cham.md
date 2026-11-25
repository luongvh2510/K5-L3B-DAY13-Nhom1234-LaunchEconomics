# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhóm 1234 (L3B)
- Nhóm được chấm: Nhóm 101 (L3B — `K5-L3B-DAY13-Nhom101-LaunchEconomics`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Chọn **Go có điều kiện** khớp chi phí cả hệ thống 5.865 đ/yc = 0,49× (`simulated`) và phạm vi `noi_dia` (0,22×) + `hang_nang` (0,69×); nêu đủ con số bất lợi (xem lại 100% lên 11.743–12.415 đ `simulated`, power ≈ 0,64 ở MDE 5 điểm, lỗi hoàn trùng ca 20/ca 7) kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra rõ ràng. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn nhãn `simulated` đầy đủ ở mọi số từ 2 cột `_simulated` và ghi trạng thái `Giả lập` ở mục 1, 2, 3, 7 của hồ sơ; không dùng từ cấm; thu hẹp phạm vi còn `noi_dia` + `hang_nang` (loại `quoc_te` 22.515 đ = 1,88×, thành công 27,3% và `doi_tac` 10.215 đ = 0,85× có điều khoản riêng). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách được tác động: 20 nhân viên đối chứng chạy song song, phân tầng ngẫu nhiên 12 depot (`seed: 130101`), kiểm soát spillover bằng quyền tài khoản và log `staff_id`; đủ cỡ mẫu theo đánh đổi MDE 6 điểm (`n_per_arm` 859 hiệu dụng / 5.980 thô, `DE = 6,96`, 20 cụm/nhóm); đủ 3 luật dừng đúng mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ` (ngưỡng an toàn +2 điểm hoặc > 6% phù hợp nền mở lại 4,25% / 3,97% trong phạm vi) và rollback trong 30 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ đủ 7 mục, số liệu nhất quán giữa `bang_chi_phi.md`, `bang_loi.md`, `chi_so.md`, `pilot_plan.yaml` và `ho_so_launch_v0.md`; đề xuất nêu rõ 4 điều kiện chặn trước và trong pilot (vá khóa chống trùng ca 20 và đối soát sổ cái ca 7 trước 2026-12-05, ký chấp nhận MDE 6 điểm với power ≈ 0,64, thay phút `simulated` bằng thời gian đo thật sau tuần 1, và lộ trình giảm xem lại xuống < 50% sau bước 0.25).

**Một câu hỏi cho đội trình:** Nếu trong tuần đầu pilot phải xem lại 100% khiến chi phí thực tế vượt ngưỡng 8.000 đ (ước tính 11.743–12.415 đ, `simulated`), nhóm sẽ dựa trên tiêu chí cụ thể nào để giảm dần tỉ lệ xem lại mà không kích hoạt luật dừng chi phí ở tuần thứ 2?

**Câu trả lời của đội trình (ghi lại tại buổi):** *(Ghi lại khi Nhóm 101 trả lời tại phiên duyệt chéo 17:25)*
