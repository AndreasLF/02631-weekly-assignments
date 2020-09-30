# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:03:38 2020

@author: Andreas Fiehn
"""

import numpy as np
import pandas as pd

def computeLanguageError(freq):
    # Convert csv to panda
    letterfreq = pd.read_csv("letter_frequencies.csv")
    
    # Convert column names into list. Slice away "Letter" column
    languages  = letterfreq.columns[1:]
        
    # Take the languages (column names). Exclude the first on which is the letter column
    languages = letterfreq.columns[1:]
    
    # Define list to contain the errors
    E = []
    
    # Loop through the languages
    for l in languages:
        # Error for the specific language
        El = 0
        # Loop through each letter frequency
        for (ft,fl) in zip (freq,letterfreq[l]):
            El += (ft - fl)**2
        # Append the language error to the list of errors
        E.append(El)    
    
    return E