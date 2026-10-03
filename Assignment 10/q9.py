li = [10, 20, 30, 40, 50, 79]
even = []
odd = []
for i in li:
    if(i % 2 == 0):
        even = even + [i]
    else:
        odd = odd+[i]
print(even)
print(odd)