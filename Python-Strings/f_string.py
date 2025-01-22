first_name = "John"
last_name = "Doe"

setence = f"my name is {first_name.lower()} {last_name.lower()}"

print(setence)


person = {"name": "Jenn", "age": 23}

setence = f"my name is {person['name']} and I am {person['age']} years old"

print(setence)

# https://stackoverflow.com/questions/339007/how-do-i-pad-a-string-with-zeros
# https://docs.python.org/3/library/string.html#format-string-syntax
for n in range(1, 11):
    print(f"The value is {n:03}")

pi = 3.14159265

setence = f"Pi is equal to {pi:.4f}"

print(setence)

from datetime import datetime

birthday = datetime(1990, 1, 1)

# https://docs.python.org/3/library/datetime.html#format-codes
setence = f"Jenn has a birthday on {birthday:%B %d, %Y}"
print(setence)
