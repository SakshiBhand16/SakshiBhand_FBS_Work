str = input('enter the string: ')
new = ' ' 
for i in str:
    if i == ' ':
        new = new + '-'
    else:
        new = new + i

print(new)