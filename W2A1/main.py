import pandas as pd
import os

# Load all CSV files in the same folder
csv_files = [f for f in os.listdir(".") if f.startswith("PRSA_Data") and f.endswith(".csv")]

for file in csv_files:
    data = pd.read_csv(file)

    # Display first 5 rows per station
    print(f"\n--- {file} ---")
    print(data.head())

    # Show column names and data types
    print(data.dtypes)

    # Count total rows and columns
    rows, columns = data.shape
    print(f"Total Rows: {rows}")
    print(f"Total Columns: {columns}")