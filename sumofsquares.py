# Author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
#
# What: 2 functions: sumofsquares and reallocate P
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
