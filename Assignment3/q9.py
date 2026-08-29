m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))
m4 = int(input("Enter marks of subject 4:"))
m5 = int(input("Enter marks of subject 5:"))

total = m1 + m2 + m3 + m4 + m5

if total > 75:
    print("First Class")
elif total > 60:
    print("Second Class")
elif total > 50:
    print("Third Class")
else:
    print("Fail")