def bubblesort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li
li = [10, 70, 50, 20, 40, 30]
bubblesort(li)
print(li[-2])