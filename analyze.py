# analyze.py
import pandas as pd

def process_edges():
    odds = pd.read_csv("data/odds.csv")
    
    # Example logic: Compare book odds to a 'Fair' line
    # If a book is -130 (56.5% prob) and your PrizePicks line is 50%,
    # that is a +6.5% edge.
    odds['edge'] = (odds['implied_prob'] - 0.50) * 100
    
    # Filter for "Green" (Good) plays
    indicators = odds[odds['edge'] > 3]
    indicators.to_csv("data/indicators.csv")

process_edges()