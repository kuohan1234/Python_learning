import pandas as pd 
import numpy as np
import time

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
time.sleep(5)  # import time

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


# can you give me a code to print the DataFrame and Series in a formatted way?
def print_formatted(df, series):
    print("Formatted DataFrame:")
    with pd.option_context('display.float_format', '{:.2f}'.format):
        print(df)
    print("\nFormatted Series:")
    print(series)

print_formatted(df, series_dict)

# 我想 看看 格式化輸出 可以給我一個例子嗎?
# Example of formatted output
print("\nExample of formatted output:")
print_formatted(df, series_dict) 