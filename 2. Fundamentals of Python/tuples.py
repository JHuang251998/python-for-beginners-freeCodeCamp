names = ("Roger", "Syd")

print(type(names))

# Tuples do not have 'append'
#names.append("Beau") ## Error

names_cp = names + ("Beau", "Alice")

print(names_cp, '\n')
print(sorted(names_cp), '\n')

# To add single element, convert it to tuple
# tuple("Ben") doesn't work since tuple() can only convert iterable objects
names_cp1 = names_cp + ("Ben",)

print(names_cp1)