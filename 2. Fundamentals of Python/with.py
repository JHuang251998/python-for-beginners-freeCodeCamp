filename = "test.txt"

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

# Using with automatically closes the file for us
# We don't need to close the file explicitly
with open(filename, 'r') as file:
    content = file.read()
    print(content)