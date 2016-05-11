import math 
import csv
import numpy as np
output=np.zeros((1000,36))
k=0
a=[]
s=0  #format of output is such that the time for i-j node  is the (6*(i-1)+j)th bit for the kth time stamp.0 =>no data
x=np.array(list(csv.reader(open('C:/Users/Abhijeet/Downloads/traffic_data.csv', 'rb'),delimiter=','))).astype(float)   
max_range=len(x)
for i in range(max_range):
    a.append(x[i][0]*100+x[i][1]*10+x[i][2])

for i in range(max_range):
    k=0
    s=0
    for j in range(max_range):
        if (a[i]==a[j]):
            k+=1
            s+=(x[j][3])
            print i,j
       
    val1=int(x[i][0])
    val2=int((x[i][1]-1)*6)
    val3=int(x[i][2])
    
    output[val1-1][val2+val3-1]=s/(k)
    

