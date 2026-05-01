import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
df = pd.read_csv("age_networth.csv")

feature_x = "Age"
feature_y = "Net Worth"

x = df[feature_x]
y = df[feature_y]

# Pearson correlation: measures linear relationship strength (-1 to 1)
pearson_r, pearson_p = stats.pearsonr(x, y)

# Spearman correlation: measures monotonic relationship (robust to outliers)
spearman_r, spearman_p = stats.spearmanr(x, y)

# Linear regression: fits a line y = slope * x + intercept
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Pearson r:      {pearson_r:.4f}  (p={pearson_p:.6f})")
print(f"Spearman rho:   {spearman_r:.4f}  (p={spearman_p:.6f})")
print(f"R-squared:      {r_value**2:.4f}")
print(f"Slope:          {slope:.2f}")
print(f"Intercept:      {intercept:.2f}")

# Generate regression line values for plotting
x_line = pd.Series([x.min(), x.max()])
y_line = slope * x_line + intercept

# Residuals: difference between actual and predicted values
y_predicted = slope * x + intercept
residuals = y - y_predicted

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle(f"Correlation: {feature_x} vs {feature_y}", fontsize=14)

# Scatter plot with regression line
ax1 = axes[0]
ax1.scatter(x, y, color="steelblue", zorder=5, label="Data points")
ax1.plot(x_line, y_line, color="tomato", linewidth=2,
         label=f"Regression line (r={pearson_r:.2f})")
ax1.set_xlabel(feature_x)
ax1.set_ylabel(feature_y)
ax1.set_title("Scatter plot with regression line")
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.5)

# Residual plot: checks if errors are randomly distributed (good linear fit if so)
ax2 = axes[1]
ax2.scatter(x, residuals, color="steelblue", zorder=5)
ax2.axhline(0, color="tomato", linewidth=2, linestyle="--")
ax2.set_xlabel(feature_x)
ax2.set_ylabel("Residuals")
ax2.set_title("Residual plot")
ax2.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("correlation_plot.png", dpi=150)
plt.show()
