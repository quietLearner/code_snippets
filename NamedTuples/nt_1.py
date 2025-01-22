from collections import namedtuple
from enum import Enum

# tuple unchangeable
color = (55, 155, 255)
print(color[0])  # what is color[0] 55

# dictionary, this is better than tuple? dictionary does not have dot notation
color = {"red": 55, "green": 155, "blue": 255}
print(color["red"])

# namedtuple, name is capitalized, immutable
RGB = namedtuple("RGB", ["red", "green", "blue"])
blue = RGB(0, 0, 255)
white = RGB(255, 255, 255)
red = RGB(255, 0, 0)


print(white.red)
print(red[1])


# enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3


print(Color.red)
print(Color["red"])
print(Color.red.name)
print(Color.red.value)
