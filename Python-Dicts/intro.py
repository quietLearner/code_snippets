# Dictionaries look like JSON
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"], 1: "one"}

for key, value in student.items():
    print(key, value)

# print(student["phone"]) # KeyError: 'phone'
# print(student["phone"])


print(student.get("phone", "Not Found"))

student["phone"] = "555-5555"

student.update({"name": "Jane", "age": 26, "phone": "555-5555"})

print(student)

# Delete
del student["age"]

print(student)

# Pop
# age = student.pop("age")

print(student)

# len
print(len(student))

# keys
print(student.keys())

# values
print(student.values())

# items
print(student.items())


# Iterate KEYS
for key in student:
    print(key)

# Iterate VALUES
for value in student.values():
    print(value)

# Iterate ITEMS
for key, value in student.items():
    print(key, value)
