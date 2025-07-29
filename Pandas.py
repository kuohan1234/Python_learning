import pandas as pd 

# --- DataFrame Creation and Basic Operations ---

# Create a DataFrame from a dictionary
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print("Original DataFrame:")
print(df)

# Calculate the sum of each column
column_sums = df.sum()
print("\nSum of each column:")
print(column_sums)

# --- DataFrame Slicing ---

# Access specific rows by their integer location using iloc
# This selects the rows at index 0 and 1
print("\nSlicing rows at index 0 and 1:")
print(df.iloc[[0, 1]])


# --- Series Creation ---

# Create a Series from a dictionary
recipe = {
  "Flour": True,
  "Sugar": True,
  "Salt": False
}
series_dict = pd.Series(recipe)
print("\nSeries created from a dictionary:")
print(series_dict)
