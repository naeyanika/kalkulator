import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data

# Fungsi untuk menghitung rating
def calculate_rating(minor, moderate, major, fraud):
    if fraud:
        return "HIGH"
    
    # Kriteria untuk High
    if (
        (1 <= major <= 2 and moderate > 12) or 
        (major > 3) or 
        (moderate == 0 and major > 0)
    ):
        return "HIGH"
    
    # Kriteria untuk Medium
    if (
        (major == 0 and 8 <= moderate <= 15) or
        (major == 1 and 8 <= moderate <= 12) or
        (major == 2 and 8 <= moderate <= 10)
    ):
        return "MEDIUM"
    
    # Kriteria untuk Low
    if (
        major == 0 and (moderate == 0 or 1 <= moderate <= 7)
    ):
        return "LOW"
    
    # Default jika tidak masuk kriteria
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
