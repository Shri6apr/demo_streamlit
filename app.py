import streamlit as st
import pandas as pd
import os

st.title("📊 Excel to CSV Converter")

uploaded_file = st.file_uploader(
    "Upload Excel file (.xlsx only recommended)",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    try:
        filename = uploaded_file.name.lower()

        if filename.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, engine="openpyxl")

        elif filename.endswith(".xls"):
            df = pd.read_excel(uploaded_file, engine="xlrd")

        else:
            st.error("Unsupported file type")
            st.stop()

        st.success("✅ Excel file read successfully")
        st.dataframe(df.head())

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download CSV",
            csv,
            "converted.csv",
            "text/csv"
        )

    except Exception as e:
        st.error("❌ Unable to read the uploaded file")
        st.info(
            "Make sure the file is a real Excel file, "
            "not a CSV or renamed file."
        )
        st.exception(e)
``
