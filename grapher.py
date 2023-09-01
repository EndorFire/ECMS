import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')

def main():
    x = []
    y = []

    with open("pulsedata.csv") as f: 
        next(f)
        for line in f:
            point = line.split(",\t")
            try:
                x.append(float(point[4]))
                y.append(float(point[5]))
            except:
                break
            
    x = np.array(x)
    y = np.array(y)

    fig, ax = plt.subplots()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    xstepSize = 500
    ystepSize = .1
    ax.set_xticks(np.arange(min(x), max(x)+xstepSize, step=xstepSize))
    ax.set_yticks(np.arange(min(y), max(y)+ystepSize, step=ystepSize))

    ax.plot(x, y, markersize = 10)

    plt.show()
    