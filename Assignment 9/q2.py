def armstrong(temp, num, count, sum=0):
    if temp == 0:
        if num == sum:
            print("Number is Armstrong")
        else:
            print("Number is not Armstrong")
        return

    d = temp % 10
    sum = sum + d ** count

    armstrong(temp // 10, num, count, sum)


n = int(input("Enter number: "))

count = len(str(n))

armstrong(n, n, count)