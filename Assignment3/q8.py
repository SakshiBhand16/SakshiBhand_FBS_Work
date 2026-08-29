import random

username = input("Enter username: ")
password = input("Enter password: ")

if username == "sakshi@123" and password == "sakshi@12345":
    num = random.randint(1000, 9999)
    print(num)

    n = int(input("Enter the number: "))

    if n == num:
        print("Success")
    else:
        print("Failed")
else:
    print("Incorrect username or password")