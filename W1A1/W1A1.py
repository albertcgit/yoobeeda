import pandas as pd
import matplotlib.pyplot as plt
 
# load the file
df = pd.read_excel("Data_set_w1A1.xlsx", sheet_name="descriptive_aggregation (1)")
 
# show the data
print("Data Preview:")
print(df.to_string(index=False))
 
# aggregation summary
summary = df.groupby("category")[["sales_sum", "sales_mean", "sales_count"]].sum().reset_index()
print("\nAggregated Summary:")
print(summary.to_string(index=False))
 
# anlayze
best = df.loc[df["sales_sum"].idxmax(), "category"]
print("\nInsight: Category " + best + " has the highest total sales.")
 
# bar chart
plt.bar(df["category"], df["sales_sum"], color=["#534AB7", "#1D9E75", "#D85A30"])
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales ($)")
plt.savefig("final_output.png")
plt.show()