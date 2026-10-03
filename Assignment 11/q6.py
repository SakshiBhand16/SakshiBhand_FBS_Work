li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]
new = []
for i in li1:
    if i not in new:
        new.append(i)
for i in li2:
    if i not in new:
        new.append(i)
print(new)


