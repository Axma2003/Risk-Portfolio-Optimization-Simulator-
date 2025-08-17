import pandas as pd
import numpy as np

# Load processed returns
returns = pd.read_csv('../data/asset_returns.csv', index_col='Date', parse_dates=True)

# Portfolio simulation
num_portfolios = 10000
results = np.zeros((3, num_portfolios))

for i in range(num_portfolios):
    weights = np.random.random(returns.shape[1])
    weights /= np.sum(weights)
    
    portfolio_return = np.sum(weights * returns.mean()) * 252
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_std
    
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std
    results[2,i] = sharpe_ratio

# Convert to DataFrame
portfolio_results = pd.DataFrame(results.T, columns=['Return', 'Volatility', 'Sharpe'])
# Identify optimal portfolio
optimal_portfolio = portfolio_results.iloc[portfolio_results['Sharpe'].idxmax()]

print("Optimal Portfolio:")
print(optimal_portfolio)
portfolio_results.to_csv('../data/portfolio_simulation_results.csv')
