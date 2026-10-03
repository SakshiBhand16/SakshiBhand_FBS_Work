str = input('enter the str:')
new = ' '
for i in str:
    if(i == 'a'):
        new = new+'&'
    else:
        new = new + i
print(new)

