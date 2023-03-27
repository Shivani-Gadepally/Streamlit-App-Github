import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

# Load data
data = pd.read_csv('drinks.csv')

st.title('Graph from Midterm Data')

# Sidebar filters
x_col = st.sidebar.selectbox('X-axis', data.columns)
y_col = st.sidebar.selectbox('Y-axis', data.columns)


# Plot line chart
line_chart = alt.Chart(data).mark_line().encode(
    x=x_col,
    y=y_col,

).properties(
    width=800,
    height=500
)
st.altair_chart(line_chart)