# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:57:07 2020

@author: Andreas Fiehn
"""
import math
import numpy as np

def boxArea(boxCorners, area):
    bc = boxCorners
    x1,x2,x3,x4 = bc[0],bc[1],bc[2],bc[3]
    y1,y2,y3,y4 = bc[4],bc[5],bc[6],bc[7]
        
    if area == "Box1":
        A = abs(x2-x1)*abs(y2-y1)
    elif area == "Box2":
        A = abs(x4-x3)*abs(y4-y3)
    elif area == "Intersection":
        A = max(0,min(x2,x4)-max(x1,x3))*max(0,min(y2,y4)-max(y1,y3))
    elif area == "Union":
        A1 = abs(x2-x1)*abs(y2-y1)
        A2 = abs(x4-x3)*abs(y4-y3)
        A0 = max(0,min(x2,x4)-max(x1,x3))*max(0,min(y2,y4)-max(y1,y3))
        A = A1 + A2 - A0
    return A