from itertools import tee
from statistics import median

purchases = [1, 2, 3, 4, 5]


def process_purchases(purchases):
    min_, max_, avg = tee(purchases, 3)
    return min(min_), max(max_), median(avg)


def _process_purchases(purchases):
    return min(purchases), max(purchases), median(purchases)


# double = map(lambda n: n * 2, purchases)
# _process_purchases(double)
# ValueError: max() arg is an empty sequence

double = map(lambda n: n * 2, purchases)
min, max, median = process_purchases(double)
print(min, max, median)
