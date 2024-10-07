greeting = 'Hel"lo'
name = "Michael"

a = """
    sdfjaksdf
sdfasdf asdfasd         djfasdjf;asdf

"""


print(greeting.lower())
print(greeting.upper())

# print(help)

# help(max)

# print(help(str.lower))

print(a)
print(len(a))

print(greeting[0])

# not included 4
print(greeting[1:4])

print(greeting[1:])

# not included 5
print(greeting[:5])

print(greeting.find("o"))

print(greeting.count("o"))

print(greeting.replace("o", "0"))

message = "{}, {}. Welcome!"

print(message.format(greeting, name))

message = f"{greeting}, {name}. Welcome!"

print(message)

message = r"Hello\nWorld"

print(message)

message = "Hello\nWorld"

print(message)

# print out all the methods available for the string
print(dir(message))

# print out all the methods available for the string
print(help(str.lower))
