# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25× giá một lần chạy |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn hoặc cách tính | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 đ | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | `attempt` là 2 hoặc 3 | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 đ/việc | Tổng chi phí / số việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ/yêu cầu | `logix_runs.csv` và `logix_requests.csv` | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,3 lần hoá đơn token và tool trên mỗi yêu cầu (simulated).
- Làm lại chiếm tỷ trọng lớn nhất, 51,8% tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- `quoc_te` không đáng đưa vào pilot vì chi phí 22.515 đ/việc thành công, gấp 1,88× mốc 12.000 đ (simulated). Chạy lại mang lại ít lợi ích: tỉ lệ lượt chạy có trạng thái `ok` giảm từ 30,0% ở lượt 1 xuống 11,4% ở lượt 2 và 2,2% (2/93) ở lượt 3.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 việc/tháng (simulated) | +1.185 đ (simulated) | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng | 16.875 việc/tháng (simulated) | +2.370 đ (simulated) | 5.784 đ (simulated) | 0,48× (simulated) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không. Với chi phí biến đổi 3.414 đ/việc (simulated), tổng chi phí vẫn dưới 12.000 đ/việc ở cả 45.000 và 22.500 yêu cầu/tháng.

## B1 · Đổi từng yếu tố

So với chi phí gốc A2 là 4.472 đ/việc thành công (simulated). Tỉ lệ thay đổi được tính trước khi làm tròn chi phí.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt có `attempt > 2`. Yêu cầu có `so_lan_chay > 2` chuyển cho nhân viên, tính 0 phút xem lại và làm lại trong chi phí trợ lý. | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Áp dụng cùng quy tắc với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3% so với mức cơ sở 4.472 đ, đều simulated).
  Hai mức tăng +5,6% (token) và +40,7% (xem lại), đều simulated, cộng trực tiếp vì CPS là tổng chi phí token, tool, xem lại và làm lại chia cho mẫu số cố định là 978 việc thành công.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8% / −25,9%, simulated) · 2. Tỉ lệ xem lại (+40,7% / −20,3%, simulated)
  · 3. Lương nhân viên (+23,1% khi tăng lương 25%, simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công.

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ, simulated). Giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ, simulated), đồng thời để lại thêm 85 yêu cầu cho nhân viên so với giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: CPS biến đổi với 5 phút/yêu cầu có status=ok là 11.743 đ (0,98×) khi làm lại 9 phút/ca và 12.415 đ (1,03×) khi làm lại 15,3 phút/ca (đều simulated).
  Mốc 12.414 đ (1,03×) trong hướng dẫn lệch 1 đ so với kết quả làm tròn từ 12.414,79 đ (đều simulated).
- Kết quả này nói gì về thứ pilot cần học được? Pilot cần đo thời gian xem lại, làm lại và mức giảm tỉ lệ xem lại an toàn. Ngưỡng xem lại hòa vốn (làm tròn) ≤ 5,1 phút/yêu cầu với 9 phút làm lại, hoặc ≤ 4,8 phút với 15,3 phút làm lại (đều simulated).
