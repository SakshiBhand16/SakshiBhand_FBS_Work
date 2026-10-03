# write a program to fine second max number from the list
lis = [10, 20, 30, 40, 50, 60, 10, 40]  
max = lis[0]
smax = 0
for ind in range(1, len(lis)):
    if lis[ind]>max:
        smax = max
        max = lis[ind]
    elif lis[ind]>smax:
        smax = lis[ind]
print(max)
print(smax)