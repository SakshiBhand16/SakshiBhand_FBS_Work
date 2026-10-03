dict1 = {
    "name": "Sakshi",
    "age": 22
}
dict2 = {
    "city": "Pune",
    "course": "Python"
}
dict3 = {}
for key in dict1:
    dict3[key] = dict1[key]
for key in dict2:
    dict3[key] = dict2[key]
print(dict3)