# Author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
#
# What: 2 functions: sumofsquares and overall loss
#


# 1) ###############################################
#function for computing sum of squares over single array of multiple
# numpy arrays.
# note that this is just a simple wrapper function
# example: x = np.arange(1000).reshape((10,10,10))
#  sumofsquares(x)
#
# 2) ###############################################

import numpy as np

def sumofsquares(arrays):
    '''
    Computes the SSQ of array(s)
    '''
    result = np.sum(np.power(arrays, 2))
    return result


def overall_loss(data, P, S, A):
    '''
    This function computes the overall loss function of the C-ICA model
    '''
    shape = np.shape(P)
    Loss = np.zeros(shape = shape[0] )
    for i in range(shape[0]):
        idx = np.where(P[i] == 1)
        idx
        Xhat = np.dot(S[idx], A[i].T)
        Loss[i] = np.sum( np.power( (data[i]) - Xhat, 2) )
    return np.sum(Loss)
