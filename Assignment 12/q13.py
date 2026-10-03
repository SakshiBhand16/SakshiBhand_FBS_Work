str = input('enter a string: ')

letters = 0
digits = 0

for i in str:
    if i >= 'a' and i <= 'z':
        letters = letters + 1
    elif i >= 'A' and i <= 'Z':
        letters = letters + 1
    elif i >= '0' and i <= '9':
        digits = digits + 1

print('number of letters:', letters)
print('number of digits:', digits)