# Beijing Air Quality Dataset
From: https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data

This is the dataset from Beijing. It is about the air quality. The data is from year 2013 to 2017.

## Files used

The 12 CSV files inside the folder PRSA_Data_20130301-20170228. Each file is one station. All files have same columns like PM2.5, temperature, wind, and other air data.

## Other files

data.csv and test.csv - seems to be stock market data, not air quality.
The JPG file - irrelevant picture

## How to Run the code

Step 1. Download and unzip the dataset.

Step 2. Put all 12 CSV files and the beijing_air_quality.py in one folder.

Step 3. Install pandas.
   pip install pandas

Step 4. Run the program.
   python main.py

Step 5. The output will show the first 5 rows of each station, the column names, and how many rows and columns.
