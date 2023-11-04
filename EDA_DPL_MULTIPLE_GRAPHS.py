import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("EDA_DPL_DATASET.csv")

# Streamlit App
st.title('Data Visualization App For Crimes committed Against Women')

# Dropdown for selecting x-axis column
x_column = st.selectbox('Select X-axis Column:', df.columns)

# Dropdown for selecting y-axis column
y_column = st.selectbox('Select Y-axis Column:', df.columns)

# Dropdown for selecting plot type
plot_type = st.selectbox('Select Plot Type:', ['Bar', 'Histogram', 'Scatter', 'Area'])

# Dropdown for selecting state
states = ['None'] + sorted(df['Area_Name'].str.strip().unique(), key=str.lower)
selected_state = st.selectbox('Select State:', states)

# Dropdown for selecting year
years = ['None'] + sorted(df['Year'].unique())
selected_year = st.selectbox('Select Year:', years)

# Filter data for state-wise and year-wise analysis
if selected_state == 'None':
    filtered_df = df
else:
    filtered_df = df[df['Area_Name'].str.strip().str.lower() == selected_state.lower().strip()]

# MODIFICATION: We have added a catogorical column to our streamlit app this helps the user get the data as year wise where the user can select which year they need to display. 
if selected_year != 'None':
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]

# Plot the selected graph
try:
    if plot_type == 'Bar':
        fig = px.bar(filtered_df, x=x_column, y=y_column, title=f'Bar Plot: {y_column} vs {x_column} - {selected_state} - {selected_year}')
    elif plot_type == 'Histogram':
        fig = px.histogram(filtered_df, x=x_column, y=y_column, title=f'Histogram: {y_column} distribution over {x_column} - {selected_state} - {selected_year}')
    elif plot_type == 'Scatter':
        fig = px.scatter(filtered_df, x=x_column, y=y_column, title=f'Scatter Plot: {y_column} vs {x_column} - {selected_state} - {selected_year}')
    elif plot_type == 'Area':
        fig = px.area(filtered_df, x=x_column, y=y_column, title=f'Area Plot: {y_column} over {x_column} - {selected_state} - {selected_year}')
    else:
        st.warning("Selected plot type is not supported.")
except ValueError as e:
    st.error(f"Error: {e}")

# Show the plot
st.plotly_chart(fig)

