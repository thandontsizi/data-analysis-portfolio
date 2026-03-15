import pandas as pd

# Load Dataset:
df = pd.read_csv("../data/train.csv")


# Total Revenue:
total_revenue = df["Sales"].sum().round(2)
print("\nTotal Revenue: ")
print(total_revenue)


# Revenue by Category:
print("\nRevenue by Category: ")
category_revenue = df.groupby("Category")["Sales"].sum().round(2).sort_values(ascending=False)
print(category_revenue)

# Percentage Contribution to Total Sales Per Category:
print("\nShare Per Category (%): ")
category_share = ((category_revenue / total_revenue) * 100).round(2)
print(category_share)


# Revenue by Region:
print("\nRevenue by Region: ")
region_revenue = df.groupby("Region")["Sales"].sum().round(2).sort_values(ascending=False)
print(region_revenue)

# Percentage Contribution to Total Sales Per Region:
print("\nShare Per Region (%): ")
region_share = ((region_revenue / total_revenue) * 100).round(2)
print(region_share)


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
