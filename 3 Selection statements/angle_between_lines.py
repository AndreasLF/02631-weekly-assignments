# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:08:59 2020

@author: Andreas Fiehn
"""

import math
import numpy as np



def acuteAngle(v1,v2):
     # returns False if either of the vectors are [0,0] since it would not have a direction
    if (np.array_equal(v1,np.array([0,0]))) or (np.array_equal(v2,np.array([0,0]))):
        return False
    
    # calculate unit vectors
    v1_unit = v1 / np.linalg.norm(v1)
    v2_unit = v2 / np.linalg.norm(v2)
    
    theta = np.arccos(np.dot(v1_unit,v2_unit)) 
    
    if theta > (math.pi/2):
        theta = math.pi - theta
    return theta