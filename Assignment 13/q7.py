student = {
    "name": "Sakshi",
    "age": 22,
    "city": "Pune"
}
key = input("Enter the key to remove: ")
new = {}
for i in student:
    if i != key:
        new[i] = student[i]

print(new)