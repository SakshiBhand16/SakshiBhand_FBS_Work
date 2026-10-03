str1 = input('enter first string: ')
str2 = input('enter second string: ')
count1 = 0
count2 = 0
for i in str1:
    count1 = count1 + 1
for i in str2:
    count2 = count2 + 1
if count1 > count2:
    print('large string is:', str1)
elif count2 > count1:
    print('larger string is:', str2)
else:
    print('Both strings are equal')