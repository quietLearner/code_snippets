import itertools

letters = ["a", "b", "c", "d", "e", "f", "g"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

result = itertools.combinations(letters, 2)
# order does not matter, (a, b) is the same as (b, a)
for item in result:
    print(item)


result = itertools.permutations(letters, 2)
# order does matter
for item in result:
    print(item)


iterable = itertools.product(numbers, repeat=4)
for item in iterable:
    print(item)

iterable = itertools.combinations_with_replacement(numbers, 4)
for item in iterable:
    print(item)
