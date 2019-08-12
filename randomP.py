# Author: jeffrey durieux
# email: durieux.jeffrey@gmail.com
# What: function to generate a random Partitioning matrix


import numpy as np
from numpy import random


def randomP(nsubjects, nclusters):

    P = np.zeros(shape = (nsubjects, nclusters), dtype = int)

    p = random.choice(a = range(1, nclusters + 1), size = nsubjects, p=None)

    check = False
    while check == False:
        set = np.unique(p)
        if len(set) == nclusters:
            check = True
        else:
            p = random.choice(a = range(1, nclusters + 1), size = nsubjects,
            p=None)

    for i in range(nsubjects):
        P[i, p[i] - 1] = 1

    return P



nsubjects = 10
nclusters = 3

randomP(5, 3)
