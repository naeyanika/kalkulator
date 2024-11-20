import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data

# Fungsi untuk menghitung rating
def calculate_rating(minor, moderate, major, fraud):
    # Jika ada fraud, langsung HIGH
    if fraud:
        return "HIGH"
    
    # Kriteria HIGH lainnya:
    if (
        (1 == major <= 2 and moderate > 12) or  # Kriteria 1
        (major >= 3 )         # Bagian dari Kriteria 2
    ):
        return "HIGH"
    
    # Kriteria MEDIUM:
    if (
        (major == 0 and 8 <= moderate => 8) or    # Kriteria 1
        (major == 1 and 8 <= moderate <= 12) or    # Kriteria 2
        (major == 2 and 8 <= moderate <= 10)       # Kriteria 3
    ):
        return "MEDIUM"
    
    # Kriteria LOW:
    if (
        (major == 0 and moderate <= 7)    # Tidak ada major dan moderate 0-7
    ):
        return "LOW"
    
    # Default case
    return "LOW"

# Streamlit untuk antarmuka
st.title("Kalkulator Risk Issue")

# Input jumlah temuan
minor = st.number_input("Masukkan jumlah temuan Minor:", min_value=0, step=1)
moderate = st.number_input("Masukkan jumlah temuan Moderate:", min_value=0, step=1)
major = st.number_input("Masukkan jumlah temuan Major:", min_value=0, step=1)

# Checkbox untuk "Terdapat Fraud"
fraud = st.checkbox("Terdapat Fraud")

# Hitung rating
rating = calculate_rating(minor, moderate, major, fraud)

# Tampilkan hasil
st.write(f"Rating Audit Issue Anda adalah: **{rating}**")
