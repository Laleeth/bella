import streamlit as st
import pandas as pd


# Streamlit app title
st.title("Excel Data Analysis and Forecast")

# File uploader for Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Display the raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    
