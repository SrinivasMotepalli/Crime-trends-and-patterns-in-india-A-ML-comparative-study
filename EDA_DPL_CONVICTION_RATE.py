import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("EDA_DPL_DATASET.csv")

# Streamlit App
st.title('Conviction Rates for Crimes Against Women')

# Dropdown for selecting crime type
crime_type_column = 'Group_Name'
crime_type = st.selectbox('Select Crime Type:', df[crime_type_column].unique())

# Filter data for the selected crime type
filtered_df = df[df[crime_type_column] == crime_type]

# Group by crime type and calculate average conviction rate
conviction_rates = filtered_df.groupby(crime_type_column)[['Convicted', 'Arrested']].mean().reset_index()

# Calculate conviction rate
conviction_rates['Conviction_Rate'] = conviction_rates['Convicted'] / conviction_rates['Arrested']

# Bar Plot for Conviction Rates
fig_conviction_rates = px.bar(conviction_rates, 
                              x=crime_type_column, 
                              y='Conviction_Rate', 
                              title=f'Conviction Rates for {crime_type}')
st.plotly_chart(fig_conviction_rates)
