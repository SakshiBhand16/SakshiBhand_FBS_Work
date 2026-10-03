li = [10, 20, 10, 30, 40, 50, 60]
li1 = []
for i in li:
    found = 0
    for j in li1:
        if ( i == j):
            found = found+1
    if found == 0:
        li1 = li1+ [i]

print(li1)

