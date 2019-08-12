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

# group icas
ICA = FastICA(n_components=2)
S1 = ICA.fit_transform(X1)  # Reconstruct signals
A1 = ICA.mixing_  # Get estimated mixing matrix
np.shape(A1)

S2 = ICA.fit_transform(X2)  # Reconstruct signals
A2 = ICA.mixing_  # Get estimated mixing matrix
np.shape(A2)

type(A1)
type(A2)

A1
np.shape(np.split(A1, 1))

A2
test = np.split(A2, 5)


#### make code to reconstruct data Xhat = S %*% A.T
P
