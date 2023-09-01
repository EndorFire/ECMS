import os
from scipy import integrate
from natsort import natsorted



def main(): 
    folder_path = "\pulseDataSplit\\"

    with open("integrationResults.txt", 'w') as Results:
        Results.write("Filename\tAverage Potential\t Charge\n")
        Results.write("none\tV\tC\n")
        for filename in natsorted(os.listdir(folder_path+"EC\\")):
            inputArray = []
            sampleArray = []
            voltage = 0
            with open(folder_path+"EC\\"+filename,'r') as f:
                data = f.read()
                data = data.split('\n')
                for dataPoint in data[:-1]:
                    dataPoint = dataPoint.split('\t')
                    inputArray.append(float(dataPoint[2]))
                    sampleArray.append(float(dataPoint[0]))
                    voltage += float(dataPoint[1])

                averageVoltage = voltage/(len(data)-1)

                totalCoulombs = integrate.trapezoid(inputArray, x = sampleArray)
                Results.write(filename[:-4] + f"\t{str(averageVoltage)[:6]}" + "\t" + str(totalCoulombs) + '\n')

        Results.write("\nFilename\t 2amu Signal\n")
        Results.write("None\t C\n")
        for filename in natsorted(os.listdir(folder_path+"MS\\")):
            inputArray = []
            sampleArray = []
            with open(folder_path+"MS\\"+filename,'r') as f:
                data = f.read()
                data = data.split('\n')
                for dataPoint in data[:-1]:
                    dataPoint = dataPoint.split('\t')
                    inputArray.append(float(dataPoint[1]))
                    sampleArray.append(float(dataPoint[0]))

                totalValue = integrate.trapezoid(inputArray, x = sampleArray)
                Results.write(filename[:-4] + "\t" + str(totalValue) + '\n')
