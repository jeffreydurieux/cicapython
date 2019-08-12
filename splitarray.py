# Author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
# what: function that splits a numpy array into equal parts
# Note that this is just a simple wrapper function of np.hsplit
# x = np.arange(1000).reshape(20, 50)
# np.shape(x)
# np.shape(splitarray(x, 5))


import numpy as np

def splitarray(array, originalcols):
    '''
    This functions splits an array into equal parts based on ncols
    input: numpy array and number of colums (originalcols)
    output: list of numpy arrays
    '''
    return np.hsplit(array, originalcols)
