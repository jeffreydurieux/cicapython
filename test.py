# Author: jeffrey durieux
# Email: durieux.jeffrey@gmail.com
# What test script

from sumofsquares import sumofsquares, overall_loss
from sim_one_ica import singlesubica
from split_concatenate import split_concatenate
from randomP import randomP
from groupicas import groupicas
from computeA import computeA
from reestimateP import reestimateP

import numpy as np
from sklearn.decomposition import FastICA





### data
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

### step 1 random P and split data
P = randomP(6, 3)
P
datasplit = split_concatenate(data, P)

### step 2 group ICA and overall loss
[S,A] = groupicas(datasplit, P, nc=2)
overall_loss(data,P,S,A)

### step 3
P
reestimateP(data,S,A,P)

### step convergence criterium
