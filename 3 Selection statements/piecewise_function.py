# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:38:59 2020

@author: Andreas Fiehn
"""

def gravitationalPull(x):
    g0 = 9.82
    R = 6.371e6
    
    if R <= x:    
        g_distance = g0 * ((R**2)/(x**2))
    elif R > x or x >= 0:
        g_distance = g0 * (x/R)
    else: 
        g_distance = False
    return g_distance

