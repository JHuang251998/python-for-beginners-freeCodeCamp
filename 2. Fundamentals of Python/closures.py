def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1

    return count

  return increment

increment = counter()

# Inner function still has access to count variable even though counter() has ended
print(increment())
print(increment())
print(increment())
