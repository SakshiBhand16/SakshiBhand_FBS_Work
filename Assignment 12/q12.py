str = input("Enter a string: ")
count = 0
for i in str:
    if i >= 'a' and i <= 'z':
        count = count + 1
print('number of lowercase characters:', count)