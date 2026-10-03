def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return reverse(n // 10, rev)


n = int(input("Enter number: "))
print(reverse(n))
