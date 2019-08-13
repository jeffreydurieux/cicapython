# author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
# what compute A hats based on S and X


import numpy as np

def computeA(X, S):

    # Ai = X.T %*% S %*% (S.T %*% S)^-1
    a = np.dot(X.T, S)
    b = np.dot(S.T, S)
    c = np.linalg.inv(b)
    A = np.dot(a, c)
    return A
