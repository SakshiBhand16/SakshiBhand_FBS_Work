start = int(input("Enter start: "))
end = int(input("Enter end: "))
num = int(input("Enter number: "))

for i in range(start, end + 1):
    if i % num == 0:
        print(i)