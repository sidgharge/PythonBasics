import numpy as np
import time
import math

arr1 = np.random.randint(1, 10, (40, 50))
arr2 = np.random.randint(1, 10, (40, 50))

start1 = time.time()
arr3 = np.zeros(arr1.shape, dtype=float)
x = arr3.shape[0]
y = arr3.shape[1]
for row in range(x):
    for col in range(y):
        arr3[row, col] = math.log(arr1[row, col])
end1 = time.time()
# print(arr3)
print(end1 - start1)

start2 = time.time()
arr4 = np.log(arr1)
end2 = time.time()
# print(arr4)
print(end2 - start2)
