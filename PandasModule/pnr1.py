import numpy as np

x = np.random.uniform(1, 12, 5)
val = 3
print(x)
print(x.flat[np.abs(x - val).argmin()])
