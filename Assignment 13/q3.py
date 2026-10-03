student = {
    "name": "Sakshi",
    "age": 22,
    "city": "Pune"
}
key = input('Enter the key: ')
found = 0
for i in student:
    if i == key:
        found = 1
if found == 1:
    print('key exists')
else:
    print('key does not exist')