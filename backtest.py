import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define traditional portfolio allocations
traditional_portfolios = {
    '60/40 Portfolio': {'SPY': 0.60, 'AGG': 0.40},
    'Risk Parity': {'SPY': 0.33, 'AGG': 0.33, 'GLD': 0.34},
    'All-Weather': {'SPY': 0.30, 'TLT': 0.40, 'IEF': 0.15, 'GLD': 0.07, 'DBC': 0.08},
    'Permanent Portfolio': {'SPY': 0.25, 'TLT': 0.25, 'GLD': 0.25, 'BIL': 0.25},
    'Barbell Strategy': {'SPY': 0.50, 'TLT': 0.25, 'GLD': 0.25}
}

# Download historical price data
start_date = '2000-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

def get_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    return data

# Fetch data for all portfolios
tickers = list(set(ticker for portfolio in traditional_portfolios.values() for ticker in portfolio.keys()))
data = get_data(tickers, start_date, end_date)

# Calculate daily returns
returns = data.pct_change().dropna()

# Compute portfolio returns
def compute_portfolio_returns(returns_df, weights):
    weights_array = np.array(list(weights.values()))
    return (returns_df[list(weights.keys())] * weights_array).sum(axis=1).dropna()

portfolio_returns = {name: compute_portfolio_returns(returns, weights) for name, weights in traditional_portfolios.items()}

# Calculate cumulative returns
portfolio_cum_returns = {name: 10000 * (1 + ret).cumprod() for name, ret in portfolio_returns.items()}

# Performance metrics
def calculate_metrics(portfolio_returns):
    cagr = (portfolio_returns[-1] ** (1 / ((len(portfolio_returns) - 1) / 252))) - 1
    volatility = np.std(portfolio_returns) * np.sqrt(252)
    sharpe_ratio = cagr / volatility if volatility != 0 else np.nan
    max_drawdown = ((portfolio_returns / portfolio_returns.cummax()) - 1).min()
    return cagr, volatility, sharpe_ratio, max_drawdown

metrics = {name: calculate_metrics(portfolio_cum_returns[name]) for name in traditional_portfolios.keys()}

# Print performance metrics
for name, (cagr, vol, sharpe, mdd) in metrics.items():
    print(f"{name} Performance Metrics:")
    print(f"CAGR: {cagr:.2%}")
    print(f"Volatility: {vol:.2%}")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {mdd:.2%}\n")

# Plot performance
plt.figure(figsize=(12,6))
for name, cum_returns in portfolio_cum_returns.items():
    plt.plot(cum_returns, label=name, linewidth=2)
plt.title('Cumulative Portfolio Returns')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.legend()
plt.grid()
plt.show()
