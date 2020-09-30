# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:45:04 2020

@author: Andreas Fiehn
"""
import numpy as np

def computeItemCost(resourceItemMatrix,resourceCost):
    # Dot the matrix and the vector
    itemCost = np.dot(resourceCost, resourceItemMatrix)
    return itemCost
