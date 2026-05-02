import pandas as pd
import matplotlib.pyplot as plt


def load_and_clean(filepath):
    df = pd.read_csv(filepath)

    # Replace text-encoded numbers with actual numeric values
    df["Age"]    = df["Age"].replace({"thirty-eight": 38})
    df["Salary"] = df["Salary"].replace({"sixty five thousand": 65000})

    # Convert to numeric; unparseable values become NaN
    df["Age"]    = pd.to_numeric(df["Age"],    errors="coerce")
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

    # Standardise inconsistent country codes
    df["Country"] = df["Country"].replace({"AU": "AUS"})

    # Parse dates; invalid dates (e.g. month=13) become NaT
    df["Join Date"] = pd.to_datetime(df["Join Date"], dayfirst=True, errors="coerce")

    # Remove fully duplicate rows
    df = df.drop_duplicates()

    # Merge Bob's two rows (same ID, complementary missing data) into one complete row
    duplicate_ids = df["ID"].dropna()[df["ID"].dropna().duplicated()].unique()
    merged = df[df["ID"].isin(duplicate_ids)].groupby("ID", as_index=False).apply(
        lambda g: g.ffill().bfill().iloc[0]
    ).reset_index(drop=True)
    df = pd.concat([df[~df["ID"].isin(duplicate_ids)], merged]).reset_index(drop=True)

    # Fill missing text columns with visible placeholders
    df["Name"]    = df["Name"].fillna("Unknown")
    df["Country"] = df["Country"].fillna("Unknown")

    # Sort by ID, NaN (Eve) goes to the bottom
    df = df.sort_values("ID", na_position="last").reset_index(drop=True)

    return df


def plot_outliers(df):
    # Boxplots visually show the spread and flag extreme values as individual dots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle("Outlier Detection via Boxplots")

    for ax, col in zip(axes, ["Age", "Salary"]):
        # Drop NaN before plotting so missing values don't break the chart
        ax.boxplot(df[col].dropna(), patch_artist=True,
                   boxprops=dict(facecolor="lightblue"),
                   flierprops=dict(marker="o", color="red", markersize=7))
        ax.set_title(col)
        ax.set_ylabel(col)
        ax.set_xticks([])

    plt.tight_layout()
    plt.savefig("boxplots.png", dpi=150)
    plt.show()


def plot_correlation_heatmap(df):
    # Label encode Country: NZ=0, AUS=1 — required for Pearson which only works on numbers
    df["Country_encoded"] = df["Country"].map({"NZ": 0, "AUS": 1})

    # Calculate tenure in years from Join Date to today
    df["Company Tenure"] = (pd.Timestamp("today") - df["Join Date"]).dt.days / 365.25

    # Pearson correlation on all numeric features of interest
    corr = df[["Age", "Salary", "Country_encoded", "Company Tenure"]].corr(method="pearson")

    # Rename for display clarity
    corr.index   = ["Age", "Salary", "Country", "Company Tenure"]
    corr.columns = ["Age", "Salary", "Country", "Company Tenure"]

    print("PEARSON CORRELATION MATRIX")
    print(corr)

    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)

    # Annotate each cell with the correlation value
    for i in range(len(corr)):
        for j in range(len(corr)):
            val = corr.values[i, j]
            if not pd.isna(val):
                ax.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=11)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)
    plt.colorbar(im, ax=ax)
    plt.title("Pearson Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    df = load_and_clean("messy_dataset_Mukesh.csv")

    print("CLEANED DATA")
    print(df.to_string())
    print()

    # Save cleaned dataset to a new CSV file
    df.to_csv("messy_dataset_Mukesh_cleaned.csv", index=False)
    print("Cleaned data saved to messy_dataset_Mukesh_cleaned.csv")

    plot_outliers(df)
    plot_correlation_heatmap(df)