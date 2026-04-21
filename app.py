import streamlit as st
import pandas as pd

st.title("📊 Excel to CSV Converter")

uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")

        st.success("File read successfully ✅")
        st.subheader("Preview")
        st.dataframe(df.head())

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download CSV",
            csv,
            "converted.csv",
            "text/csv"
        )

    except Exception as e:
        st.error("Error reading Excel file")
        st.exception(e)
