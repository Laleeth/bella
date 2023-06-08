import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

    # Generate bar chart
    st.subheader("Data Visualization - Bar Chart")
    st.write("Select the column for the x-axis:")
    x_axis = st.selectbox("X-axis", df.columns)
    st.write("Select the column for the y-axis:")
    y_axis = st.selectbox("Y-axis", df.columns)
    plt.bar(df[x_axis], df[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)

    # Download the processed data
    st.subheader("Download Processed Data")
    csv_data = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="processed_data.csv",
        mime="text/csv"
    )

    # Separate forecast for items
    st.subheader("Item Forecast")
    item_column = st.selectbox("Select the column for item names:", df.columns)
    forecast_data = df.groupby(item_column).sum()
    st.dataframe(forecast_data)
