import numpy as np


def diffsigmoid(z):
    sig = 1 / (np.exp(z) * (1 + np.exp(-z) ** 2))
    return sig


z = np.arange(1, 11)
print(diffsigmoid(z))
