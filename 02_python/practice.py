# -*- coding: utf-8 -*-
"""
A template for performing data analysis using the pandas library.

This script covers the standard workflow:
1.  Importing libraries
2.  Loading data
3.  Exploratory Data Analysis (EDA)
4.  Data Cleaning and Preprocessing
5.  Data Analysis and Aggregation
6.  Data Visualization
7.  Exporting Results
"""

# 1. Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set some display options for pandas
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 100)

# 2. Loading Data
# It's common to load data from a CSV file.
# Replace 'your_dataset.csv' with the path to your file.
try:
    df = pd.read_csv('your_dataset.csv')
except FileNotFoundError:
    print("Data file not found. Using a sample DataFrame for demonstration.")
    # Create a sample DataFrame if the CSV is not available
    data = {
        'product_id': [101, 102, 103, 104, 105, 102, 106],
        'category': ['Electronics', 'Apparel', 'Electronics', 'Home Goods', 'Apparel', 'Apparel', None],
        'price': [599.99, 49.99, 129.95, 24.50, 89.99, 49.99, 15.00],
        'rating': [4.5, 4.0, 4.2, 3.8, 4.5, 4.0, np.nan],
        'sales_date': pd.to_datetime(['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-16', '2023-01-20'])
    }
    df = pd.DataFrame(data)

# 3. Exploratory Data Analysis (EDA)
print("--- Initial Data Exploration ---")
# View the first 5 rows
print("First 5 rows of the data:\n", df.head())

# View the last 5 rows
# print("Last 5 rows of the data:\n", df.tail())

# Get a concise summary of the dataframe
print("\nDataFrame Info:")
df.info()

# Get descriptive statistics for numerical columns
print("\nDescriptive Statistics:\n", df.describe())

# Get the dimensions of the DataFrame (rows, columns)
print("\nDataFrame Shape:", df.shape)

# 4. Data Cleaning and Preprocessing
print("\n--- Data Cleaning and Preprocessing ---")
# Check for missing values
print("Missing values per column:\n", df.isnull().sum())

# --- Strategies for handling missing values ---
# Option A: Drop rows with any missing values (use with caution)
# df_cleaned = df.dropna()

# Option B: Fill missing values with a specific value (e.g., mean, median, mode)
df['rating'] = df['rating'].fillna(df['rating'].median())
df['category'] = df['category'].fillna('Unknown')

# Check for and handle duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Correct data types if necessary (e.g., converting object to category)
df['category'] = df['category'].astype('category')

print("\nDataFrame Info after cleaning:")
df.info()

# 5. Data Analysis and Aggregation
print("\n--- Data Analysis and Aggregation ---")
# Group by a column and calculate aggregate statistics
category_analysis = df.groupby('category')['price'].agg(['mean', 'count', 'sum']).round(2)
print("Analysis by Category:\n", category_analysis)

# Filtering data based on a condition
high_rated_products = df[df['rating'] > 4.0]
print("\nHigh-rated products:\n", high_rated_products)

# Creating a new column (Feature Engineering)
df['price_per_rating_point'] = df['price'] / df['rating']

# 6. Data Visualization
print("\n--- Generating Visualizations ---")
# Set plot style
sns.set_style("whitegrid")

# Histogram of prices
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], bins=15, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Bar chart of category counts
plt.figure(figsize=(8, 5))
sns.countplot(y=df['category'])
plt.title('Number of Products per Category')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()

# 7. Exporting Results
# Save the cleaned and processed DataFrame to a new CSV file
df.to_csv('cleaned_dataset.csv', index=False)
print("\nCleaned data has been saved to 'cleaned_dataset.csv'")

