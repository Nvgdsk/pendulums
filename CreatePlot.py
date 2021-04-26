import numpy as np
import matplotlib.pyplot as plt
import csv

x1List = []
x2List = []
v1List = []
v2List = []
timeList = []

with open('/output.txt', newline = '' ) as file:
    reader = csv.reader(file)
    
    for row in reader:
       
        timeList.append(float(row[0]))
        x1List.append(float(row[3]))        
        x2List.append(float(row[4]))        
        v1List.append(float(row[1]))        
        v2List.append(float(row[2]) )   



fig, ax = plt.subplots()
ax.plot(timeList,v1List) 
ax.plot(timeList,v2List) 
plt.ylabel('V')
plt.xlabel('t')
ax.grid()

plt.show()


fig, ax = plt.subplots()
ax.plot(timeList,x1List) 
ax.plot(timeList,x2List) 
plt.ylabel('x')
plt.xlabel('t')
ax.grid()

plt.show()
