import streamlit as st
import pandas as pd

# Streamlit app title
st.title("Price Data Analysis and Forecast")

# Function to read CSV or Excel file
@st.cache_data
def read_file(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file, engine='openpyxl')
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return None
    return df

# File upload
file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xls', 'xlsx'])

if file is not None:
    df = read_file(file)
    if df is not None:
        # ---- SIDEBAR ----
        st.sidebar.header("Please Filter Here:")
        city = st.sidebar.multiselect(
            "Select the City:",
            options=df["Kitchen_City"].unique(),
            default=df["Kitchen_City"].unique()
        )
        
        customer_type = st.sidebar.multiselect(
            "Select the Special Price Type:",
            options=df["specialPrice"].unique(),
            default=df["specialPrice"].unique(),
        )
        
        gender = st.sidebar.multiselect(
            "Select the Category:",
            options=df["Category"].unique(),
            default=df["Category"].unique()
        )
        diet = st.sidebar.multiselect(
            "Select the Diet:",
            options=df["Diet"].unique(),
            default=df["Diet"].unique()
        )
        
        food_type = st.sidebar.multiselect(
            "Select the Type:",
            options=df["Type"].unique(),
            default=df["Type"].unique()
        )
        
        df_selection = df.query(
            "Kitchen_City == @city & specialPrice == @customer_type & Category == @gender & Diet == @diet & Type == @food_type"
        )
        
        st.dataframe(df_selection)

