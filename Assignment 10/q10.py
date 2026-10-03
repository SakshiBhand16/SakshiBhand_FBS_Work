li = [10, 20, 30, 40, 50, 79, 20, 30, 20]
n = int(input('enter the no:'))
new = []
for i in li:
    if(i!=n):
        new = new+[i]
print(new)