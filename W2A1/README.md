# Beijing Air Quality Dataset
Dataset from Beijing about air quality from 2013 to 2017.
From: https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data

## Files to Use
12 CSV files inside PRSA_Data_20130301-20170228 folder. One file per station, same columns for all.

## Files to Ignore
data.csv and test.csv - stock market data, not related.
JPG file - just a photo, not related.

## How to Run
1. Download and unzip the dataset.
2. Put all 12 CSV files and beijing_air_quality.py in one folder.
3. Install pandas: pip install pandas
4. Run: python beijing_air_quality.py

## Output
The program merges all 12 files into one table around 420,768 rows. It will show the first 5 rows, column names and data types, and total rows and columns.

<img width="1441" height="737" alt="image" src="https://github.com/user-attachments/assets/32b5330d-f72b-44bc-a2db-5a95f5ecfebb" />
