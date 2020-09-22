# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:07:41 2020

@author: Andreas Fiehn
"""
import numpy as np
import matplotlib.pyplot as plt

def getAngle(v1):
     # returns False if the vector is [0,0] since it would not have a direction
    if (np.array_equal(v1,np.array([0,0]))):
        return False

    v2 = np.array([20,0])

    # calculate unit vectors
    v1_unit = v1 / np.linalg.norm(v1)
    v2_unit = v2 / np.linalg.norm(v2)

    theta = np.arccos(np.dot(v1_unit,v2_unit))

    return theta

def computePassesGoalLine(point, directionVector):

    # checks if ball is kicked from outside the field
    if point[0] <= 68 or point[0] >= 0 or point[1] <= 105 or point[1] >= 0:
       # define goals with the ball position as origo
       goal1 = np.array([np.array([(0 - point[0]),(30.34 - point[1])]),np.array([(0 - point[0]),(37.66 - point[1])])])
       goal2 = np.array([np.array([(105 - point[0]),(30.34 - point[1])]),np.array([(105 - point[0]),(37.66 - point[1])])])


       shootingAngle = getAngle(directionVector)

       goal1Angles = np.array([getAngle(goal1[0]),getAngle(goal1[1])])
       goal2Angles = np.array([getAngle(goal2[0]),getAngle(goal2[1])])

       
       # plt.plot(np.array([0,105,105,0,0])-point[0],np.array([0,0,68,68,0])-point[1])
       # plt.plot(np.array([0,0])-point[0],np.array([30.34,37.66])-point[1],"ro")
       # plt.plot(np.array([105,105])-point[0],np.array([30.34,37.66])-point[1],"ro")
       # plt.plot(0,0,"ro",color="black")
       # plt.quiver(directionVector[0],directionVector[1],scale=5)
       # plt.quiver(goal1[0][0],goal1[0][1],scale=1,color="blue")
       # plt.quiver(goal1[1][0],goal1[1][1],scale=1,color="blue")
       # plt.quiver(goal2[0][0],goal2[0][1],scale=1,color="blue")
       # plt.quiver(goal2[1][0],goal2[1][1],scale=1,color="blue")
       # plt.show()


       if min(goal1Angles) < shootingAngle and shootingAngle < max(goal1Angles):
           return True
       elif min(goal2Angles) < shootingAngle and shootingAngle < max(goal2Angles):
           return True
       else:
           return False

    else:
        return "Ball is outside of the field"


computePassesGoalLine(np.array([10,10]),np.array([5,2]))
