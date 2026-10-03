str1 = input("Enter a string: ")

words = {}
word = ""

for i in str1:
    if i != " ":
        word = word + i
    else:
        if word != "":
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1
            word = ""

if word != "":
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1

for i in words:
    print(i, ":", words[i])