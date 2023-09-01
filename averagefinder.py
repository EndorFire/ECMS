def main(start, stop): 

    with open("pulsedata.csv",'r') as f: #Put csv filepath here
        sum = 0
        entries = 0

        next(f)

        line = f.readline()
        point = line.strip().split(",")

        while(float(point[0])<start):
            line = f.readline()
            point = line.strip().split(",")

        while(float(point[0])<stop):
            sum += float(point[2])
            entries += 1
            line = f.readline()
            point = line.strip().split(",")        

    average = sum/entries
    print(f"Average from {start} to {stop}: {average} mA")

    with open("Average.txt",'w') as q: #Put desired filepath here
        q.write(f"Average from {start} to {stop}: {average} mA")