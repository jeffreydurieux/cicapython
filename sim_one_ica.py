'''
Author: Jeffrey Durieux
Email: durieux.jeffrey@gmail.com
What: script for simulating ICA data

'''

import numpy as np
from adderrorfunctions import adderror


def singlesubica(samples = 1000, ncomp = 2, error = 0.0):
    '''
    This function simulates ica data for one subject
    The signals S are drawn from a uniform distribution
    output is a dict
    '''
    S = np.random.uniform(low = -1.0, high = 1.0, size = (samples, ncomp))
    A = np.random.uniform(low = -2.0, high = 2.0, size = (ncomp, ncomp ))
    X = np.dot(a = S, b = A.T)
    Xe = adderror(X, error)
    
    return {'Xe': Xe, 'S': S, 'A': A,'X': X}




