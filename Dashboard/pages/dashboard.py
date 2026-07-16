import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# streamlit run home.py
#st.title("Home page of dashboard")

# 16 July 2026

# Page Configuration
st.set_page_config(
    page_title="Car Crashes Dashboard",
    page_icon="🙌",# Window + .
    layout = 'wide'
)

# Load Dataset
df = sns.load_dataset("car_crashes")

df["State"] = df["abbrev"]

# Sidebar
st.sidebar.title("Dashboard Filters")
st.sidebar.multiselect(
    "Select State",
    options = df["State"],
    default = df["State"]

)

# Title
st.title("Explore the insights here ✌")

#KPI Cards -> Key Performance Indicator
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Accidents %",
    round(df['total'].mean()),'%'
)

col2.metric(
    "Average Speeding %",
    round(df['speeding'].mean()),'%'
)

col3.metric(
    "Average Alcoholic %",
    round(df['alcohol'].mean()),'%'
)

st.dataframe(df)
