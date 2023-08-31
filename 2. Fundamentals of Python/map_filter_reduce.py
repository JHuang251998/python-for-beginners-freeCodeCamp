# map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5, 6]

def double(a):
    return a * 2

result = map(double, numbers)
result2 = map(lambda a : a * 2, numbers)

print(list(result))
print(list(result2))

def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)
result2 = filter(lambda n : n % 2 == 0, numbers)

print(list(result))
print(list(result2))

from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]

# a = accumulated value, b = element in iterable
sum2 = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum)
print(sum2)
