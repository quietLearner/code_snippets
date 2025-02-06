import itertools
import operator
from pathlib import Path


people = [
    {"name": "John Doe", "city": "Gotham", "state": "NY"},
    {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
    {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
    {"name": "Al Einstein", "city": "Denver", "state": "CO"},
    {"name": "John Henry", "city": "Hinton", "state": "WV"},
    {"name": "Randy Moss", "city": "Rand", "state": "WV"},
    {"name": "Nicole K", "city": "Asheville", "state": "NC"},
    {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
    {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
]


def get_state(person):
    return person["state"]


# groupby() function is used to group the elements of an iterable based on some key and return a dictionary of the groups
# The key is a function computing a key value for each element.
# If not specified or is None, key defaults to an identity function and returns the element unchanged.
# Generally, the iterable needs to already be sorted on the same key function.
# The returned group is itself an iterator that shares the underlying iterable with groupby().
# Because the source is shared, when the groupby() object is advanced, the previous group is no longer visible.
# So, if that data is needed later, it should be stored as a list.

people.sort(key=get_state)
person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()

print("*" * 50)

iter1, iter2 = itertools.tee(person_group, 2)

for key, group in iter1:
    print(key)
    for person in group:
        print(person)
    print()

print("*" * 50)


for key, group in iter2:
    print(key)
    for person in group:
        print(person)
    print()

iterator1, iterator2 = itertools.tee([1, 2, 3, 4, 5, 6, 7], 2)

for i in iterator1:
    print(i)

print("*" * 50)


for i in iterator2:
    print(i)
