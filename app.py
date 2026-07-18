import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Retail Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Enterprise Retail Dashboard")
st.markdown("A simple Streamlit dashboard")

# Upload data
uploaded_file = st.file_uploader("C:\DINNESH FILES\GUVI FILES\PROJECT FROM GUVI\FINAL PROJECT\inventory_recommendations.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Data Loaded Successfully!")

    # Display data
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # KPIs
    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", len(df))

    with col2:
        st.metric("Columns", len(df.columns))

    with col3:
        numeric_cols = df.select_dtypes(include="number").columns
        st.metric("Numeric Columns", len(numeric_cols))

    # Numeric column selection
    if len(numeric_cols) > 0:
        st.subheader("Data Visualization")

        column = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig, ax = plt.subplots(figsize=(8,4))
        df[column].hist(ax=ax, bins=20)
        ax.set_title(f"Distribution of {column}")
        st.pyplot(fig)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

else:
    st.info("Please upload a CSV file to begin.")