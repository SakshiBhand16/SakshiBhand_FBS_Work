def prime(n):
    count=0
    for i in range(1, n+1):
        if(n%i==0):
            count = count+1
    if(count==2):
        return True
    else:
        return False

def sumprime(n):
    sum=0
    for i in range(1,n+1):
        if(prime(i)):
            sum = sum+i
    return sum
n = int(input('enter the number:'))
print(sumprime(n))
