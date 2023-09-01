import os
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')


def main(rest, pulse, offset, initial, final):

    x = []
    y = []
    restT = rest #Seconds
    pulseT = pulse #Seconds
    offset = offset #Seconds
    initialT = initial + restT + offset
    finalT = final 
    trialStartTime = initialT




    with open("Python\DrDave\EC-MS\pulsedata.csv",'r') as f:
        next(f)
        pulseCounter = 1
        dataHolder = []

        line = f.readline()
        point = line.strip().split(",")

        while(float(point[4])<(initialT)):
            line = f.readline()
            point = line.strip().split(",")

        try: 
            os.mkdir(os.getcwd() + "\pulseDataSplit")
        except OSError as error: 
            pass 
        try: 
            os.mkdir(os.getcwd() + "\pulseDataSplit\MS")
        except OSError as error: 
            pass


        while(float(point[4])<(finalT-restT-pulseT)):
            dataHolder = []
            while(float(point[4]) < (trialStartTime + pulseT)):
                dataHolder.append(point)
                line = f.readline()
                point = line.strip().split(",")
            with open(f"pulseDataSplit\MS\MSpulse{pulseCounter}.txt",'w') as pFile: 
                for dataPoint in dataHolder: 
                    dataPoint[4] = str(float(dataPoint[4])-trialStartTime)
                    pFile.write(''.join(dataPoint[4:]).strip() + '\n')
            dataHolder = []


            while(float(point[4]) < (trialStartTime + pulseT + restT)):
                dataHolder.append(point)
                line = f.readline()
                point = line.strip().split(",")

            with open(f"pulseDataSplit\MS\MSrest{pulseCounter}.txt",'w') as rFile: 
                for dataPoint in dataHolder: 
                    dataPoint[4] = str(float(dataPoint[4])-trialStartTime)
                    rFile.write(''.join(dataPoint[4:]).strip() + '\n')

            trialStartTime += restT + pulseT
            pulseCounter+=1