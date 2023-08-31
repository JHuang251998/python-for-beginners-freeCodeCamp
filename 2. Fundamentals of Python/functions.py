def change(value):
  value = 2

val = 1
change(val)

print(val)

def change2(value):
  value["name"] = "Syd"

val = {"name": "Beau"}
# A dictionary is mutable, so the function is going to change it
change2(val)

print(val)