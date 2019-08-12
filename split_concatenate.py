#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:53:04 2019

@author: jeffreydurieux
email: durieux.jeffrey@gmail.com
What: two functions:
1) split and concatenate based on P
2) splitarray

1) ################################################
Function that concatenates data based on P matrix

import numpy as np


from randomP import randomP
P = randomP(4,2)

A = np.array([[1,1],
             [1,1]])
B = np.array([[2,2],
             [2,2]])
C = np.array([[3,3],
             [3,3]])
D = np.array([[4,4],
             [4,4]])


data = np.stack([A,B,C,D])

2) ################################################
split_concatenate(data, P)[1]

# What: function for computing sum of squares over single array of multiple
# numpy arrays.
# note that this is just a simple wrapper function
# example: x = np.arange(1000).reshape((10,10,10))
#  sumofsquares(x)

"""


import numpy as np

def split_concatenate(array, P):
    '''
    This functions splits a 3d array based on a boolean partioning matrix P.
    returns a list (K elements) of np.arrays (Voxel X Time)
    '''

    shape = np.shape(P)

    result = []

    for cluster in range(shape[1]):
        index = P[:,cluster] == 1
        result.append( np.concatenate( array[index], axis = 1) )

    return result

def splitarray(array, originalcols):
    '''
    This functions splits an array into equal parts based on ncols
    input: numpy array and number of subjects in array
    output: list of numpy arrays
    '''
    return np.split(array, subjects)
