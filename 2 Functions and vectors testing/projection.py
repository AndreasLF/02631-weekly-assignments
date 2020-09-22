# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:32:01 2020

@author: Andreas Fiehn
"""

import math
import numpy as np


def computeProjection(a):
    #create an array of ones with the same number of elements as a
    b = np.ones(a.size) 
    
    # Magnitude of vector a is found the numpy's norm function
    a_magnitude = np.linalg.norm(a) 
    
    projection = ((np.dot(a,b)) / (a_magnitude**2))*a
    return projection

