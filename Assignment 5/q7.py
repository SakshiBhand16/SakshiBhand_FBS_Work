##7(a) #1! + 2! + 3! + ... + n!
n = int(input("Enter n: "))

fact = 1
sum = 0

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print(sum)


##7(b) N + N² + N³ + ... + Nᴺ
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + n ** i

print(sum)



##7(c) Geometric series from 1 to n, common ratio = 2
n = int(input("Enter n: "))

term = 1
sum = 0

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print(sum)


##7(d) S = a + a²/2 + a³/3 + ... + a¹⁰/10
a = int(input("Enter a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print(sum)