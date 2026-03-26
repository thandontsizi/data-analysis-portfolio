# 04_analysis.py
# MSFT Stock Analysis.
# Purpose: Create analytical features from cleaned stock data.

import pandas as pd

# Load cleaned dataset:
df = pd.read_csv("../01_data/cleaned_msft_stock_prices.csv")

# Convert 'Date' to datetime format:
df["Date"] = pd.to_datetime(df["Date"])

# Daily return calculation:
df["Daily_Return"] = df["Close"].pct_change()

# Moving Averages (trend smoothing):
df["MA_7"] = df["Close"].rolling(window=7).mean()
df["MA_30"] = df["Close"].rolling(window=30).mean()

# Volatility (stability measure):
df["Volatility_7"] = df["Daily_Return"].rolling(window=7).std()

# Extract time components for grouping and summarising data:
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Basic aggregation (summaries):
yearly_avg = df.groupby("Year")["Close"].mean()
print("Yearly Average Close Price: ")
print(yearly_avg)

monthly_avg = df.groupby(["Year", "Month"])["Close"].mean()
print("\nMonthly Average Close Price: ")
print(monthly_avg)

# Identify extremes (peaks & lows):
max_price = df["Close"].max()
print("\nMaximum Close Price: ", max_price)

min_price = df["Close"].min()
print("\nMinimum Close Price: ", min_price)

# Final data check:
print("\nDataset Info: ")
print(df.info())

print("\nDataset Preview: ")
print(df.head())

# Save analysed dataset with new columns:
df.to_csv("../01_data/analysed_msft_stock_prices.csv", index=False)
