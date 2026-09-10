length = int(input('enter length of wall:'))
height = int(input('enter height of wall:'))
rate = int(input('enter painting cost per sq.ft:'))

area = 4 * length * height
cost = area * rate

print('total cost of painting:', cost)