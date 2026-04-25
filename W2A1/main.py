import pandas as pd
import matplotlib.pyplot as plt
import glob

# Task 1: Load all CSV files and merge into one table
csv_files = glob.glob("PRSA_Data*.csv")
data = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)

print("\nTask 1 - First 5 Rows:")
print(data.head())

print("\nTask 1 - Column Names and Data Types:")

print(data.dtypes)

rows, columns = data.shape
print(f"\nTotal Rows: {rows}")
print(f"Total Columns: {columns}")

# Task 2: Find and fix missing values
print("\nTask 2 - Missing Values per Column:")
print(data.isnull().sum())

data.fillna(data.select_dtypes(include="number").mean(), inplace=True)
data.dropna(inplace=True)

# Task 3: Basic statistics for all stations
print("\nTask 3 - Overall PM2.5 Statistics (All Stations):")
print(f"Mean:               {data['PM2.5'].mean():.2f} ug/m3")
print(f"Median:             {data['PM2.5'].median():.2f} ug/m3")
print(f"Minimum:            {data['PM2.5'].min():.2f} ug/m3")
print(f"Maximum:            {data['PM2.5'].max():.2f} ug/m3")
print(f"Standard Deviation: {data['PM2.5'].std():.2f} ug/m3")

# Task 4: Average pollution levels for all stations
print("\nTask 4 - Average Pollution Levels per Station:")
avg_all = data.groupby("station")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().round(2)
print(avg_all)

# Station selection for detailed analysis
stations = sorted(data["station"].unique())

print("\nTask 4 - Select a Station for Detailed Analysis:")
print("0. All Stations")
for i, name in enumerate(stations, 1):
    print(f"{i}. {name}")

choice = input("\nEnter number (0 for all): ").strip()

if choice == "0":
    selected = data
    label = "All Stations"
elif choice.isdigit() and 1 <= int(choice) <= len(stations):
    station_name = stations[int(choice) - 1]
    selected = data[data["station"] == station_name]
    label = station_name
else:
    print("Invalid choice. Showing all stations.")
    selected = data
    label = "All Stations"

print(f"\nStation: {label}")
print(f"Records: {len(selected)}")

print("\nAverage Pollution Levels:")
print(selected[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().round(2))

# Task 3 again: Statistics for selected station
print(f"\nTask 3 - PM2.5 Statistics for {label}:")
print(f"Mean:               {selected['PM2.5'].mean():.2f} ug/m3")
print(f"Median:             {selected['PM2.5'].median():.2f} ug/m3")
print(f"Minimum:            {selected['PM2.5'].min():.2f} ug/m3")
print(f"Maximum:            {selected['PM2.5'].max():.2f} ug/m3")
print(f"Standard Deviation: {selected['PM2.5'].std():.2f} ug/m3")

# Comparison
diff = selected['PM2.5'].mean() - data['PM2.5'].mean()
print(f"\nOverall mean: {data['PM2.5'].mean():.2f} ug/m3")
print(f"{label} mean: {selected['PM2.5'].mean():.2f} ug/m3")
if diff > 0:
    print(f"{label} is {diff:.2f} ug/m3 above the overall average.")
elif diff < 0:
    print(f"{label} is {abs(diff):.2f} ug/m3 below the overall average.")
else:
    print(f"{label} is equal to the overall average.")

# Task 5: Visualizations for selected station

print("\nTask 5 - Generating Charts...")

# Histogram of PM2.5
plt.figure(figsize=(8, 5))
selected["PM2.5"].dropna().plot(kind="hist", bins=50, color="steelblue", edgecolor="black")
plt.title(f"Histogram of PM2.5 - {label}")
plt.xlabel("PM2.5 (ug/m3)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_pm25.png")
plt.show()

# Line plot of PM2.5 over time
plt.figure(figsize=(12, 5))
selected["PM2.5"].reset_index(drop=True).plot(color="tomato")
plt.title(f"PM2.5 Over Time - {label}")
plt.xlabel("Record Index")
plt.ylabel("PM2.5 (ug/m3)")
plt.tight_layout()
plt.savefig("lineplot_pm25.png")
plt.show()

# Boxplot of pollutants
plt.figure(figsize=(10, 6))
selected[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].plot(kind="box")
plt.title(f"Boxplot of Pollutants - {label}")
plt.ylabel("Concentration (ug/m3)")
plt.tight_layout()
plt.savefig("boxplot_pollutants.png")
plt.show()

# Task 6: Correlation analysis
pollutant_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
corr_matrix = selected[pollutant_cols].corr()

print(f"\nTask 6 - Correlation with PM2.5 ({label}):")
corr_pm25 = corr_matrix["PM2.5"].sort_values(ascending=False).round(2)
print(corr_pm25)

most_correlated = corr_pm25.drop("PM2.5").idxmax()
print(f"\nMost correlated with PM2.5: {most_correlated} (r={corr_pm25[most_correlated]})")

print(f"\nTask 6 - Correlation between TEMP and PM2.5: {selected['TEMP'].corr(selected['PM2.5']):.4f}")