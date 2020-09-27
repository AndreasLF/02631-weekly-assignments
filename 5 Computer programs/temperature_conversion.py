# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:25:30 2020

@author: Andreas Fiehn
"""

def convertTemperature(t='50', unit_from='fahrenheit', unit_to='celsius'):
#Converts the temperature from one unit to another
#
# Parameters:
# t -- temperature (default 50)
# unit_from -- unit converting from (default celsius)
# unit_to -- un it to convertinto (default fahrenheit)
# 
# Accepted units are "Fahrenheit", "Celsius", or "Kelvin"
    
    if unit_from.lower() == "fahrenheit":
        if unit_to.lower() == "celsius":
            t = (t-32)/1.8 
        elif unit_to.lower() == "kelvin":
            t = (t + 459.67)/1.8
    elif unit_from.lower() == "celsius":
        if unit_to.lower() == "fahrenheit":
            t = 1.8 * t + 32
        elif unit_to.lower() == "kelvin":
            t = t + 273.15
    elif unit_from.lower() == "kelvin":
        if unit_to.lower() == "fahrenheit":
            t = 1.8 * t - 459.67
        elif unit_to.lower() == "celsius":  
            t = t - 273.15
    return t