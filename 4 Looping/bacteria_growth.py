# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:54:51 2020

@author: Andreas Fiehn
"""

def bacteriaGrowth(n0, alpha, K, N):
    t = 0
    n = n0
    while(n < N):
        n = ((1+alpha*(1-n/K))*n)
        t += 1
    
    return t

