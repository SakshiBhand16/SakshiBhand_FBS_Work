str = input('enter the string: ')

new = ' '

size = len(str)

for i in range(size):
    if i == 0:
        new = new + str[size - 1]
    elif i == size - 1:
        new = new + str[0]
    else:
        new = new + str[i]

print(new)