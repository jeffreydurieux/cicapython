#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:20:41 2019

@author: jeffreydurieux
@email: j.durieux@fsw.leidenuniv.nl
what: compute correlations between columns of two matrices

"""

import numpy as np

def correlations(X, Y):
    '''
    This function computes the pearson correlations between the columns of
    two matrices
    input: two numpy MxN arrays
    output: a NxN matrix with correlations
    '''
    X = (X - X.mean(axis=0)) / X.std(axis=0)
    Y = (Y - Y.mean(axis=0)) / Y.std(axis=0)
    pearson_r = np.dot(X.T, Y) / X.shape[0]
    
    return(pearson_r)
    
    
