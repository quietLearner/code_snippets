person = {"name": "John", "age": 25, "job": "Developer"}
person = {"name": "Jess", "age": 23}

# look before you leap

# LBYL look before you leap
if "name" in person and "job" in person and "age" in person:
    print(person["name"])
    print(person["job"])
else:
    print("Missing Key")

# EAFP
try:
    print("I'm {name}, I'm a {job} and I'm {age} years old".format(**person))
except KeyError as e:
    print(f"Missing Key: {e}")
except Exception as e:
    print(f"Error: {e}")

my_list = [1, 2, 3, 4, 5]

# not pythonic
if len(my_list) > 10:
    print(my_list[10])
else:
    print("Index Error")

# pythonic
try:
    print(my_list[10])
except IndexError as e:
    print(f"Index Error: {e}")
