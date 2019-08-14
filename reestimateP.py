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

### print suppress scientific notation
np.set_printoptions(suppress=True)

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
            A = mixing matrices
    Output: new estimated P matrix

    '''
    shape = np.shape(P)
    N = np.shape(A)

    Ahats = np.zeros(shape = (shape[0], shape[1], N[1], N[2]))
    Lir = np.zeros(shape = shape)
    newP = np.zeros(shape = shape, dtype=int)

    # outer for loop per subject
    # then inner loop per cluster
    # compute Xhat based on computing Ai with different S matrix
    # compute loss function ||Xi - Xhat||2
    # put in NxC loss matrix
    # compute new P matrix by checking minimal loss per subject
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

    newP
    newP[5,2]=0

    # check for empty clusters
    # use while loop for check multiple empty clusters
    emcluscount = np.sum(newP, axis = 0)
    flag = any(emcluscount == 0)

    # add flag iteration and warning if this code does not work
    # just to escape the while loop

    flagiter = 0
    while flag == True:
        flagiter += 1
        #index of empty clusters
        emptycluster = emcluscount == 0

        # get loss function values
        minn = np.zeros(shape=(shape[0]))

        for n in range(shape[0]):
            minn[n] = Lir[n, nP[n]]

        # get top loss values indices to swap
        idtoswap = minn.argsort()[-np.sum(emptycluster):][::-1]

        for swap in range(np.sum(emptycluster)):
            # put old 1 to 0
            oldone = newP[idtoswap[swap],:] == 1
            newP[idtoswap[swap],oldone] = 0
            # put emtpy clus to 1
            idemp = np.where(emptycluster)[0]
            replaceid = np.random.choice(idemp,1)
            newP[idtoswap[swap], replaceid] = 1

        emcluscount = np.sum(newP, axis = 0)
        flag = any(emcluscount == 0)
        if flagiter == 30:
            flag = False

    return newP
