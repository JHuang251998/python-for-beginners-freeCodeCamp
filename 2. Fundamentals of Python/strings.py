name = "beau"
name += " is a person"
print(name)

print("beau".upper())
print("bEAu".lower())
print("bEAu person".title())

print(" ".join("Hello"))
print("Hello world how are you".split())
print("Are;you;in;a;good;mood".split(";"))

# String methods return another string but do not modify original string
print(name.upper())
print(name)

print("au" in name)

# Escaping characters
print("B\"ea\"u")
print("B'ea'u")
print('B"ea"u')
print("Be\\au")

# Slicing
print(name[1:7])
print(name[5:])
print(name[::2])
print(name[::-1])