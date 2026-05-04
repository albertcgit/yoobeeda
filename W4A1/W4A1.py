# Import libraries for data handling, visualization, and file management
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

def load_data(filepath):
    # Read the CSV file into a DataFrame
    return pd.read_csv(filepath)

def clean_data(df):
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Get all numeric columns for cleaning
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    # Drop rows where every numeric value is missing
    df.dropna(how="all", subset=numeric_cols, inplace=True)

    # Remove outliers using the IQR method for each numeric column
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        # Keep only rows within the acceptable range
        df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

    # Reset index after rows have been removed
    df.reset_index(drop=True, inplace=True)
    return df

def plot_happiness_by_country(df):
    # Sort countries by happiness score for better readability
    df_sorted = df.sort_values("Happiness_Score", ascending=True)
    fig, ax = plt.subplots(figsize=(10, 7))
    # Plot horizontal bars for each country
    ax.barh(df_sorted["Country"], df_sorted["Happiness_Score"], color="steelblue")
    ax.set_xlabel("Happiness Score")
    ax.set_title("Happiness Score by Country")
    plt.tight_layout()
    plt.savefig("output/01_happiness_by_country.png", dpi=150)
    plt.close()

def plot_correlation_heatmap(df):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    fig, ax = plt.subplots(figsize=(9, 7))
    # Compute pairwise correlation between all numeric columns
    corr = df[numeric_cols].corr()
    # Plot heatmap with correlation values annotated
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("output/02_correlation_heatmap.png", dpi=150)
    plt.close()

def plot_boxplots(df):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    # Create a 2x3 grid of subplots, one per numeric feature
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()
    for i, col in enumerate(numeric_cols[:6]):
        # Draw box plot showing spread, median, and any outlier points
        axes[i].boxplot(df[col].dropna())
        axes[i].set_title(col.replace("_", " "))
    fig.suptitle("Distribution of Features (Box Plots)")
    plt.tight_layout()
    plt.savefig("output/03_boxplots.png", dpi=150)
    plt.close()

def plot_scatter_factors(df):
    # Select key factors to compare against happiness score
    factors = ["GDP_per_Capita", "Social_Support", "Freedom_to_Make_Choices", "Perceptions_of_Corruption"]
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    for ax, col in zip(axes.flatten(), factors):
        # Plot each country as a point
        ax.scatter(df[col], df["Happiness_Score"], color="steelblue")
        # Calculate and draw a linear trend line
        m, b = np.polyfit(df[col], df["Happiness_Score"], 1)
        x_line = np.linspace(df[col].min(), df[col].max(), 100)
        ax.plot(x_line, m * x_line + b, color="red", linestyle="--")
        # Show Pearson correlation coefficient in the title
        r = df[col].corr(df["Happiness_Score"])
        ax.set_title(f"{col.replace('_', ' ')} (r={r:.2f})")
        ax.set_xlabel(col.replace("_", " "))
        ax.set_ylabel("Happiness Score")
    fig.suptitle("Key Factors vs Happiness Score")
    plt.tight_layout()
    plt.savefig("output/04_scatter_factors.png", dpi=150)
    plt.close()

def plot_stacked_contributions(df):
    factors_stack = ["GDP_per_Capita", "Social_Support", "Freedom_to_Make_Choices",
                     "Generosity", "Perceptions_of_Corruption"]
    # Isolate the selected factor columns with Country as index
    df_stack = df.set_index("Country")[factors_stack]
    # Normalise each row so all factors sum to 1 (proportional share)
    df_norm = df_stack.div(df_stack.sum(axis=1), axis=0)
    # Order countries from highest to lowest happiness score
    df_norm = df_norm.reindex(df.sort_values("Happiness_Score", ascending=False)["Country"])
    fig, ax = plt.subplots(figsize=(12, 7))
    bottom = np.zeros(len(df_norm))
    # Stack each factor on top of the previous one
    for col in factors_stack:
        ax.bar(df_norm.index, df_norm[col], bottom=bottom, label=col.replace("_", " "))
        bottom += df_norm[col].values
    ax.set_ylabel("Proportional Share")
    ax.set_title("Relative Factor Contributions per Country")
    # Format y-axis as percentage
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_xticks(range(len(df_norm.index)))
    ax.set_xticklabels(df_norm.index, rotation=40, ha="right")
    ax.legend(loc="upper right", fontsize=8)
    plt.tight_layout()
    plt.savefig("output/05_stacked_contributions.png", dpi=150)
    plt.close()

def plot_happiness_distribution(df):
    fig, ax = plt.subplots(figsize=(9, 5))
    # Plot frequency distribution of happiness scores
    ax.hist(df["Happiness_Score"], bins=8, color="steelblue", edgecolor="white")
    # Add vertical lines for mean and median
    ax.axvline(df["Happiness_Score"].mean(), color="red", linestyle="--",
               label=f"Mean {df['Happiness_Score'].mean():.2f}")
    ax.axvline(df["Happiness_Score"].median(), color="green", linestyle=":",
               label=f"Median {df['Happiness_Score'].median():.2f}")
    ax.set_xlabel("Happiness Score")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Happiness Scores")
    ax.legend()
    plt.tight_layout()
    plt.savefig("output/06_happiness_distribution.png", dpi=150)
    plt.close()

def main():
    # Create output folder if it does not exist
    os.makedirs("output", exist_ok=True)

    # Load, clean, and save the dataset
    df = load_data("world_happiness_dataset.csv")
    df = clean_data(df)

    # Generate all visualizations
    plot_happiness_by_country(df)
    plot_correlation_heatmap(df)
    plot_boxplots(df)
    plot_scatter_factors(df)
    plot_stacked_contributions(df)
    plot_happiness_distribution(df)

    print("All charts saved to output/")

if __name__ == "__main__":
    main()