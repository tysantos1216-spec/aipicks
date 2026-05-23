import pandas as pd
import os

# Ensure the output directory exists
os.makedirs('data', exist_ok=True)

def calculate_edge(odds_a, odds_b, line_prizepicks):
    # Implied probability calculation
    prob_a = abs(odds_a) / (abs(odds_a) + 100) if odds_a < 0 else 100 / (odds_a + 100)
    prob_b = abs(odds_b) / (abs(odds_b) + 100) if odds_b < 0 else 100 / (odds_b + 100)
    fair_prob = prob_a / (prob_a + prob_b)
    return (fair_prob - 0.50) * 100

# Logic to load raw data and save processed data
if os.path.exists("data/raw_odds.csv"):
    df = pd.read_csv("data/raw_odds.csv")
    # Apply your logic (update column names to match your actual API data)
    df['edge'] = df.apply(lambda x: calculate_edge(x['odds_a'], x['odds_b'], x['pp_line']), axis=1)
    df.to_csv("data/processed.csv", index=False)