import streamlit as st
st.image("logo.jpg")
# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 TO TRUONG THANH TRUC")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================

so_tien = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Lãi suất dạng thập phân
    lai_suat_nam = lai_suat / 100

    # Tổng tiền lãi theo công thức lãi đơn
    tong_tien_lai = so_tien * lai_suat_nam * (ky_han / 12)

    # Tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai
        so_ky = 1
        ten_ky = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        tien_lai_dinh_ky = tong_tien_lai / ky_han
        so_ky = ky_han
        ten_ky = "tháng"

    else:  # Hàng quý
        so_quy = ky_han / 3
        tien_lai_dinh_ky = tong_tien_lai / so_quy
        so_ky = so_quy
        ten_ky = "quý"

    # Tổng tiền sau khi cộng lãi
    tong_tien_nhan = so_tien + tong_tien_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("Đã tính toán thành công!")

    st.subheader("📊 KẾT QUẢ")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Tiền lãi định kỳ",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

        st.metric(
            "Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Tổng tiền gốc",
            f"{so_tien:,.0f} VNĐ"
        )

        st.metric(
            "Tổng gốc + lãi",
            f"{tong_tien_nhan:,.0f} VNĐ"
        )

    st.divider()

    # Thông tin chi tiết
    st.subheader("📋 Thông tin khoản tiền gửi")

    st.write(f"**Số tiền gửi:** {so_tien:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
    st.write(f"**Tiền lãi mỗi {ten_ky}:** {tien_lai_dinh_ky:,.0f} VNĐ")
    st.write(f"**Tổng tiền lãi:** {tong_tien_lai:,.0f} VNĐ")
    st.write(f"**Tổng số tiền nhận được:** {tong_tien_nhan:,.0f} VNĐ")

    # =========================
    # BẢNG TÓM TẮT
    # =========================

    st.divider()
    st.subheader("💰 Tổng kết")

    ket_qua = {
        "Khoản mục": [
            "Tiền gốc",
            "Tổng tiền lãi",
            "Tổng gốc + lãi"
        ],
        "Số tiền (VNĐ)": [
            f"{so_tien:,.0f}",
            f"{tong_tien_lai:,.0f}",
            f"{tong_tien_nhan:,.0f}"
        ]
    }

    st.table(ket_qua)
