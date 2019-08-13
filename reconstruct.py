# author jeffrey durieux
# email durieux.jeffrey@gmail.com
# What: function for computing reconstructed data

from sumofsquares import sumofsquares
from sim_one_ica import singlesubica
from split_concatenate import split_concatenate
from randomP import randomP
from groupicas import groupicas

import numpy as np
from sklearn.decomposition import FastICA


P = randomP(6, 2)
P

data = singlesubica()
x1 = data['Xe']
x2 = data['Xe']
x3 = data['Xe']
data = singlesubica()
x4 = data['Xe']
x5 = data['Xe']
x6 = data['Xe']

data = np.stack([x1,x2,x3,x4,x5,x6])
np.shape(data)

data = split_concatenate(data, P)

X1 = data[0]
X2 = data[1]
np.shape(X1)
np.shape(X2)

nc = 2

[S,A] = groupicas(data, P, nc=2)
A
import numpy as np

def reconstruct(data, S, A, P):
    shape = np.shape(P)

    # sum A over arrays
    At = np.sum(A, axis=0)


    Xhat = np.zeros(shape)

    for i in range(shape[0]):
        np.shape(S)











test = np.arange((3*4*3)).reshape((3,4,3))
test
np.sum(test,0)

A
At
