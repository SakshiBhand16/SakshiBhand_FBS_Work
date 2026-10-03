str = input('enter the string:')
n = int(input('enter the index:'))
new = ' '
size = len(str)
for i in range (size):
    if(i != n):
        new = new+ str[i]
print(new)