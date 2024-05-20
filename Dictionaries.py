dict1={
    "Name":"Ayush",
    "Age":20,
    "Country":"India"
}
dict1["Hobbies"]="Gaming"
print(dict1)

print(dict1["Name"])
#or
print(dict1.get("Name"))

dict1["Name"]="Molu"
print(dict1)