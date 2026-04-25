# Housing Prices – Descriptive Analytics
# Dataset: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

import pandas as pd
import matplotlib.pyplot as plt


# ── Load Data ─────────────────────────────────────────────────
df = pd.read_csv("Housing.csv")

# Check for missing values
if df.isnull().sum().sum() == 0:
    print("No missing values found.\n")
else:
    print("Missing values detected.\n")


# ── Data Aggregation ──────────────────────────────────────────
# Create area size groups: Small, Medium, Large
df["area_group"] = pd.cut(df["area"], bins=3, labels=["Small", "Medium", "Large"])

# Average price by key features
bedroom_avg  = df.groupby("bedrooms")["price"].mean()
bathroom_avg = df.groupby("bathrooms")["price"].mean()
parking_avg  = df.groupby("parking")["price"].mean()
area_avg     = df.groupby("area_group")["price"].mean()


# ── Story / Findings ──────────────────────────────────────────
print("Findings:")
print("1. Price generally increases with more bedrooms.")
print("2. More bathrooms and parking spaces raise the price.")
print("3. Larger homes have a higher average price.")
print("4. Price is not determined by one factor alone.\n")


# ── Charts ────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(9, 6))

bedroom_avg.plot(kind="bar", ax=axes[0, 0], color="teal")
axes[0, 0].set_title("Price by Bedrooms")
axes[0, 0].set_xlabel("Bedrooms")
axes[0, 0].set_ylabel("Avg Price")

bathroom_avg.plot(kind="bar", ax=axes[0, 1], color="steelblue")
axes[0, 1].set_title("Price by Bathrooms")
axes[0, 1].set_xlabel("Bathrooms")
axes[0, 1].set_ylabel("Avg Price")

parking_avg.plot(kind="bar", ax=axes[1, 0], color="slateblue")
axes[1, 0].set_title("Price by Parking")
axes[1, 0].set_xlabel("Parking")
axes[1, 0].set_ylabel("Avg Price")

area_avg.plot(kind="bar", ax=axes[1, 1], color="coral")
axes[1, 1].set_title("Price by Area Size")
axes[1, 1].set_xlabel("Area Size")
axes[1, 1].set_ylabel("Avg Price")

plt.suptitle("Housing Prices – Descriptive Analytics", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("chart_housing.png")
plt.show()
print("Chart saved as chart_housing.png")
