import numpy as np


def sigmoid(z):
    sig = 1 / (1 + np.exp(-z))
    return sig


z = np.arange(1, 11)
print(sigmoid(z))
