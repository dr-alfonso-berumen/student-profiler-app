import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit.components.v1 import html

st.set_page_config(layout="wide")
st.title("📊 Student Data Profiler")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("First few rows of your dataset:")
    st.dataframe(df.head())

    st.subheader("📈 Profiling Report")
    profile = ProfileReport(df, title="Profiling Report", explorative=True)
    profile.to_file("report.html")

    with open("report.html", "r", encoding='utf-8') as f:
        html_report = f.read()
        html(html_report, height=1000, scrolling=True)
