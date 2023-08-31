dog = {"name": "Roger", "age": 8, "sex": "male"}

dog["name"] = "Syd"

print(dog["name"], dog.get("name"))

# get() method does not modify dictionary if key doesn't exist
print(dog.get("color", "brown"))

print(dog.keys())
print(list(dog.keys()))

print(dog.values())
print(list(dog.values()))

print(dog.items())

print(dog.pop("name"))
# popitem() deletes the last key value pair
print(dog.popitem())

dog["favorite food"] = "meat"
dog["color"] = "green"

print(dog)

del dog["color"]

dogCopy = dog.copy()

print(dog)
print(dogCopy)