import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    a = np.asarray(x)
    b = 1 + np.exp(-a)
    c = np.reciprocal(b)
    return c