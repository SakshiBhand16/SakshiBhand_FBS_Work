start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3    # if digit is in range between 100 to 999
        temp = temp // 10

    if total == num:
        print(num)
else:
    print('there is no number between this numbres')