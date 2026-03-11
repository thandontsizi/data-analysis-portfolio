import pandas as pd

# Load Dataset:
df = pd.read_csv("../data/train.csv")


# Total Revenue:
total_revenue = df["Sales"].sum().round(2)
print("\nTotal Revenue: ")
print(total_revenue)


# Revenue by Category:
print("\nRevenue by Category: ")
print(df.groupby("Category")["Sales"].sum().round(2).sort_values(ascending=False))


# Revenue by Region:
print("\nRevenue by Region: ")
print(df.groupby("Region")["Sales"].sum().round(2).sort_values(ascending=False))


# Top 10 Products by Revenue:
print("\nTop 10 Products by Revenue: ")
print(
	df.groupby("Product Name")["Sales"]
	.sum()
	.round(2)
	.sort_values(ascending=False)
	.head(10)
)


# Top 10 Customers by Revenue:
print("\nTop 10 Customers by Revenue: ")
print(
	df.groupby("Customer Name")["Sales"]
	.sum()
	.round(2)
	.sort_values(ascending=False)
	.head(10)
)
