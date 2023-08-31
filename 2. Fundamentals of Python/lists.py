dogs = ["Roger", "Syd", "Quincy"]

dogs[1] = "Beau"
dogs.append("Judah")

dogs.extend(["Jim", "Jonny"])
dogs += ["Mike", "Jimmy"]

# Puts every letter as a single element
dogs += "pig"

dogs.remove("Quincy")
print(dogs.pop())

dogs.insert(2, "Test")
# Insert multiple elements
dogs[1:1] = ["Test1", "Test2"]

dogs.sort()
print(dogs, '\n')
# Key takes a function
print(sorted(dogs, key = str.lower), '\n')

print(dogs)
print(len(dogs))