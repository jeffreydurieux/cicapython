# author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
# What group icas

from sumofsquares import sumofsquares
from sim_one_ica import singlesubica
from split_concatenate import split_concatenate, splitarray
from randomP import randomP

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

def groupicas(data, P, nc = 2):
    clusters = np.shape(P)[1]
    dim = np.shape(data[0])[0]
    N = np.shape(P)[0]


    S = np.zeros((clusters, dim, nc))
    A = np.zeros((clusters, N, nc, nc))

    for i in range(clusters):
        ICA = FastICA(n_components = nc)
        ica = ICA.fit_transform(data[i])
        icam = ICA.mixing_
        S[i] = ica


        test = np.split(ICA.mixing_, np.sum(P[:,i]))

        index = P[:,i] == 1
        count = 0
        for j in range(N):


            if index[j] == True:
                A[i,j,:,:] = test[count]
                count += 1
