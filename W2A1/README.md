# Beijing Air Quality Dataset

Dataset from Beijing about air quality from 2013 to 2017.
Download: https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data


## Files to Use

12 CSV files inside PRSA_Data_20130301-20170228 folder. One file per station, same columns for all.


## Files to Ignore

data.csv and test.csv - stock market data, not related.
JPG file - just a photo, not needed.


## How to Run

1. Download and unzip the dataset.
2. Put all 12 CSV files and main.py in one folder.
3. Install libraries: pip install pandas matplotlib
4. Run: python main.py


## What the Program Does

Task 1 - Load and Inspect
Merges all 12 CSV files into one table around 420,768 rows. Shows first 5 rows, column names and data types, and total rows and columns.

Task 2 - Data Cleaning
Identifies missing values per column. Replaces missing values with the column mean. Removes remaining rows with missing values.

Task 3 - Basic Statistical Analysis
Shows mean, median, minimum, maximum, and standard deviation of PM2.5.

Task 4 - Data Filtering
Filters data by station. Calculates average pollution levels per station for PM2.5, PM10, SO2, NO2, CO, and O3.

Task 5 - Data Visualization
Saves 3 charts as PNG files in the same folder.
- histogram_pm25.png - distribution of PM2.5 values
- lineplot_pm25.png - PM2.5 over time for one station
- boxplot_pollutants.png - spread of all pollutants

Task 6 - Correlation Analysis
Shows which variable is most correlated with PM2.5. Also checks if temperature affects pollution levels.
