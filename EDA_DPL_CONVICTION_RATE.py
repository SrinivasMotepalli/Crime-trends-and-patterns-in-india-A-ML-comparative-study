import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("EDA_DPL_DATASET.csv")

# Streamlit App
st.title('Conviction Rates for Crimes Against Women')

# Dropdown for selecting crime type
crime_type = st.selectbox('Select Crime Type:', df['Crime_Type'].unique())

# Group by crime type and calculate average conviction rate
conviction_rates = df.groupby('Crime_Type')[['Convicted', 'Arrested']].mean().reset_index()

# Calculate conviction rate
conviction_rates['Conviction_Rate'] = conviction_rates['Convicted'] / conviction_rates['Arrested']

# Bar Plot for Conviction Rates
fig_conviction_rates = px.bar(conviction_rates, 
                              x='Crime_Type', 
                              y='Conviction_Rate', 
                              title='Conviction Rates for Crimes Against Women')
st.plotly_chart(fig_conviction_rates)
