import numpy as np

macros = np.array([
    [0.8, 2.9, 3.9],
    [52.4, 23.6, 36.5],
    [55.2, 31.7, 23.9],
    [14.4, 11, 4.9]
])

cal_per_macro = np.array([3, 3, 8])
print(cal_per_macro.shape):w!
result = macros * cal_per_macro

print(result)

