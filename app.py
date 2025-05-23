import streamlit as st
import pandas as pd
import sweetviz as sv
import os

st.set_page_config(layout="wide")
st.title("📊 Student Data Profiler (Sweetviz)")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("👀 Preview of your data:")
    st.dataframe(df.head())

    st.subheader("📈 Generating Sweetviz Report...")
    report = sv.analyze(df)
    report_path = "sweetviz_report.html"
    report.show_html(report_path, open_browser=False)

    with open(report_path, "r", encoding="utf-8") as f:
        html = f.read()
        st.components.v1.html(html, height=800, scrolling=True)
