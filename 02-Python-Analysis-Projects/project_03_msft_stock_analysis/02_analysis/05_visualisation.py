# 05_visualisation.py
# MSFT Stock Analysis
# Purpose: Visualise trends, patterns, and stability in stock price data.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset:
df = pd.read_csv("../01_data/analysed_msft_stock_prices.csv")

# Convert 'Date' to datetime format:
df["Date"] = pd.to_datetime(df["Date"])

# Sort data:
df = df.sort_values("Date")

# Close price trend visualisation:
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Close"], label="Close Price:")

plt.title("MSFT Stock Close Price Over Time:")
plt.xlabel("Date:")
plt.ylabel("Price ($):")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../03_results/plots/close_price.png")
plt.close()

# Moving Average (trend smoothing):
plt.figure(figsize=(12, 6))

plt.plot(df["Date"], df["MA_7"], label="7-Day MA")
plt.plot(df["Date"], df["MA_30"], label="30-Day MA")

plt.title("MSFT Stock Price with Moving Averages:")
plt.xlabel("Date:")
plt.ylabel("Price ($):")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../03_results/plots/moving_averages.png")
plt.close()

# Daily return:
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Daily_Return"], label="Daily Return")

plt.title("MSFT Daily Returns:")
plt.xlabel("Date:")
plt.ylabel("Daily Return:")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../03_results/plots/daily_returns.png")
plt.close()

# Volatility:
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Volatility_7"], label="7-Day Volatility")

plt.title("MSFT 7-Day Rolling Volatility:")
plt.xlabel("Date:")
plt.ylabel("Volatility:")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../03_results/plots/volatility.png")
plt.close()

# Yearly average price:
yearly_avg = df.groupby("Year")["Close"].mean()

plt.figure(figsize=(12, 6))
plt.bar(yearly_avg.index, yearly_avg.values)

plt.title("MSFT Yearly Average Close Price:")
plt.xlabel("Year:")
plt.ylabel("Average Price ($):")
plt.grid(True)
plt.tight_layout()
plt.savefig("../03_results/plots/yearly_average.png")
plt.close()
