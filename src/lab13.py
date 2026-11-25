"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    if k is None:
        return 1 / p if p > 0 else math.inf
    return sum((1 - p) ** i for i in range(k))


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    if k is None:
        return float(k>0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    xac_suat = ti_le_thanh_cong(p, k)
    if xac_suat == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / xac_suat


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    cac_phep_thu = [
        ("Số lần chạy trung bình, tối đa 2 lần", so_lan_chay_ky_vong(0.8, 2), 1.20, " lần"),
        ("Số lần chạy trung bình, chạy đến khi đúng", so_lan_chay_ky_vong(0.8), 1.25, " lần"),
        ("Hệ số chi phí mỗi việc thành công, tối đa 3 lần",
         he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 1.25, "× giá một lần chạy"),
    ]
    for ten, ket_qua, dap_an, don_vi in cac_phep_thu:
        assert abs(ket_qua - dap_an) < 1e-9, f"{ten}: mong đợi {dap_an}, nhận {ket_qua}"
        ket_qua_hien_thi = f"{ket_qua:.2f}".replace(".", ",")
        print(f"{ten}: {ket_qua_hien_thi}{don_vi}")
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    runs_nhom = runs.loc[runs["request_id"].isin(reqs["request_id"])]
    thanh_cong = reqs["ket_qua"].eq("thanh_cong")
    reqs_tinh_phut = reqs

    if max_lan_chay is not None:
        runs_nhom = runs_nhom.loc[runs_nhom["attempt"].le(max_lan_chay)]
        trong_gioi_han = reqs["so_lan_chay"].le(max_lan_chay)
        thanh_cong = thanh_cong & trong_gioi_han
        # Yêu cầu vượt giới hạn chuyển cho nhân viên, bỏ phút khỏi chi phí trợ lý.
        reqs_tinh_phut = reqs.loc[trong_gioi_han]

    token = (
        runs_nhom["tokens_in"].sum() * gia_vao
        + runs_nhom["tokens_out"].sum() * gia_ra
    ) / 1_000
    tool = runs_nhom["tool_calls"].sum() * gia_tool
    xem_lai = reqs_tinh_phut["phut_xem_lai_simulated"].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs_tinh_phut["phut_lam_lai_simulated"].sum() * luong_phut * he_so_lam_lai

    tong = token + tool + xem_lai + lam_lai
    so_viec_thanh_cong = int(thanh_cong.sum())
    return {
        "token": token,
        "tool": tool,
        "xem_lai": xem_lai,
        "lam_lai": lam_lai,
        "tong": tong,
        "thanh_cong": so_viec_thanh_cong,
        "cps": tong / so_viec_thanh_cong if so_viec_thanh_cong else math.inf,
    }


def in_bang_a2(runs, reqs, ket_qua):
    """In bảng A2 theo định dạng Markdown của báo cáo."""
    hoa_don_moi_yeu_cau = (ket_qua["token"] + ket_qua["tool"]) / len(reqs)
    chay_lai = mo_hinh(runs.loc[runs["attempt"].isin([2, 3])], reqs)
    chi_phi_chay_lai = chay_lai["token"] + chay_lai["tool"]
    boi_so_hoa_don = ket_qua["cps"] / hoa_don_moi_yeu_cau
    ten_khoan = {"token": "Token", "tool": "Tool", "xem_lai": "Xem lại", "lam_lai": "Làm lại"}
    khoan_lon_nhat = max(ten_khoan, key=ket_qua.__getitem__)
    ty_trong_lon_nhat = ket_qua[khoan_lon_nhat] / ket_qua["tong"]

    cac_dong = [
        ("Token", f"{ket_qua['token']:,.0f} đ", "`logix_runs.csv`", "đo từ trace"),
        ("Tool", f"{ket_qua['tool']:,.0f} đ", "`logix_runs.csv`", "đo từ trace"),
        ("Trong đó, phần của lần chạy thứ 2 và 3", f"{chi_phi_chay_lai:,.0f} đ",
         "`attempt` là 2 hoặc 3", "đo từ trace"),
        ("Xem lại", f"{ket_qua['xem_lai']:,.0f} đ", "`phut_xem_lai_simulated`", "simulated"),
        ("Làm lại", f"{ket_qua['lam_lai']:,.0f} đ", "`phut_lam_lai_simulated`", "simulated"),
        ("Tổng chi phí", f"{ket_qua['tong']:,.0f} đ", "Token + tool + xem lại + làm lại", "simulated"),
        ("Số việc thành công", f"{ket_qua['thanh_cong']:,d} việc", "`ket_qua`", ""),
        ("Chi phí mỗi việc thành công", f"{ket_qua['cps']:,.0f} đ/việc",
         "Tổng chi phí / số việc thành công", "simulated"),
        ("Hoá đơn token và tool chia cho số yêu cầu", f"{hoa_don_moi_yeu_cau:,.1f} đ/yêu cầu",
         "`logix_runs.csv` và `logix_requests.csv`", "đo từ trace"),
    ]

    print("\n## A2 · Mô hình chi phí từ trace\n")
    print("| Khoản | Giá trị | Nguồn hoặc cách tính | Nhãn |")
    print("| --- | ---: | --- | --- |")
    for ten, gia_tri, nguon, nhan in cac_dong:
        print(f"| {ten} | {gia_tri} | {nguon} | {nhan} |")

    print(f"\n- Chi phí mỗi việc thành công gấp {boi_so_hoa_don:.1f} lần hoá đơn mỗi yêu cầu (simulated).")
    print(f"- {ten_khoan[khoan_lon_nhat]} chiếm tỷ trọng lớn nhất, {ty_trong_lon_nhat:.1%} (simulated).")


def in_bang_b1(runs, reqs, cps_goc):
    """In chi phí và mức thay đổi so với A2 cho mỗi kịch bản B1."""
    kich_ban = {
        "Giá token gấp đôi": {"gia_vao": 52, "gia_ra": 260},
        "Giá token giảm một nửa": {"gia_vao": 13, "gia_ra": 65},
        "Tỉ lệ xem lại gấp đôi": {"he_so_xem_lai": 2},
        "Tỉ lệ xem lại giảm một nửa": {"he_so_xem_lai": 0.5},
        "Số ca làm lại gấp đôi": {"he_so_lam_lai": 2},
        "Số ca làm lại giảm một nửa": {"he_so_lam_lai": 0.5},
        "Lương nhân viên tăng 25%": {"luong_phut": 2500},
        "Chỉ cho chạy tối đa 2 lần": {"max_lan_chay": 2},
        "Chỉ cho chạy 1 lần": {"max_lan_chay": 1},
    }

    print("\n## B1 · Đổi từng yếu tố\n")
    print("| Kịch bản | Chi phí mỗi việc thành công (simulated) | Thay đổi (simulated) |")
    print("| --- | ---: | ---: |")
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        thay_doi = cps / cps_goc - 1
        chi_phi_hien_thi = f"{cps:,.0f}".replace(",", ".")
        thay_doi_hien_thi = f"{thay_doi:+.1%}".replace(".", ",")
        print(f"| {ten} | {chi_phi_hien_thi} đ | {thay_doi_hien_thi} |")


def in_bang_b3(runs, reqs):
    """So sánh chi phí cả hệ thống khi giới hạn số lượt chạy."""
    print("\n## B3 · Giới hạn chạy lại có thật sự rẻ hơn\n")
    print(
        "| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | "
        "Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |"
    )
    print("| --- | ---: | ---: | ---: | ---: |")
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua["thanh_cong"]
        chi_phi_he_thong = ket_qua["tong"] + khong_thanh_cong * BASELINE
        tong_tro_ly_hien_thi = f"{ket_qua['tong']:,.0f}".replace(",", ".")
        he_thong_hien_thi = f"{chi_phi_he_thong:,.0f}".replace(",", ".")
        cps_hien_thi = f"{ket_qua['cps']:,.0f}".replace(",", ".")
        print(
            f"| {gioi_han} lần | {tong_tro_ly_hien_thi} đ | {khong_thanh_cong} | "
            f"{he_thong_hien_thi} đ | {cps_hien_thi} đ |"
        )


def co_mau_hai_ti_le(p1, p2, alpha, power):
    """Cỡ mẫu mỗi nhóm, kiểm định hai phía, theo công thức của lab."""
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    tu_so = (
        z_alpha * math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
        + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2
    return math.ceil(tu_so / (p2 - p1) ** 2)


def in_co_mau_d1():
    """Tính năm phương án D1 từ tham số chung và hệ số thiết kế."""
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    n_5_diem = co_mau_hai_ti_le(p1, 0.75, alpha, power)
    n_6_diem = co_mau_hai_ti_le(p1, 0.76, alpha, power)

    don_moi_nguoi = 75
    de_75 = 1 + (don_moi_nguoi - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * de_75)
    nguoi_moi_nhom = math.ceil(n_theo_nhan_vien / don_moi_nguoi)
    tong_nguoi = 2 * nguoi_moi_nhom
    nhan_vien_hien_co = 40

    so_nguoi_moi_nhom = 20
    so_depot_moi_nhom = 6
    tran_nhan_vien = so_nguoi_moi_nhom / icc
    tran_depot = so_depot_moi_nhom / icc

    # c*m / (1 + (m - 1)*ICC) >= n => m >= n*(1 - ICC)/(c - n*ICC).
    m_6_diem = math.ceil(
        n_6_diem * (1 - icc) / (so_nguoi_moi_nhom - n_6_diem * icc)
    )
    de_6_diem = 1 + (m_6_diem - 1) * icc
    n_hieu_dung = so_nguoi_moi_nhom * m_6_diem / de_6_diem

    n_5_hien_thi = f"{n_5_diem:,}".replace(",", ".")
    n_nhan_vien_hien_thi = f"{n_theo_nhan_vien:,}".replace(",", ".")
    tran_nhan_vien_hien_thi = f"{tran_nhan_vien:,.0f}".replace(",", ".")
    de_75_hien_thi = f"{de_75:.2f}".replace(".", ",")
    de_6_hien_thi = f"{de_6_diem:.2f}".replace(".", ",")
    hieu_dung_hien_thi = f"{n_hieu_dung:.2f}".replace(".", ",")

    print("\n## D1 · Cỡ mẫu\n")
    print("Tham số: p1 = 0,70; alpha = 0,05; power = 0,80; ICC = 0,02; hai phía.")
    print(f"a) Theo yêu cầu, p2 = 0,75: {n_5_hien_thi} đơn mỗi nhóm.")
    print(
        f"b) Theo nhân viên, m = {don_moi_nguoi}: DE = {de_75_hien_thi}; "
        f"{n_nhan_vien_hien_thi} đơn mỗi nhóm; {nguoi_moi_nhom} người mỗi bên; "
        f"tổng {tong_nguoi} > {nhan_vien_hien_co} nhân viên hiện có: không đủ."
    )
    print(
        f"c) {so_nguoi_moi_nhom} người mỗi bên: trần cỡ mẫu hiệu dụng c/ICC = "
        f"{tran_nhan_vien_hien_thi} < {n_5_hien_thi}: không đủ dù tăng m."
    )
    print(
        f"d) {so_depot_moi_nhom} depot mỗi bên: trần cỡ mẫu hiệu dụng c/ICC = "
        f"{tran_depot:.0f} < {n_5_hien_thi}: không đủ dù tăng m."
    )
    print(
        f"e) p2 = 0,76 (+6 điểm), {so_nguoi_moi_nhom} người mỗi bên: "
        f"cần {n_6_diem} đơn hiệu dụng mỗi nhóm; m nhỏ nhất = {m_6_diem} đơn/người; "
        f"DE = {de_6_hien_thi}; n hiệu dụng = {hieu_dung_hien_thi} >= {n_6_diem}."
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    in_bang_a2(runs, reqs, ket_qua)
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.


    for loai, reqs_loai in reqs.groupby("loai"):
        kq = mo_hinh(runs, reqs_loai)
        print(
            f"{loai}: {len(reqs_loai)} yêu cầu | "
            f"{kq['thanh_cong'] / len(reqs_loai):.1%} thành công | "
            f"{reqs_loai['so_lan_chay'].mean():.2f} lần/yêu cầu | "
            f"{kq['cps']:,.0f} đ (simulated) | "
            f"{kq['cps'] / BASELINE:.2f}× (simulated)"
        )

    runs_quoc_te = runs.loc[
        runs["request_id"].isin(reqs.loc[reqs["loai"].eq("quoc_te"), "request_id"])
    ].assign(ok=lambda df: df["status"].eq("ok"))

    print(runs_quoc_te.groupby("attempt")["ok"].agg(["sum", "count", "mean"]))
    in_bang_b1(runs, reqs, ket_qua["cps"])
    in_bang_b3(runs, reqs)
    # CP4 · Nhiệm vụ D: cỡ mẫu.
    in_co_mau_d1()
