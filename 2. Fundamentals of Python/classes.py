class Animal:
    def walk(self):
        print("Walking...")

# Inheritance declared in parentheses
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("Woof!")

roger = Dog("Roger", 8)

print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()

roger.walk()