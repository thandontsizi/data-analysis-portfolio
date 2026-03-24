import pandas as pd

# Load Dataset:
df = pd.read_csv("../01_data/msft_stock_prices.csv")

# Keep Only Raw Columns:
columns_to_keep = ["Date", "Open", "High", "Low", "Close", "Volume"]
df = df[columns_to_keep]

# Convert 'Date' to datetime format:
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print(df.dtypes)

# Sort Dataset:
df = df.sort_values("Date")

# Filter Dataset:
df = df[df["Date"] >= "2015-01-01"]

# Reset Index:
df = df.reset_index(drop=True)

# Save Cleaned Dataset:
df.to_csv("../01_data/cleaned_msft_stock_prices.csv", index=False)

print(df.info())
print(df.head())
