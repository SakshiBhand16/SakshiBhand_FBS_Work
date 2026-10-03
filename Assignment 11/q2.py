li1 = [30, 10, 50]

li2 = [40, 20, 60]
new = []
for i in li1:
    new = new + [i]
for i in li2:
    new = new + [i]
print(new)
new1 = new
def bubblesort():
    size = len(new1)
    for i in range(1, size):
        for j in range(0, size-i):
            if new1[j] > new1[j+1]:
                new1[j], new1[j+1] = new1[j+1], new1[j]
    return new1
res = bubblesort()
print(res)
