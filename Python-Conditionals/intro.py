condition = "Test"

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print(id(a))
print(id(b))


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

# condition = False

# condition = None

# condition = 0

# condition = ()

# condition = ""

# condition = {}

condition = []


if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
