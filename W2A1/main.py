import pandas as pd
import os

# Load and merge all 12 CSV files into one
csv_files = [f for f in os.listdir(".") if f.startswith("PRSA_Data") and f.endswith(".csv")]
data = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Display first 5 rows
print("--- First 5 Rows ---")
print(data.head())

# Show column names and data types
print("\n--- Column Names and Data Types ---")
print(data.dtypes)

# Count total rows and columns
rows, columns = data.shape
print(f"\nTotal Rows: {rows}")
print(f"Total Columns: {columns}")