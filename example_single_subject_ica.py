#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:04:30 2019

@author: jeffreydurieux
@email: durieux.jeffrey@gmail.com
"""


from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

from sim_one_ica import singlesubica 
from correlations import correlations

icadata = singlesubica(samples=1500, ncomp = 2)


Xe = icadata['Xe']

# initialize fastica
ica = FastICA(n_components=2)

# get reconstructed signals
Shat = ica.fit_transform(Xe)
Ahat = ica.mixing_



plt.scatter(Shat[:,0], Shat[:,1])
correlations(icadata['S'], Shat)

plt.scatter(Xe[:,0], Xe[:,1])