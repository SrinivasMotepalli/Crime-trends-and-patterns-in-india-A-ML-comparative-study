import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("EDA_DPL_AFTER_ROBUST_SCALLING.csv")

# Streamlit App
st.title('Conviction Rates for Crimes Against Women')

# Dropdown for selecting crime type
crime_type_column = 'Group_Name'
crime_type = st.selectbox('Select Crime Type:', df[crime_type_column].unique())

# Dropdown for selecting state
states = ['None'] + sorted(df['Area_Name'].str.strip().unique(), key=str.lower)
selected_state = st.selectbox('Select State:', states)

# Dropdown for selecting year
years = ['None'] + sorted(df['Year'].unique())
selected_year = st.selectbox('Select Year:', years)

# Filter data for state-wise, crime type, and year analysis
if selected_state == 'None':
    filtered_df = df[df[crime_type_column] == crime_type]
else:
    filtered_df = df[(df['Area_Name'].str.strip().str.lower() == selected_state.lower().strip()) & (df[crime_type_column] == crime_type)]

# Filter data for the selected year
if selected_year != 'None':
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]

# Calculate conviction rate
conviction_rate = max(min((filtered_df['Convicted'].sum() / filtered_df['Arrested'].sum()) * 100, 100), 0)

# Display Conviction Rate as percentage
st.write(f'Conviction Rate for {crime_type} in {selected_state} in {selected_year if selected_year != "None" else "all years"}: {conviction_rate:.2f}%')


