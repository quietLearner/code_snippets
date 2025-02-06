s1 = set([1, 2, 3, 4, 5])
s2 = {4, 5, 6, 7, 8}

s3 = {}  # This is not a set, it is a dictionary, becareful!
print(type(s3))  # <class 'dict'>

s4 = set()  # This is an empty set
print(type(s4))  # <class 'set'>

print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2))  # {4, 5}
print(s1.difference(s2))  # {1, 2, 3}
print(s1.symmetric_difference(s2))  # {1, 2, 3, 6, 7, 8}
print(s1.issubset(s2))  # False
print(s1.issuperset(s2))  # False
print(s1.isdisjoint(s2))  # False

s1.update(s2)

print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8}

s1.remove(8)
print(s1)  # {1, 2, 3, 4, 5, 6, 7}

s1.discard(7)
print(s1)  # {1, 2, 3, 4, 5, 6}


s1.pop()
print(s1)  # {2, 3, 4, 5, 6}
