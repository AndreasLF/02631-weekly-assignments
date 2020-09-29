# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:18:59 2020

@author: Andreas Fiehn
"""
import numpy as np

def thermoEquilibrium(N, r):
    
    t = 0 
    NL = N
    NR = 0
    
    #  Loop as long as NL and NR are not the same
    # I expect r to contain enough numbers to not end up in an infinite loop
    while NL != NR: 
        # Calculate pLR
        pLR = NL/N
    
        # Return false if r does not contain sufficient values 
        if(t == len(r)):
             return 0
         
        # Decide wether a particle goes left or right
        if r[t] < pLR:
            NL -= 1
            NR += + 1 
        else: 
            NL += 1
            NR -= 1 
        # Increment time
        t += 1
    return t