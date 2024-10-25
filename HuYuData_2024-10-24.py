import numpy as np
from scipy.stats import norm
import yfinance as yf
from datetime import datetime


# Black-Scholes function
def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


# Fetch GM stock price
ticker = 'GM'
data = yf.Ticker(ticker)
stock_price = data.history(period='1d')['Close'].iloc[-1]

# Parameters
S = stock_price  # Current stock price of GM
K = 40  # Example strike price
T = (datetime(2024, 12, 31) - datetime.now()).days / 365  # Time to expiration (1 year)
r = 0.05  # Risk-free interest rate (5%)
sigma = 0.30  # Volatility (30%, based on historical data for GM stock)

# Calculate option prices
call_option_price = black_scholes(S, K, T, r, sigma, 'call')
put_option_price = black_scholes(S, K, T, r, sigma, 'put')

print(f"General Motors (GM) Stock Price: {S:.2f}")
print(f"Call Option Price: {call_option_price:.2f}")
print(f"Put Option Price: {put_option_price:.2f}")