n = int(input('Enter 3 digit number:'))

a = n // 100
b = (n // 10) % 10
c = n % 10

if a == 2*b  and    c == 2*a:
    print('yes you have done it')

else:
    print('please try next time')