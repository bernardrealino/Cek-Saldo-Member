import streamlit as st
from sheetparser import read_google_sheet_value_by_id

SHEET_URL = "https://docs.google.com/spreadsheets/d/18LKei_sTHq6nJ7pqanun0GWbCiwF7WE-pwZQqbGL84o/edit?usp=sharing"

st.title("Data Member")
text_id = st.text_input("Masukkan ID Member Kamu")
if st.button("Cek Data"):
    st.write(read_google_sheet_value_by_id(SHEET_URL, text_id))