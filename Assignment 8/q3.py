#a. 1+ 2 + 3 + 4+..... + n

def sumofseries(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum+i
    return sum
  
n = int(input('enter the number:'))
print(sumofseries(n))

#1! + 2! + 3! + ... + n!
def sumofseries(n):
    sum = 0
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
        sum = sum + fact
    return sum
  
n = int(input('enter the number:'))
print(sumofseries(n))

#1¹ + 2² + 3³ + ... + nⁿ
def sumofseries(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum+i**i
    return sum
n = int(input('enter the number:'))
print(sumofseries(n))



