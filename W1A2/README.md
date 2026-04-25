# Housing Prices Dataset
**Week 1 – Activity 2 | Yoobee Colleges**  
**Dataset:** https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

---

## The Story
A real estate agency wants to understand what drives house prices. Using 546 property records, we explore and summarise the data to uncover key pricing patterns.

---

## Analytics Type
**Descriptive Analytics** — *"Deals with what happened in the past"*  
Techniques used: **Data Aggregation** + **Data Mining**

---

## Dataset
- **546 rows**, **13 features**, **1 target: price**
- Features: area, bedrooms, bathrooms, stories, parking, airconditioning, furnishingstatus, and more

---

## Findings
1. Price generally increases with more bedrooms
2. More bathrooms and parking spaces raise the price
3. Larger homes have a higher average price
4. Price is not determined by one factor alone

---

## Output
- Findings printed to console
- `chart_housing.png` — 2x2 bar charts (bedrooms, bathrooms, parking, area size vs price)

---

## How to Run
```
pip install pandas matplotlib
python housing_prices.py
```
> Place `Housing.csv` in the same folder as the script.
