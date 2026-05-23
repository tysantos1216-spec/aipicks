import streamlit as st
import pandas as pd

st.title("🏀 AI +EV NBA Indicator")
df = pd.read_csv("data/processed.csv")

# Filter Green (Good) vs Red (Bad)
green = df[df['edge'] > 3]

st.subheader("High Edge Plays (>3%)")
st.table(green[['Player', 'Edge', 'Status']])