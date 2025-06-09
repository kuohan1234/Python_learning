import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,np.nan,6,7])

#print(s)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

#print(df2.dtypes)
#print(df2.head(3))
#print(df2.to_numpy())

arr1= np.array([0,10,20,40,60])
print("Array1: ", arr1)
arr2= np.array([0,40])
print("Array2: ", arr2)
print("Compare each element of array1 and array2")
print("Output: ", np.in1d(arr1,arr2))