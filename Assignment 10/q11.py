li = [10, 20, 30, 40, 50, 79, 20, 30, 20]
m = 2
n = 3
new = []
for i in li:
    if(i%m == 0 and i%n == 0):
        new = new + [i]
print(new)