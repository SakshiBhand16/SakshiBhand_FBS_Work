n = int(input("Enter number of passengers: "))
cost = int(input("Enter ticket cost: "))

total = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger: "))

    if age < 12:
        ticket = cost - (cost * 30 / 100)

    elif age > 59:
        ticket = cost - (cost * 50 / 100)

    else:
        ticket = cost

    total = total + ticket

print("Total ticket amount =", total)