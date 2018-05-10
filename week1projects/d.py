import numpy as np
import pandas

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# pandas.DataFrame(arr).to_excel('pandasarray.xlsx')

try:
    arr = pandas.read_excel('pandasarray.xlsx').values
except FileNotFoundError:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    pandas.DataFrame(arr).to_excel('pandasarray.xlsx')

print(arr)
