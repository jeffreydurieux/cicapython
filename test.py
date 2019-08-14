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
from sim_cica import simcica
import numpy as np
from sklearn.decomposition import FastICA





datadict = simcica()
datadict.keys()

data = datadict['XE']

### step 1 random P and split data
P = randomP(20, 2)
P

datasplit = split_concatenate(data, P)

### step 2 group ICA and overall loss
[S,A] = groupicas(datasplit, P, nc=4)
overall_loss(data,P,S,A)

### step 3

P = reestimateP(data,S,A,P)
P

### step convergence criterium

2591015.204506336
1703013.6584665347

1652595.6264669758
1610834.5930968456
1563851.6850565504
  10667.21707994243
  10667.21707994243



np.shape(S)

from correlations import correlations

oriS = datadict['Sr']
oriS1 = oriS[0]
oriS2 = oriS[1]

np.shape(oriS)

np.shape(S)

shat1 = S[0]
shat2 = S[1]

P
correlations(oriS1, shat1)
correlations(oriS2, shat2)
