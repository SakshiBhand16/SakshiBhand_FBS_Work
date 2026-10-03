str1 = input('enter first string: ')
str2 = input('enter second string: ')

count1 = 0
count2 = 0

for i in str1:
    count1 = count1 + 1

for i in str2:
    count2 = count2 + 1

if count1 > count2:
    print('larger string:', str1)
elif count2 > count1:
    print('larger string:', str2)
else:
    print('both strings are equal')