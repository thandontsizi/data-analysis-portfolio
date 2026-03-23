import pandas as pd

# Load Dataset:
df = pd.read_csv("../01_data/msft_stock_prices.csv")


print("\nDataset Shape: ")
print(df.shape)

print("\nColumn Names: ")
print(df.columns)

print("\nData Types: ")
print(df.dtypes)

print("\nMissing Values: ")
print(df.isnull().sum())

print("\nDuplicated Rows: ")
print(df.duplicated().sum())

print("\nPreview: ")
print(df.head())
