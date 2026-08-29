a = int(input('enter the side:'))
b = int(input('enter the side:'))
c = int(input('enter the side:'))
if( a<b+c and b<a+c and c<a+b):
    print('valid')
else:
    print('not valid')