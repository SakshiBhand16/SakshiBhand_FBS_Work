def fibonacci(n):
    a = 1
    b = 1
    for i in range(1, n+1):
        print(a, end = ' ')
        c = a+b
        a = b
        b = c
    return
n = int(input('enter the number:'))
fibonacci(n)
