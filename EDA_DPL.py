import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("EDA_DPL_DATASET.csv")

# Streamlit App
st.title('Correlation Analysis of Crimes Against Women')

# Dropdowns for selecting crime types
crime_type1 = st.selectbox('Select Crime Type 1:', df.columns.unique())
crime_type2 = st.selectbox('Select Crime Type 2:', df.columns.unique())

# Scatter plot for correlation analysis
fig_correlation = px.heatmap(df, x=crime_type1, y=crime_type2, title=f'Correlation Analysis: {crime_type1} vs {crime_type2}')
st.plotly_chart(fig_correlation)
