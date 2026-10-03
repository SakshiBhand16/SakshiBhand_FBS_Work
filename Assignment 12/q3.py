str1 = input('enter first string: ')
str2 = input('enter second string: ')
count1 = 0
count2 = 0
for i in str1:
    count1 = count1 + 1
for i in str2:
    count2 = count2 + 1
if count1 != count2:
    print('strings r not')
else:
    flag = 1
    for i in str1:
        c1 = 0
        c2 = 0
        for j in str1:
            if i == j:
                c1 = c1 + 1
        for j in str2:
            if i == j:
                c2 = c2 + 1
        if c1 != c2:
            flag = 0
    if flag == 1:
        print('strings r anagram')
    else:
        print('strings not anagrams')