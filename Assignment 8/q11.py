def armstrong(n):
    temp = n
    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + r ** 3
        n = n // 10

    if sum == temp:
        return True
    else:
        return False


n = int(input("Enter number: "))

print(armstrong(n))