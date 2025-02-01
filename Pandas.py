import pandas as pd 

    # Create a DataFrame from a dictionary
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    # Calculate the sum of each column 
column_sums = df.sum()

################################################################
    
print(column_sums)