import pandas as pd 

    # Create a DataFrame from a dictionary
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    # Calculate the sum of each column 
column_sums = df.sum()

print (df)
print ("KH dont care about")
################################################################
    
print(column_sums)

print ("test exam")

print ("more test")

print (r"KH dont care about")


print(df.iloc[[0,1]])  # Accessing all rows in column 'A'


recipe = {
  "Flour": True,
  "Sugar": True,
  "Salt": False
}
series_dict = pd.Series(recipe)

series_dict = pd.Series()

print (series_dict)















