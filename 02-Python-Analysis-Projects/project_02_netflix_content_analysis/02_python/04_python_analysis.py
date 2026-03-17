import pandas as pd

# Load Cleaned Dataset:
df = pd.read_csv("../01_data/cleaned_dataset.csv")

# Convert date_added to Datetime Again:
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")


# -------------------------------------
# Movies vs TV Shows:
# -------------------------------------
content_type_counts = df["type"].value_counts()

print("\nContent Type Distribution: ")
print(content_type_counts)


# ------------------------------------
# Top 10 Countries:
# ------------------------------------
country_counts = df["country"].dropna().value_counts().head(10)

print("\nTop 10 Countries: ")
print(country_counts)


# ------------------------------------
# Content Added Per Year:
# ------------------------------------
df["year_added"] = df["date_added"].dt.year
content_by_year = df["year_added"].value_counts().sort_index()

print("\nContent Added Per Year: ")
print(content_by_year)


# ------------------------------------
# Top 10 Genres:
# ------------------------------------
genre_counts = df["listed_in"].str.split(", ").explode().value_counts().head(10)

print("\nTop 10 Gemres: ")
print(genre_counts)


# ------------------------------------
# Movies vs TV Shows Over Time:
# ------------------------------------
content_trend = df.groupby(["year_added", "type"]).size().unstack()

print("\nContent Trend By Type Over Time: ")
print(content_trend)
