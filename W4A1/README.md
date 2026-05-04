# Week 4 Activity 1 – World Happiness Data Visualization

## Requirements

```
pip install pandas numpy matplotlib seaborn
```

## Usage

1. Put the file `world_happiness_dataset.csv` in the same folder as `analysis.py`
2. Run `python analysis.py`
3. The output files will be saved in the `output/` folder

## Output Files

- `01_happiness_by_country.png` - Bar chart that shows happiness score for each country
- `02_correlation_heatmap.png` - Heatmap that shows how features relate to each other
- `03_boxplots.png` - Box plots that show the spread of each feature
- `04_scatter_factors.png` - Scatter plots that compare key factors to happiness score
- `05_stacked_contributions.png` - Stacked bar that shows how much each factor adds per country
- `06_happiness_distribution.png` - Histogram that shows how happiness scores are spread out

## Data Cleaning Steps

1. Checked for duplicate rows — none found
2. Checked for missing values — none found
3. Checked for outliers using the IQR method — none found
4. The dataset had no issues so it was used as it is

## Findings

- **Happiness by Country:** Canada (7.34) and Brazil (6.98) have the highest scores. South Africa (3.53), Denmark (3.61), and Germany (3.61) have the lowest.
- **Correlation Heatmap:** Freedom to Make Choices has the strongest link to happiness (r = 0.43). Generosity has the weakest link (r = 0.05).
- **Box Plots:** No outliers were found. Generosity has the most spread. GDP per Capita is a little skewed to the left.
- **Scatter Plots:** Freedom to Make Choices has the clearest positive trend with happiness. GDP per Capita is also positive but more spread out.
- **Stacked Contributions:** GDP per Capita and Social Support are the biggest factors for most countries. Generosity is the smallest factor across all countries.
- **Distribution:** Happiness scores are grouped around 3.5 to 4.5 and 6.0 to 7.0. The mean is 5.17 and the median is 5.00.
