def calculate_ev(win_prob, decimal_odds):
    # EV = (Probability of Winning * Profit) - (Probability of Losing * Stake)
    # Simplified: (Win_Prob * Decimal_Odds) - 1
    return (win_prob * decimal_odds) - 1

# Example usage:
# If you calculate a 55% chance to win (0.55) and odds are -110 (1.91 decimal)
# EV = (0.55 * 1.91) - 1 = 0.0505 (5.05% edge)