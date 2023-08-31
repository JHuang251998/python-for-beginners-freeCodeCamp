condition = True

while condition == True:
    print("The condition is true")
    condition = False

count = 0

while count < 10:
    print(count)
    count = count + 1

print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for index, item in enumerate(items):
    print(index, item)