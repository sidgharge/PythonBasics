import numpy as np

arr = np.random.randint(1, 100, (64, 64, 64))

arr2 = arr.flatten()

print(arr2.shape)
