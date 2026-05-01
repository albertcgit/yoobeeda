# Week 3 - Activity 1: Correlation Analysis

## Dataset
age_networth.csv with 10 rows. It has two columns: Age and Net Worth.

## How to Run
- Install libraries: pip install pandas matplotlib scipy
- Run the script: python W3A1.py

## Results
- Pearson r = 0.88
- Spearman rho = 0.91
- R-squared = 77.86%
- p-value = 0.00073
- Slope = $17,046 per year

## What the Results Mean
- Pearson r = 0.88 means there is a strong link between age and net worth. When age goes up, net worth goes up too.
- R-squared = 77.86% means age explains about 78% of the change in net worth. The other 22% comes from other things not in the data.
- p-value = 0.00073 means the result is real and not by chance.
- Slope = $17,046 means for every one year increase in age, net worth goes up by about $17,000 on average.

## Plot
The scatter plot shows the data points going up from left to right. The red line fits the trend well. The residual plot shows points spread around zero with no clear pattern. This means the linear model is a good fit.
