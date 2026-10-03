str1 = input("Enter a string: ")

words = str1.split()
frequency = {}

for i in words:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1

print(frequency)