# jhonson's algorithm(2 machines)
import numpy as np
import pandas as pd

list1 = []
l1 = []
l2 = []
l3 = []
l4 = []

c = input('do you want to enter data from file? y/n')
if c == 'y':
    file_name = input('enter the file name: ')
    # file_name=j_rule.txt

    df = pd.read_csv(file_name, delimiter=',')
    a = np.array(df['m1'])
    b = np.array(df['m2'])
    n = np.size(a)
    for i in range(0, np.size(a)):
        list1.append(i)
        l1.append(a[i])
        l2.append(b[i])

else:
    n = int(input('enter the number of parts'))

    for i in range(0, n):
        list1.append(i)
        l1.append(int(input(f'enter the processing time of job{i + 1} on machine1')))
        l2.append(int(input(f'enter the processing time of job{i + 1} on machine2')))
# print(list1)
# print(l1)
# print(l2)
for i in range(0, n):
    x1 = min(l1)
    x2 = min(l2)
    if x1 == x2:
        if l1[l1.index(x1)] + l2[l1.index(x1)] < l1[l2.index(x2)] + l2[l2.index(x2)]:
            x = x1
        else:
            x = x2
    elif x1 != x2:
        x = min(x1, x2)
    if x == x1:
        k = l1.index(x1)
        l3.append(list1[k])
    else:
        k = l2.index(x2)
        l4.append(list1[k])
    list1.pop(k)
    l1.pop(k)
    l2.pop(k)
l4.reverse()
new_list = l3 + l4

for i in range(0, len(new_list)):
    new_list[i] = new_list[i] + 1
print(f'the optimum order is {new_list}')

