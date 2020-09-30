# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:56:06 2020

@author: Andreas Fiehn
"""

def textToNato(plainText):
    
    # Define alphabet dictionairy
    nato_alphabet = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    

    natoLetters = []
    
    # Loop through characters in string
    for character in plainText:
        natoLetters.append(nato_alphabet.get(character.upper()))
    
    natoText = "-".join(natoLetters)
    
    return natoText

