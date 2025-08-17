import pandas as pd

# Load historical asset prices
data = pd.read_csv('../data/asset_prices.csv', index_col='Date', parse_dates=True)

# Calculate daily returns
returns = data.pct_change().dropna()

# Save processed returns
returns.to_csv('../data/asset_returns.csv')
print("Data preprocessed and saved.")
