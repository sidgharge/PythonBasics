import numpy as np


def tanh(z):
    t = (np.exp(z) - np.exp(-z))/(np.exp(z) + np.exp(-z))
    return t


z = np.arange(1, 11)
print(tanh(z))
