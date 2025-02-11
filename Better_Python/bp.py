x = 1 if True else 2

num1 = 1_000_000_000_000_000
num2 = 100_000_000_000

total = num1 + num2

print(f"{total:,}")


from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "bp.py"

with open(file_location, "r") as f:
    f_contents = f.read()

words = f_contents.split(" ")
word_count = len(words)
print(word_count)

name = ["John", "Doe"]

for i, n in enumerate(name, start=1):
    print(i, n)


name = ["John", "Doe", "Jane", "Smith", "David"]
heros = ["Spiderman", "Superman", "Batman", "Wonder Womna"]
universe = ["Marvel", "DC", "DC", "DC"]
for n, h, u in zip(name, heros, universe):
    print(f"{n} is actually {h} from {u}")

# unpacking
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c, type(c))

# if you dont care the  rest
a, _ = (1, 2)
print(a)

# this will throw exception
# a, b, c = (1, 2)

a, b, *c, d = (1, 2, 3)
print(a, b, c, d)


class Person:
    pass


person = Person()

person.firstname = "zhang"
person.lastname = "san"

first_key = "first"
first_val = "li 4"

setattr(person, first_key, first_val)

first = getattr(person, first_key)

print(first)

print(person)


person_info = {"age": 20, "address": "shanghai"}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

from datetime import datetime

print(dir(datetime))

print(dir(datetime.today))

print(datetime.today)
