# Author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
# What: function for computing sum of squares over single array of multiple
# numpy arrays.
# note that this is just a simple wrapper function
# example: x = np.arange(1000).reshape((10,10,10))
#  sumofsquares(x)


import numpy as np

def sumofsquares(arrays):
    result = np.sum(np.power(arrays, 2))
    return result
