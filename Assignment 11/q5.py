def bubblesort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size-i):
            if len(li[j]) > len(li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]
    return li
li = ["cat", "elephant", "dog", "hi"]
bubblesort(li)
print(li)