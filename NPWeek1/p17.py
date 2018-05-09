import numpy as np

arr = np.random.randint(1, 10, (3, 3, 4))

shape = arr.shape

elements = 1
for i in shape:
    elements *= i

if elements % 2 == 0:
    print(arr.reshape((int((elements / 2)), 2)))

print(arr.reshape((elements, 1)))
