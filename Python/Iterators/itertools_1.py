import itertools

counter = itertools.count(start=3, step=-2.5)

print(next(counter))

data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))
print(daily_data)


daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

counter = itertools.cycle([1, 2, 3])

for i in range(10):
    print(next(counter))

iter_counter = itertools.repeat(200, times=3)

for i in iter_counter:
    print(i)


square = map(pow, range(10), itertools.repeat(2))
print(list(square))


result = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)])

print(list(result))
