from enum import Enum


# Parentheses after class definition indicate inheritance
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE.value)
