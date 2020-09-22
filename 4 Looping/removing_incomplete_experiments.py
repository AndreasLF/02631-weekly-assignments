# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:02:51 2020

@author: Andreas Fiehn
"""

import numpy as np

def removeIncomplete(id):
    # removes decimal by converting to int
    idInt = id.astype(int)
    
    # Numbers are counted and ordered 
    (number, count) = np.unique(idInt,return_counts = True)
    # A dict containing the numbers and the count is created
    numberCount = dict(zip(number,count))
    
    # List of indexes to remove
    indexesToRemove = []
    
    # Loops through the dict where k is the key and n is the value
    for k,n in numberCount.items():
        if n < 3:
            # The indices for the numbers present less than 3 times are added to the list
            # np.where puts the array inside a tuple, hence the [0]
            indexesToRemove += np.where(idInt == k)[0].tolist()
            # np.append(indexesToRemove, np.array([4,2]),axis=0)
    
    idComplete = np.delete(id,indexesToRemove)
    
    return idComplete


