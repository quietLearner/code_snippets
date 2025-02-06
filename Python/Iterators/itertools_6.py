from itertools import tee
from statistics import median

purchases = [1, 2, 3, 4, 5]  # list
purchases_1 = (1, 2, 3, 4, 5)  # tuple
purchases_2 = {1, 2, 3, 4, 5}  # set


# tee() takes an iterator and gives you two or more, allowing you to use the iterator passed into the function more than once:
def process_purchases(purchases):
    print(type(purchases))  # map
    min_, max_, avg = tee(purchases, 3)
    return min(min_), max(max_), median(avg)


# not working
def _process_purchases(purchases):
    return min(purchases), max(purchases), median(purchases)


# double = map(lambda n: n * 2, purchases)
# _process_purchases(double)
# ValueError: max() arg is an empty sequence

double = map(lambda n: n * 2, purchases)
print(process_purchases(double))

print(process_purchases(purchases_1))

print(process_purchases(purchases_2))
