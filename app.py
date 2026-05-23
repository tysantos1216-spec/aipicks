import streamlit as st
import pandas as pd
import os

# 1. Define your styling function separately at the top
def color_edge(val):
    color = 'green' if val > 5 else 'orange' if val > 0 else 'red'
    return f'color: {color}'

st.title("🏀 AI +EV NBA Indicator")

# 2. Safely load the data
data_path = "data/processed.csv"

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    
    # 3. Only attempt to style and display if df exists
    if 'edge' in df.columns:
        st.subheader("🚀 Live Betting Edge (Today's Games)")
        # Now this line is safe because it's inside the 'if' block
        st.dataframe(df.style.applymap(color_edge, subset=['edge']))
    else:
        st.error("Data loaded, but 'edge' column is missing.")
else:
    # This prevents the crash when the file isn't there
    st.warning("⚠️ Data file not found. The scraper is currently processing live odds...")