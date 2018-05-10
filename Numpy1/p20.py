import math
import numpy as np

# rows = int(input("Enter number of rows: "))

# for row in range(rows):
#     print(' ' * (rows - row - 1), end='')
#
#     num = int(math.pow(11, row))
#
#     string = ' '.join(str(num))
#     print(string)

# la = {}
# for row in range(rows):
#     temp = {0: 1, row: 1}
#
#     for x in range(len(la) - 1):
#         temp[x+1] = la[x] + la[x+1]
#
#     la = temp
#     print(' ' * (rows - row - 1), end='')
#
#     if rows == 0:
#         print(1)
#     else:
#         string = ' '.join(str(x) for x in la.values())
#         print(string)

a1 = np.array([[0, 10, 20],
               [40, 60, 80]])
a2 = np.array([[10, 30, 40], [50, 70, 90]])

a3 = np.array([40, 20, 30])

print(a3.size * a3.itemsize)

x = np.array([[1, 2],
              [3, 4],
              [5, 6]])
x.shape = (2, 3)
print(x.dtype)
x.dtype = 'float64'
print(x.dtype)
print(x)
