###1. Area and perimeter of the given figure
import math

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area = (length * breadth) + (0.5 * math.pi * radius * radius)

perimeter = length + length + breadth + (math.pi * radius)

print("Area of figure:", area)
print("Perimeter of figure:", perimeter)