import pandas as pd

# Load Dataset:
df = pd.read_csv("../01_data/netflix_titles.csv")

# -----------------------------------
# Convert date_added to datetime:
# -----------------------------------
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# -----------------------------------
# Handle missing rating value:
# -----------------------------------
df["rating"] = df["rating"].fillna("Unknown")

# -----------------------------------
# Save cleaned dataset:
# -----------------------------------
df.to_csv("../01_data/cleaned_dataset.csv", index=False)

# -----------------------------------
# Verification:
# -----------------------------------
print("\nCleaned Dataset Shape: ")
print(df.shape)

print("\nMissing Values After Cleaning: ")
print(df.isnull().sum())

print("\nPreview: ")
print(df.head(10))
