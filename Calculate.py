import math

#input
NUM_ITERATIONS = 2000
TIME_INTERVAL = 10
step = float(TIME_INTERVAL) / NUM_ITERATIONS
init_time = 0
dx1 = 0.05
dx2 = 0.15
k1 = 100 
k2 = 100 
ix1 = 0.1
ix2 = 0.2
m1 = 1 
m2 = 1 
z1 = 0.2
z2 = 0
#create and erase file
f = open('/output.txt', 'w')
f.close()

#getFirstSpeed
def f1(dx1, dx2, v1):
    return (k2*((dx2 - dx1) - (ix2 - ix1)) - k1*(dx1 - ix1) - z1*v1)/m1  

#getSecondSpeed
def f2(dx1, dx2,v2):
    return (-k2*((dx2 - dx1) - (ix2 - ix1)) - z1*v2)/m2


def saveResults(v1List, v2List, x1List, x2List):
    file = open('/output.txt', "a+")
    file.seek(0)
    file.truncate()
    t = 0
    for v1, v2, x1, x2 in zip(v1List, v2List, x1List, x2List):
        line = ','.join((str(t), str(v1), str(v2), str(x1), str(x2)))
        file.write(line)
        file.write("\n")
        t += step
    file.close()

x1List = []
x2List = []
v1List = []
v2List = []
timeList = []
v1 = f1(dx1, dx2, 0)
v2 = f1(dx1, dx2, 0)
time = 0
while time <= TIME_INTERVAL:
    
    dif1 = step * v1
    dif2 = step * v2
    dx1 = dx1 + dif1
    dx2 = dx2 + dif2
    v1 = v1 + step * f1(dx1, dx2,v1)
    v2 = v2 + step * f2(dx1, dx2,v2)

    x1List.append(dx1)
    x2List.append(dx2)
    v1List.append(v1)
    v2List.append(v2)
    timeList.append(time)
    time += step
    
saveResults(v1List, v2List, x1List, x2List)
