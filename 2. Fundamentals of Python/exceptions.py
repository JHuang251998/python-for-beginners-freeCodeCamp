# try:
#     # Some lines of code
# except <ERROR1>:
#     # Handler <ERROR1>
# except <ERROR2>:
#     # Handler <ERROR2>
# except:
#     # Handler for all errors
# else:
#     # Run if no exceptions
# finally:
#     # Code to run at the end whether there are exceptions or not
#     # Always going to run

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    result = 1

print(result)

try:
    raise Exception("An error!")
except Exception as error:
    print(error)

class DogNotFoundException(Exception):
    # Use pass when define a class without methods or function without code
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")