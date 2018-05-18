import numpy as np
import time

arr1 = np.random.randint(0, 10, (40, 50))
arr2 = np.random.randint(0, 10, (40, 50))

start1 = time.time()
arr3 = np.zeros(arr1.shape, dtype=int)
x = arr3.shape[0]
y = arr3.shape[1]
for row in range(x):
    for col in range(y):
        arr3[row, col] = arr1[row, col] * arr2[row, col]

# print(arr3)
end1 = time.time()
print(end1 - start1)

start2 = time.time()
arr4 = np.multiply(arr1, arr2)
end2 = time.time()
# print(arr4)
print(end2 - start2)

start3 = time.time()
arr4 = [[arr1[j, i] * arr2[j, i] for i in range(y)] for j in range(x)]
# print(arr4)
end3 = time.time()
print(end3 - start3)
