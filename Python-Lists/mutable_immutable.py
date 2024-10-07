# Mutable, list is mutable
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = "Art"

# Both lists are updated because list_2 is a reference to list_1
print(list_1)
print(list_2)

# Immutable, tuple is immutable
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)


# tuple_1[0] = "Art" # TypeError: 'tuple' object does not support item assignment

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}

print(cs_courses)

print("Math" in cs_courses)

art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()
