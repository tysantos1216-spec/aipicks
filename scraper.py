# scraper.py
from balldontlie import BalldontlieAPI
import pandas as pd
import os

# Initialize the API client
api = BalldontlieAPI(api_key=os.getenv("API_KEY"))

def get_live_nba_data():
    # Fetch today's games (using current date)
    games = api.nba.games.list(dates=["2026-05-23"])
    
    # Fetch odds for those games
    odds = api.nba.betting.list(dates=["2026-05-23"])
    
    # Convert to DataFrame for easy analysis
    return pd.DataFrame(games), pd.DataFrame(odds)

# Save to your data folder
games_df, odds_df = get_live_nba_data()
games_df.to_csv("data/games.csv")
odds_df.to_csv("data/odds.csv")