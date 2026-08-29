amount = int(input('enter the amount: '))
num2000 = amount // 2000
amount = amount % 2000

num500 = amount // 500
amount = amount % 500

num200 = amount // 200
amount = amount % 200

num100 = amount // 100
amount = amount % 100

num50 = amount // 50
amount = amount % 50

num20 = amount // 20
amount = amount % 20

num10 = amount // 10
amount = amount % 10

num5 = amount // 5
amount = amount % 5

num2 = amount // 2
amount = amount % 2

num1 = amount // 1
amount = amount % 1

total = num2000 + num500 + num200 + num100 + num50 + num20 + num10 + num5 + num2 + num1
print(total)