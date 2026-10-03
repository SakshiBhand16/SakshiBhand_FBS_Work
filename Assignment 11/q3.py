def bubblesort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size-i):
            if(li[j][1] > li[j+1][1]):
                li[j], li[j+1] = li[j+1],  li[j]
                #print(li) ##( for print step by step swaping)
    return li
li = li = [[1, 50], [2, 20], [3, 40], [4, 10]]
res =  bubblesort(li)
print(res)

    