def sumofodd(n):
    sum = 0
    for i in (1,n+1,2):
        sum = sum+i
    return sum
n = int(input('enter the number:'))
print(sumofodd(n))

