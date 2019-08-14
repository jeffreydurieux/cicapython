# author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
# what: simulate C-ICA data

import numpy as np
from adderrorfunctions import adderror

n = 10
s = 1000
nc = 4
r = 2
e = 0.001
def simcica(n = 10, s = 1000, nc = 4, r = 2, e = 0.001):
    '''
    This function simulates data according to the c-ica model
    input:  n = number of subjects per cluster
            s = number of rows in component matrix
            nc = number of components per cluster
            r = number of clusters
            e = noise
    '''

    Sr = np.zeros(shape = (r, s, nc))
    Air = np.zeros(shape = (r, n, 100, nc))
    X = np.zeros(shape = (r, n, s, 100))
    XE = np.zeros(shape = (r, n, s, 100))

    for clus in range(r):
        # simulate Sr

        Sr[clus] = np.random.uniform(low = -1.0, high = 1.0,
                size = (s, nc))


        for subjects in range(n):
            #simulate Ai
            Air[clus,subjects, : , :] = np.random.uniform(low = -2.0, high = 2.0,
                                        size = (100, nc))
            # mix S with A
            X[clus, subjects, :, :] = np.dot(Sr[clus], Air[clus, subjects, :, :].T)
            # add error
            XE[clus, subjects, :, :] = adderror(X[clus, subjects, :, :], e)
            np.shape(XE)
    XE = XE.reshape(( n*r, s, 100))


    return {'XE': XE, 'Sr': Sr, 'Air': Air,'X': X}


test = simcica()
type(test)
test.keys()
