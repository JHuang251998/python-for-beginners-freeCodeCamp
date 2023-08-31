numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

# Can be achieved by using map() as well
numbers_power_2 = list(map(lambda n : n**2, numbers))

print(numbers_power_2)