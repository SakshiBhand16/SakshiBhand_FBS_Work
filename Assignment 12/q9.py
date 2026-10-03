str1 = input("Enter a string: ")

words = 0
characters = 0
space = 0

for i in str1:
    characters = characters + 1

    if i == " ":
        space = 1
    else:
        if space == 1:
            words = words + 1
            space = 0

if characters > 0:
    words = words + 1

print("Number of words:", words)
print("Number of characters:", characters)