import numpy as np
import time


def mul_mat(arr1, arr2):
    x = arr1.shape[0]
    y = arr2.shape[1]

    tup = (x, y)

    arr3 = np.zeros(tup)

    for row in range(x):
        s = 0
        for col in range(y):
            rowx = arr1[row]
            coly = arr2[:, col]
            for i in range(len(rowx)):
                s = s + rowx[i] * coly[i]
            arr3[row, col] = s
            s = 0
    return arr3


x = np.random.randint(0, 100, (12000, 50))
w = np.random.randint(0, 100, (50, 40))

start1 = time.time()
arr3 = mul_mat(x, w)
end1 = time.time()
print(end1 - start1)

start2 = time.time()
arr4 = np.matmul(x, w)
end2 = time.time()
print(end2 - start2)
