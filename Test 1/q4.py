##4. Calculate the cost of painting both rooms
area = float(input('enter area of one wall: '))
interior_cost = float(input('enter interior painting cost per unit: '))
exterior_cost = float(input('rnter exterior painting cost per unit: '))

interior_area = 7 * area
exterior_area = 6 * area

total_interior_cost = interior_area * interior_cost
total_exterior_cost = exterior_area * exterior_cost

total_cost = total_interior_cost + total_exterior_cost

print('interior painting cost:', total_interior_cost)
print('exterior painting cost:', total_exterior_cost)
print('total painting cost:', total_cost)