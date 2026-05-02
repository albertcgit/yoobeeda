# Week 3 - Activity 2: Data Cleaning & Correlation Analysis

## Requirements
pip install pandas matplotlib

## How to Run
Place messy_dataset_Mukesh.csv in the same folder then run:
python data_analysis.py

## What the Script Does
- Cleans the raw dataset and saves messy_dataset_Mukesh_cleaned.csv
- Produces a boxplot to check for outliers
- Produces a Pearson correlation heatmap

## Issues Found and Fixed
- Text-encoded numbers replaced with actual values
- Wrong country code AU corrected to AUS
- Invalid and missing dates coerced to NaT
- Duplicate Bob rows merged into one
- Missing numeric values left as NaN
- Missing text values filled with Unknown

## Outlier Detection
No outliers found. Age IQR = 9.25, bounds = 12.6 to 49.6. Salary IQR = 7000, bounds = 48250 to 76250.

## Correlation Results
- Age vs Salary (r=0.63): Moderate positive. Older employees tend to earn more.
- Salary vs Company Tenure (r=0.01): Almost no relationship.
- Salary vs Country (r=0.35): Weak positive. AUS employees earn slightly more.
- Age vs Company Tenure (r=0.72): Strong positive. Older employees have longer tenure.
- Company Tenure vs Country (r=-0.79): Strong negative. NZ employees have longer tenure.
- Age vs Country (r=0.00): No relationship.

## Note
Currency is unknown. Same currency assumed for all employees.
