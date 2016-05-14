import math 
import csv
import numpy as np
n=int(raw_input('give no of nodes')) 
output=np.zeros((1000,n*n))
output2=[]
for i in range(n*n):
    output2.append([])
k=0
a=[]
b=[]
if n<9:                
    t=10
elif n<99:
    t=100
elif n<999:
    t=1000
elif n<9999:
    t=10000
              #format of output is such that the time for i-j node  is the (n*(i-1)+j)th bit for the kth time stamp.0 =>no data
x=np.array(list(csv.reader(open('C:/Users/Abhijeet/Downloads/traffic_data.csv', 'rb'),delimiter=','))).astype(float)   
max_range=len(x)
for i in range(max_range):
    a.append(x[i][0]*t*t+x[i][1]*t+x[i][2])

for i in range(max_range):
    k=0
    s=0
    for j in range(max_range):
        if (a[i]==a[j]):
            k+=1
            s+=(x[j][3])
            
       
    val1=int(x[i][0])
    val2=int((x[i][1]-1)*n)
    val3=int(x[i][2])
    
    output[val1-1][val2+val3-1]=s/(k)
for i in range(max_range):
  b.append(x[i][1]*t+x[i][2])
for i in range(max_range):
    k=0
    s=0
    for j in range(max_range):
        if (b[i]==b[j]):
            k+=1
            s+=(x[j][3])
       
    val1=int(x[i][0])
    val2=int((x[i][1]-1)*n)
    val3=int(x[i][2])
    output2[val2+val3-1]=s/(k)


def conn_matrix(time_stamp):
    #make a nxn matrix where n= no of nodes
    M=[]
    for i in range(n):
        M.append([])
        for j in range(n):
            if float(output[time_stamp][i*n +j]) !=0.0:
                M[i].append(output[time_stamp][i*n +j])
            else:
                M[i].append(output2[i*n +j])
            if i==j:
                M[i][j]=0
    
    return M



    
            
