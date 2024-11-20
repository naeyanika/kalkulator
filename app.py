import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data

criteria = {
    "Rating": ["HIGH", "MEDIUM", "LOW"],
    "Minor_Min": [0, 0, 0],
    "Minor_Max": [2, 2, 2],
    "Moderate_Min": [8, 1, 0],
    "Moderate_Max": [15, 12, 7],
    "Fraud": [True, False, False]
}


criteria_df = pd.DataFrame(criteria)


st.title("Kalkulator Risk Issue")


minor = st.number_input("Masukkan jumlah temuan Minor:", min_value=0, step=1)
moderate = st.number_input("Masukkan jumlah temuan Moderate:", min_value=0, step=1)
major = st.number_input("Masukkan jumlah temuan Major:", min_value=0, step=1)


fraud = st.checkbox("Terdapat Fraud")


def calculate_rating(minor, moderate, major, fraud):
    if fraud:
        return "HIGH"
    for _, row in criteria_df.iterrows():
        if (
            row["Minor_Min"] <= minor <= row["Minor_Max"]
            and row["Moderate_Min"] <= moderate <= row["Moderate_Max"]
            and not fraud
        ):
            return row["Rating"]
    return "LOW"


rating = calculate_rating(minor, moderate, major, fraud)

st.write(f"Rating Audit Issue Anda adalah: **{rating}**")
