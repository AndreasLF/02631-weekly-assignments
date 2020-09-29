# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:51:54 2020

@author: Andreas Fiehn
"""

import numpy as np

def circleAreaMC(xvals,yvals):
    
    # Number of points inside circle
    n = 0
    
    # Number of total points 
    N = 0
    
    #  Area of square
    A_square = 4
    
    # Loop through xvals and yvals simultaneously
    for (x, y) in zip(xvals, yvals):
        # Create a vector from the coordinates
        vector = np.array([x,y])
        # Calculate vector magnitude 
        m = np.linalg.norm(vector)
        
        # Check i the point is inside circle by checking if length is less than one
        if m < 1:
            # Add one to number of points inside circle
            n += 1 
        # Add one to number of total points
        N += 1
        
    # Calculate estimated area
    A_circ = A_square*(n/N)
    return A_circ
