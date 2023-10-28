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
plot_type = st.selectbox('Select Plot Type:', ['Line', 'Bar', 'Histogram', 'Scatter', 'Area', 'Box', 'Violin'])

# Filter data for state-wise analysis
area_name = st.selectbox('Select State:', df['Area_Name'].unique())

filtered_df = df[df['Area_Name'] == area_name]

# Plot the selected graph
if plot_type == 'Line':
    fig = px.line(filtered_df, x=x_column, y=y_column, title=f'Line Plot: {y_column} over {x_column} - {area_name}')
elif plot_type == 'Bar':
    fig = px.bar(filtered_df, x=x_column, y=y_column, title=f'Bar Plot: {y_column} vs {x_column} - {area_name}')
elif plot_type == 'Histogram':
    fig = px.histogram(filtered_df, x=x_column, y=y_column, title=f'Histogram: {y_column} distribution over {x_column} - {area_name}')
elif plot_type == 'Scatter':
    fig = px.scatter(filtered_df, x=x_column, y=y_column, title=f'Scatter Plot: {y_column} vs {x_column} - {area_name}')
elif plot_type == 'Area':
    fig = px.area(filtered_df, x=x_column, y=y_column, title=f'Area Plot: {y_column} over {x_column} - {area_name}')
elif plot_type == 'Box':
    fig = px.box(filtered_df, x=x_column, y=y_column, title=f'Box and Whisker Plot: {y_column} over {x_column} - {area_name}')
elif plot_type == 'Violin':
    fig = px.violin(filtered_df, x=x_column, y=y_column, title=f'Violin Plot: {y_column} over {x_column} - {area_name}')

# Show the plot
st.plotly_chart(fig)

