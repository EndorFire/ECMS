import os
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')


def main(rest, pulse, initial, final):
    x = []
    y = []
    restT = rest
    pulseT = pulse
    initialT = initial + restT
    finalT = final
    trialStartTime = initialT


    with open("pulsedata.csv",'r') as f:
        next(f)
        pulseCounter = 1
        dataHolder = []

        line = f.readline()
        point = line.strip().split(",")

        while(float(point[0])<(initialT)):
            line = f.readline()
            point = line.strip().split(",")

        try: 
            os.mkdir(os.getcwd() + "\pulseDataSplit")
        except OSError as error: 
            pass 
        try: 
            os.mkdir(os.getcwd() + "\pulseDataSplit\EC")
        except OSError as error: 
            pass 

        while(float(point[0])<(finalT-restT-pulseT)):
            dataHolder = []
            while(float(point[0]) < (trialStartTime + pulseT)):
                dataHolder.append(point)
                line = f.readline()
                point = line.strip().split(",")

            with open(f"pulseDataSplit\EC\\pulse{pulseCounter}.txt",'w') as pFile: 
                for dataPoint in dataHolder: 
                    dataPoint[0] = str(float(dataPoint[0])-trialStartTime)
                    pFile.write(''.join(dataPoint[0:3]).strip()+'\n')
                    
            dataHolder = []

            while(float(point[0]) < (trialStartTime + restT + pulseT)):
                dataHolder.append(point)
                line = f.readline()
                point = line.strip().split(",")
            with open(f"pulseDataSplit\EC\\rest{pulseCounter}.txt",'w') as rFile: 
                for dataPoint in dataHolder: 
                    dataPoint[0] = str(float(dataPoint[0])-trialStartTime)
                    rFile.write(''.join(dataPoint[0:3]).strip()+'\n')

            trialStartTime += restT + pulseT
            pulseCounter+=1



