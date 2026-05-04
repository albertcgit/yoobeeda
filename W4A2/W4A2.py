# Import libraries for data handling and SQL database
import pandas as pd
import sqlite3

def load_data(filepath):
    # Read the CSV file into a DataFrame
    return pd.read_csv(filepath)

def create_database(df):
    # Connect to an in-memory SQLite database — exists only while the script runs
    conn = sqlite3.connect(":memory:")
    # Load the DataFrame into the database as a table called "happiness"
    df.to_sql("happiness", conn, index=False, if_exists="replace")
    return conn

def query_gdp_categories(conn):
    # Assign a GDP category to each country, then calculate average happiness per category
    # Countries are sorted by category and happiness score from highest to lowest
    query = """
    SELECT
        Country,
        GDP_per_Capita,
        Happiness_Score,
        CASE
            WHEN GDP_per_Capita < 0.90 THEN 'Low'
            WHEN GDP_per_Capita BETWEEN 0.90 AND 1.20 THEN 'Medium'
            ELSE 'High'
        END AS GDP_Category,
        ROUND(
            AVG(Happiness_Score) OVER (
                PARTITION BY
                CASE
                    WHEN GDP_per_Capita < 0.90 THEN 'Low'
                    WHEN GDP_per_Capita BETWEEN 0.90 AND 1.20 THEN 'Medium'
                    ELSE 'High'
                END
            ), 2
        ) AS Avg_Happiness_In_Category
    FROM happiness
    ORDER BY GDP_Category, Happiness_Score DESC;
    """
    # Run the query and return results as a DataFrame
    return pd.read_sql_query(query, conn)

def query_corruption_comparison(conn):
    # Split countries into two groups based on whether corruption score is above or below average
    # Then compute average happiness, GDP, social support, and freedom per group
    query = """
    SELECT
        CASE
            WHEN Perceptions_of_Corruption >= (SELECT AVG(Perceptions_of_Corruption) FROM happiness)
            THEN 'High Corruption Perception'
            ELSE 'Low Corruption Perception'
        END AS Corruption_Group,
        COUNT(*) AS Number_of_Countries,
        ROUND(AVG(Happiness_Score), 2) AS Avg_Happiness,
        ROUND(AVG(GDP_per_Capita), 2) AS Avg_GDP,
        ROUND(AVG(Social_Support), 2) AS Avg_Social_Support,
        ROUND(AVG(Freedom_to_Make_Choices), 2) AS Avg_Freedom
    FROM happiness
    GROUP BY Corruption_Group
    ORDER BY Avg_Happiness DESC;
    """
    # Run the query and return results as a DataFrame
    return pd.read_sql_query(query, conn)

def main():
    df = load_data("world_happiness_dataset.csv")
    conn = create_database(df)

    print("QUERY 1: GDP Categories, Average Happiness, Country Rankings")
    result1 = query_gdp_categories(conn)
    print(result1.to_string(index=False))

    print()
    print("QUERY 2: High vs Low Corruption Comparison using Subquery")
    result2 = query_corruption_comparison(conn)
    print(result2.to_string(index=False))

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()