li = [10, 20, 40, 50]
li1 = [40, 50, 60, 80]
new = []
for i in li:
    if i in li1:
        new.append(i)
print(new)