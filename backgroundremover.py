def main(rest, pulse, offset, initial, final):

    restT = rest 
    pulseT = pulse
    offset = offset

    initialT = initial
    finalT = final

    def pointfinder(x1,y1,x2,y2):
        m = (y1-y2)/(x1-x2)
        return lambda x: m*(x-x1)+y1

    def findAveragePoint(x,jump):
        with open("pulsedata.csv", 'r') as f:
            f.seek(jump)
            yval = 0.0
            counter = 0
            f.readline()
            point = f.readline().split(',\t')
            while(float(point[4]) < x-10):
                point = f.readline().split(',\t')
            while(float(point[4]) < x):
                yval += float(point[5])
                counter+=1
                point = f.readline().split(',\t')
            
            return [x-5,yval/counter], f.tell()


    with open("Python\DrDave\EC-MS\pulsedata.csv", 'r') as r:
        r.readline()
        with open("Python\DrDave\EC-MS\\backgroundRemovedData.txt",'w') as w: 
            w.write("Time Relative (sec),	M2 \n")

            sampleTs = list(range(int(restT+initialT), int(finalT), restT+pulseT))
            averagePoint1 = r.readline().split(',\t')[4:6]
            averagePoint1 = [float(value) for value in averagePoint1]

            point = r.readline().split(',\t')
            jump = 0

            for x in sampleTs:
                averagePoint2, jump = findAveragePoint(x,jump)
                pointfunc = pointfinder(averagePoint1[0],averagePoint1[1],averagePoint2[0],averagePoint2[1])

                while(float(point[4]) < x-5):
                    w.write(point[4] + ',\t' + str(float(point[5])-pointfunc(float(point[4]))) + '\n')
                    point = r.readline().split(',\t')

                averagePoint1 = averagePoint2

    print("DONE")




