# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:10:11 2020

@author: Andreas Fiehn
"""

import numpy as np

def movingAvg(y):
    
    
    # If array only has a length of one, matrix opereations are not necessary
    if len(y) == 1:
        ysmooth = 3*y[0]/9
        return ysmooth
    
    # Define rows in matrix by slicing y and adding 0's to the end/beginning
    r1 = np.hstack((y[2:],np.array([0,0])))
    r2 = 2*(np.hstack((y[1:],np.array([0]))))
    r3 = 3*(y)
    r4 = 2*(np.hstack((np.array([0]),y[:-1])))
    r5 = np.hstack((np.array([0,0]),y[:-2]))
    
    # Create matrix from the rows
    M = np.vstack((r1,r2,r3,r4,r5))
    
    # Sum the colums in the matrix and divide by 9
    ysmooth = np.sum(M, axis=0)/9
    
    return ysmooth