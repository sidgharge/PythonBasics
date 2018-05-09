import numpy as np
import time
import pickle

arr1 = np.random.randint(0, 100, (4, 10))
print('Array1: ', arr1)

arr2 = np.random.randint(0, 100, (10, 3))
print('Array2: ', arr2)

x = arr1.shape[0]
y = arr2.shape[1]

tup = (x, y)

arr3 = np.zeros(tup)

start1 = time.time()
for row in range(x):
    s = 0
    for col in range(y):
        rowx = arr1[row]
        coly = arr2[:, col]
        for i in range(len(rowx)):
            s = s + rowx[i] * coly[i]
        arr3[row, col] = s
        s = 0
end1 = time.time()
print(arr3)
print('time taken: ', end1 - start1)

start2 = time.time()
arr4 = np.matmul(arr1, arr2)
end2 = time.time()
print(arr4)
print('time taken: ', end2 - start2)

np.savetxt('nparray.txt', arr4)

