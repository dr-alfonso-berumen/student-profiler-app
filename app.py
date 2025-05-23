import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit.components.v1 import components

st.set_page_config(layout="wide")
st.title("📊 Student Data Profiler")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ Data loaded with {df.shape[0]:,} rows and {df.shape[1]:,} columns.")

    # Show preview
    st.subheader("🧾 Data Preview")
    st.dataframe(df.head())

    # Generate the profile
    st.subheader("📈 Generating profiling report...")
    profile = ProfileReport(df, explorative=True)
    profile_html = profile.to_html()

    # Display in Streamlit
    components.html(profile_html, height=1000, scrolling=True)
