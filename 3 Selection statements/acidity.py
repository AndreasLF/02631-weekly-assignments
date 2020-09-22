# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:52:11 2020

@author: Andreas Fiehn
"""

def pH2Category(pH):
    if pH >= 0 and pH < 3:
        c = "Strongly acidic"
    elif pH >= 3 and pH < 6:
        c = "Weakly acidic"
    elif pH >= 6 and pH <= 8:
        c = "Neutral"
    elif pH > 8 and pH <= 11:
        c = "Weakly basic"
    elif pH > 11 and pH <= 14:
        c = "Strongly basic"
    else:
        c = "pH out of range"
    return c

