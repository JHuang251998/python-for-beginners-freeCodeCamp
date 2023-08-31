def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)

talk('I am going to buy the milk')

def count():
  count = 1

  def increment():
    nonlocal count
    count = count + 1
    print(count)

  increment()

count()