num = int(input("Enter a 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == c:
    print("Palindrome")
else:
    print("Not Palindrome")