# Everything in Python is an object

items = [1, 2]
items.append(3)
items.pop()

print(id(items))

age = 8

print(id(age))

# This creates an entirely new object
age = age + 1

# The id is not going to be the same as before, since it is not the same object
print(id(age))