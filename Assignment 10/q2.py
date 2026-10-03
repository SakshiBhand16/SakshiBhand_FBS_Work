li = [10, 50, 20, 5, 40]

max = li[0]
min = li[0]

for i in range(1, len(li)):
    if li[i] > max:
        max = li[i]

    if li[i] < min:
        min = li[i]

print(max)
print(min)