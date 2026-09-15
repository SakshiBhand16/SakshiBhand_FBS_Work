n = int(input('enter number of employees: '))

total = 0

for i in range(1, n + 1):

    basic = float(input('Enter basic salary: '))

    if basic < 20000:
        da = basic * 10 / 100