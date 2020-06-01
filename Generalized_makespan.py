import numpy as np
import random
import pandas as pd

c = input('Do you want the enter the data from file?y/n')
if c == 'y':
    file_name = input('enter file name')
    # file_name=ptime.txt
    df = pd.read_csv(file_name, delimiter=',')
    col = len(df.axes[1])
    row = len(df.axes[0])
    l = []
    for i in range(0, col):
        l.append(np.array(df[f'J{i + 1}']))
    pt = np.array(l)

    x = int(np.shape(pt)[0])
    y = int(np.shape(pt)[1])

else:
    x = int(input('enter the number of jobs'))
    y = int(input('enter the number of machines'))
    # pt=np.array([[1,2,3,4],[5,2,1,2],[3,4,2,5],[2,4,5,1]])
    list1 = []

    for i in range(0, x):
        list1.append([])
        for j in range(0, y):
            # k=int(input(f'enter the processing time of JOB {i+1} in Machine {j+1}'))
            list1[i].append(int(input(f'enter the processing time of JOB {i + 1} in Machine {j + 1}')))
    pt = np.array(list1)

M = []
for i in range(0, y):
    M.append([])

# enter the order here
# o=[4,3,1,2,0]
o = []
for t in range(0, x):
    o.append(t)
random.shuffle(o)

print(f'The order is {o}')

s = 0

for i in range(0, x):
    s = s + pt[o[i], 0]
    M[0].append(s)
    for j in range(1, y):
        M[j].append(M[j - 1][i] + pt[o[i], j])

for i in range(0, y - 2):
    for j in range(0, x - 1):
        if M[i][j + 1] < M[i + 1][j]:
            M[i + 1][j + 1] = M[i + 1][j] + pt[o[j + 1], i + 1]
            M[i + 2][j + 1] = M[i + 1][j + 1] + pt[o[j + 1], i + 2]

for i in range(0, x - 1):
    if M[-2][i + 1] > M[-1][i]:
        M[-1][i + 1] = M[-2][i + 1] + pt[o[i + 1], -1]
    else:
        M[-1][i + 1] = M[-1][i] + pt[o[i + 1], -1]
# processing_time array    
# print(pt)

# A=np.array([M[0],M[1],M[2],M[3]])
A = np.array(M)
# makespan calculation array
# print(A)
print(f'The makespan time of given order is: {A[-1, -1]} units')