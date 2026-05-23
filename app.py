import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NBA AI Indicator", layout="wide")

st.title("🏀 AI +EV NBA Indicator")
st.write("Live analysis of player props and betting edges.")

data_path = "data/processed.csv"

# Check if file exists, if not, show a waiting message
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    
    # Filter for the "Green" indicator (Edge > 3%)
    if 'edge' in df.columns:
        green_bets = df[df['edge'] > 3]
        
        st.subheader("✅ High Value Plays (Edge > 3%)")
        if not green_bets.empty:
            st.table(green_bets)
        else:
            st.info("No high-value plays found at this time.")
            
        st.subheader("All Analyzed Props")
        st.dataframe(df)
    else:
        st.error("The data file exists but is missing the 'edge' column. Check your analyze.py logic.")
else:
    st.warning("⚠️ Data file not found. The scraper/analyzer is running in the background. Please refresh in a few minutes.")