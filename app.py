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
    import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Refresh the app every 60 seconds (60000 milliseconds)
count = st_autorefresh(interval=60000, key="nba_dashboard_refresh")

# ... rest of your code ...
st.title("🏀 AI +EV NBA Indicator")
# Your logic to read data/processed.csv goes here
import streamlit as st
import pandas as pd

def show_live_predictions():
    st.subheader("🚀 Live Betting Edge (Today's Games)")
    
    # Load your processed predictions
    if os.path.exists("data/processed.csv"):
        df = pd.read_csv("data/processed.csv")
        
        # Display only high-confidence plays
        # Edge > 3% is generally considered a strong signal
        plays = df[df['edge'] > 3.0]
        
        for index, row in plays.iterrows():
            with st.container(border=True):
                col1, col2, col3 = st.columns(3)
                col1.metric("Matchup", f"{row['away_team']} @ {row['home_team']}")
                col2.metric("Edge", f"{row['edge']:.2f}%")
                col3.write(f"Bet: {row['recommended_side']}")
    else:
        st.info("Analysis engine is currently processing live odds...")

# Call this in your main layout
show_live_predictions()
def color_edge(val):
    color = 'green' if val > 5 else 'orange' if val > 0 else 'red'
    return f'color: {color}'

st.dataframe(df.style.applymap(color_edge, subset=['edge']))
import streamlit as st
import pandas as pd

def show_live_predictions():
    st.subheader("🚀 Live Betting Edge (Today's Games)")
    
    # Load your processed predictions
    if os.path.exists("data/processed.csv"):
        df = pd.read_csv("data/processed.csv")
        
        # Display only high-confidence plays
        # Edge > 3% is generally considered a strong signal
        plays = df[df['edge'] > 3.0]
        
        for index, row in plays.iterrows():
            with st.container(border=True):
                col1, col2, col3 = st.columns(3)
                col1.metric("Matchup", f"{row['away_team']} @ {row['home_team']}")
                col2.metric("Edge", f"{row['edge']:.2f}%")
                col3.write(f"Bet: {row['recommended_side']}")
    else:
        st.info("Analysis engine is currently processing live odds...")

# Call this in your main layout
show_live_predictions()

def color_edge(val):
    # Your function logic here
    color = 'green' if val > 5 else 'orange' if val > 0 else 'red'
    return f'color: {color}'
    

st.dataframe(df.style.applymap(color_edge, subset=['edge']))
import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("🏀 NBA Live Betting Dashboard")

if os.path.exists("data/processed.csv"):
    df = pd.read_csv("data/processed.csv")
    
    # Filter for +EV plays
    high_value = df[df['edge'] > 0.03]
    st.dataframe(high_value)
else:
    st.warning("Data is currently syncing...")