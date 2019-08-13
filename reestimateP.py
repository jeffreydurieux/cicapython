# author jeffrey durieux
# email durieux.jeffrey@gmail.com
# What: function for computing reconstructed data

from sumofsquares import sumofsquares
from sim_one_ica import singlesubica
from split_concatenate import split_concatenate
from randomP import randomP
from groupicas import groupicas
from computeA import computeA

import numpy as np
from sklearn.decomposition import FastICA

'''
P = randomP(6, 3)
P

data = singlesubica()
x1 = data['Xe']
data = singlesubica()
x2 = data['Xe']
data = singlesubica()
x3 = data['Xe']
data = singlesubica()
x4 = data['Xe']
data = singlesubica()
x5 = data['Xe']
data = singlesubica()
x6 = data['Xe']


data = np.stack([x1,x2,x3,x4,x5,x6])
np.shape(data)

datasplit = split_concatenate(data, P)

nc = 2

[S,A] = groupicas(datasplit, P, nc=2)
reestimateP(data,S,A,P)

'''

import numpy as np

def reestimateP(data, S, A, P):
    '''
    This function updates the P matrix
    Input:  data = original datasets
            S = ica estimated components
            A =

    '''
    shape = np.shape(P)
    #M = np.shape(S)[1]
    N = np.shape(A)

    Ahats = np.zeros(shape = (shape[0], shape[1], N[1], N[2]))
    #Xhats = np.zeros(shape = (shape[0], shape[1], M, N[1]))
    Lir = np.zeros(shape = shape)
    newP = np.zeros(shape = shape, dtype=int)

    for i in range(shape[0]):

        for j in range(shape[1]):
            A = computeA(data[i], S[j])
            Ahats[i, j, :, :] = A

            Xhat = np.dot(S[j], A.T)

            Loss = np.sum( np.power( (data[i] - Xhat), 2) )
            Lir[i,j] = Loss

    nP = np.argmin(Lir, axis = 1)
    for p in range(shape[0]):
        newP[p, nP[p]] = 1

    return newP
