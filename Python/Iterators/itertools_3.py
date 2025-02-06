import itertools
import operator
from pathlib import Path

script_path = Path(__file__).resolve().parent
log_path = script_path / "employee.log"

letters = ["a", "b", "c", "d", "e", "f", "g"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

selectors = [True, True, False, True]

# chain() function is used to combine multiple iterables into one, without creating a new list
iterable = itertools.chain(letters, numbers, names)

for item in iterable:
    print(item)

iterable = itertools.islice(range(10), 2, 6, 2)
for item in iterable:
    print(item)

# get the first 3 lines of a file
with open(log_path, "r") as f:
    header = itertools.islice(f, 1, 4, 1)
    for line in header:
        print(line, end="")

# compress() function is used to filter an iterable based on another iterable of selectors
iterable = itertools.compress(letters, selectors)
for item in iterable:
    print(item)


print("*" * 50)

iterable = itertools.takewhile(lambda x: x > 0, [1, 4, -6, 0, 3, -7, 8])
for item in iterable:
    print(item)


def lt_2(n):
    if n < 2:
        return True
    return False


print("*" * 50)

iterable = itertools.filterfalse(lt_2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for item in iterable:
    print(item)

print(list(filter(lt_2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

# The dropwhile() function of Python returns an iterator only after the func. in argument returns false for the first time.
iterable = itertools.dropwhile(lambda x: x > 0, [1, 4, -6, 0, 3, -7, 8])
for item in iterable:
    print(item)

print("*" * 50)


for item in itertools.accumulate([1, 2, 3, 4, 5], operator.mul):
    print(item)
