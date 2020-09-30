# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:19:35 2020

@author: Andreas Fiehn
"""

def letterFrequency(filename):
    
    # Get the lines from the file
    lines = open(filename,"r").readlines()
    # Join lines into a string
    text = "".join(lines)
    
    # Make text lowercase
    text = text.lower()
    
    # Letters to seacrh for 
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # List to contain letter count
    letter_count = []
    s = 0
    
    # Loop through each letter
    for l in letters: 
        # Count the letter
        c = text.count(l)
        
        # Append the count to the list
        letter_count.append(c)
        
        # Add the count to the sum
        s += text.count(l)
        
    # Frequency list
    freq = []
    
    # Loop through the letter count
    for n in letter_count:
        
        # Calculate frequency
        freq.append((n/s)*100)
    
    return freq

