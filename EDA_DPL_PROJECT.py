import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame(pd.read_csv("EDA_DPL_DATASET.csv"))

# Streamlit App
st.title('Data Visualization App For Crimes committed Against Women')

# Dropdown for selecting x-axis column
x_column = st.selectbox('Select X-axis Column:', df.columns)

# Dropdown for selecting y-axis column
y_column = st.selectbox('Select Y-axis Column:', df.columns)

# Dropdown for selecting plot type
plot_type = st.selectbox('Select Plot Type:', ['Line', 'Bar', 'Histogram', 'Scatter', 'Area', 'Box', 'Violin'])

# Plot the selected graph
if plot_type == 'Line':
    fig = px.line(df, x=x_column, y=y_column, title=f'Line Plot: {y_column} over {x_column}')
elif plot_type == 'Bar':
    fig = px.bar(df, x=x_column, y=y_column, title=f'Bar Plot: {y_column} vs {x_column}')
elif plot_type == 'Histogram':
    fig = px.histogram(df, x=x_column, y=y_column, title=f'Histogram: {y_column} distribution over {x_column}')
elif plot_type == 'Scatter':
    fig = px.scatter(df, x=x_column, y=y_column, title=f'Scatter Plot: {y_column} vs {x_column}')
elif plot_type == 'Area':
    fig = px.area(df, x=x_column, y=y_column, title=f'Area Plot: {y_column} over {x_column}')
elif plot_type == 'Box':
    fig = px.box(df, x=x_column, y=y_column, title=f'Box and Whisker Plot: {y_column} over {x_column}')
elif plot_type == 'Violin':
    fig = px.violin(df, x=x_column, y=y_column, title=f'Violin Plot: {y_column} over {x_column}')

# Show the plot
st.plotly_chart(fig)
