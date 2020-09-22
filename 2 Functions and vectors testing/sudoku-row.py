# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:21:31 2020

@author: Andreas Fiehn
"""
import numpy as np

def fillSudokuRow(x):
    
    # Checks if the number from 1 to 9 is in the sudoku row. If it's no the value will be false 
    numbers_in_array = np.isin([1,2,3,4,5,6,7,8,9],x)
    
    # Finds the index of the number not in the sudoku row. 
    # One is added to get the correct number: Index starts at 0 
    number_missing = np.where(numbers_in_array == False)[0] + 1   
    
    # 0 is replaced with the missing number
    x[np.where(x == 0)] = number_missing
    return x

