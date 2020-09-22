# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:24:25 2020

@author: Andreas Fiehn
"""
import numpy as np

def fermentationRate(measuredRate, lowerBound, upperBound):
    updatedMeasuredRate = measuredRate[(measuredRate < upperBound) & (measuredRate > lowerBound)]

    return np.mean(updatedMeasuredRate)
