"""
== checks for equality

is checks for identity

"""

print("coke" == "pepsi")  # false

print("pepsi" == "pepsi")  # true

print("pepsi" is "pepsi")  # true

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]

print(l1 == l2)  # true

print(l1 is l2)  # false

print(id(l1), id(l2))
