import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

DATASET_URL = 'https://www.bea.gov/system/files/2022-12/weekly-event-study-of-spending-estimates-v32-n1.csv'

st.title("Consumer Spending Data Viz")
st.markdown(f"Visualizes [bea.gov spending data]({DATASET_URL})")

df_all = pd.read_csv(DATASET_URL)

ms = st.multiselect("Industries to include", df_all.industry.unique())

df = df_all.query("industry in @ms")

st.dataframe(df)

fig = px.line(
  df,
  x="week_start_date",
  y="median",
  color="industry",
)

# Use the Streamlit theme.
# This is the default. So you can also omit the theme argument.
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
