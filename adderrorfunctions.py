'''
Author: Jeffrey Durieux
Email: durieux.jeffrey@gmail.com
What: script for adding scaled gaussian noise to a matrix
'''

import numpy as np

def ssequal(E, X):
    
    A = np.square(E)
    A = np.sum(A)
    E = E / np.sqrt(A)
    
    B = np.square(X)
    B = np.sum(B)
    
    Out = E * np.sqrt(B)
    return Out
    
    


def adderror(X, error):
    
    shape = np.shape(X)
    E = np.random.normal(size = shape)
    
    E = ssequal(E, X)
    
    errorlevel = error / (1 - error)
    
    Out = X + (E * np.sqrt(errorlevel))
    
    return Out


