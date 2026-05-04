# Week 4 Activity 2 – Data Aggregation with SQL

## Requirements

```
pip install pandas
```

SQLite is built into Python so no extra install is needed.

## Usage

1. Put `world_happiness_dataset.csv` in the same folder as `activity2.py`
2. Run `python activity2.py`

## Query 1 – GDP Categories and Average Happiness

- `CASE WHEN` checks each country's GDP value and assigns a label: Low, Medium, or High
- `AVG() OVER (PARTITION BY ...)` calculates the average happiness for each category while keeping every country as its own row
- `ORDER BY GDP_Category, Happiness_Score DESC` sorts results by category then by highest happiness first

`CASE WHEN` works like an if/else — it goes through each condition in order and assigns the first one that matches. `PARTITION BY` inside the window function tells SQL to calculate the average separately for each GDP group instead of across the whole table.

## Query 2 – High vs Low Corruption Comparison

- `CASE WHEN` labels each country as High or Low corruption using the dataset average as the cutoff
- `(SELECT AVG(Perceptions_of_Corruption) FROM happiness)` is a subquery that calculates the average from the data so no value needs to be hardcoded
- `GROUP BY` collapses all countries in each group into one summary row
- `AVG()` is applied to happiness, GDP, social support, and freedom to compare both groups across multiple indicators
