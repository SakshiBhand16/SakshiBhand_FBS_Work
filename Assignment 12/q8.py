str = input('enter the string: ')
new = ' '
size = len(str)
for i in range(size):
    if i % 2 == 0:
        new = new + str[i]
print(new)