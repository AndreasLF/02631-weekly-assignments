# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:39:44 2020

@author: Andreas Fiehn
"""

import numpy as np

def clusterAnalysis(reflectance):
    cluster1 = []
    cluster2 = []
    
    #Loops through reflectance
    for n in range(len(reflectance)):
        # Checks if float is odd or even and adds it to the closter correspondingly
        if n % 2 == 0:
            cluster1.append(reflectance[n])
        else:
            cluster2.append(reflectance[n])

   
    #Define lists outside of loop
    clusterassignment = []
    prevCluster1 = []
    prevCluster2 = []
    
    # Loops until break occurs
    while True: 
        
        # calculate mean
        mean1 = np.mean(cluster1)
        mean2 = np.mean(cluster2)
        
        # Clear lists
        cluster1 = []
        cluster2 = []
        clusterassignment = []
        
        #Loops through reflectance
        for r in reflectance:
            # Checks if float is odd or even and adds it to the closter correspondingly
            if abs(r-mean1) <= abs(r-mean2):
                cluster1.append(r)
                clusterassignment.append(1)
            else:
                cluster2.append(r)
                clusterassignment.append(2)
                
        #Checks if the new cluster is identical to the previous
        if cluster1 == prevCluster1 and cluster2 == prevCluster2:
            break
        else:
            prevCluster1 = cluster1
            prevCluster2 = cluster2
            
    return clusterassignment
