import numpy as np

print(np.__version__)

python_list = [12.23, 13.32, 100, 36.32]

a = np.array(python_list)

print(a)

a = np.arange(2, 11).reshape(3, 3)

print(a)

a = np.zeros(10, dtype=float)
a[6] = 11
print(a)

a = np.arange(12, 38)
print(a)

np.asfarray(a, float)

print(a)

