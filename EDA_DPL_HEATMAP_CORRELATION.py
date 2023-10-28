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

# Calculate correlation matrix
correlation_matrix = df[[crime_type1, crime_type2]].corr()

# Heatmap for correlation analysis
fig_heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot(fig_heatmap.figure)
