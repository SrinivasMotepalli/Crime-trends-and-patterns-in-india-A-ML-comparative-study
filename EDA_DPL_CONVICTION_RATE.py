import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("EDA_DPL_DATASET.csv")

# Streamlit App
st.title('Conviction Rates for Crimes Against Women')

# Dropdown for selecting crime type
crime_type_column = 'Group_Name'
crime_type = st.selectbox('Select Crime Type:', df[crime_type_column].unique())

# Filter data for the selected crime type
filtered_df = df[df[crime_type_column] == crime_type]

# Calculate conviction rate
conviction_rate = max(min((filtered_df['Convicted'].sum() / filtered_df['Arrested'].sum()) * 100, 100), 0)

# Display Conviction Rate as percentage
st.write(f'Conviction Rate for {crime_type}: {conviction_rate:.2f}%')
