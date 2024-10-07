# python arithmetic operators

# Addition: +
print(10 + 3)  # Outputs: 13

# Subtraction: -
print(10 - 3)  # Outputs: 7

# Multiplication: *
print(10 * 3)  # Outputs: 30

# Division: / (returns a float)
print(10 / 3)  # Outputs: 3.3333333333333335

# Modulus (remainder): %
print(10 % 3)  # Outputs: 1

# even or odd
print(10 % 2)  # Outputs: 0
print(10 % 2 == 0)  # Outputs: True
print(10 % 2 == 1)  # Outputs: False

# Exponentiation: **
print(10**3)  # Outputs: 1000

# Floor division: // (returns an integer)
print(10 // 3)  # Outputs: 3

# String to integer conversion
num_1 = "100"
num_2 = "200"

# Convert strings to integers
num_1 = int(num_1)
num_2 = int(num_2)

# Add the converted integers
print(num_1 + num_2)  # Outputs: 300

print(3 * 2 + 1)

# increment operator
x = 10
x = x + 3
x += 3
print(x)

# decrement operator
x = 10
x = x - 3
x -= 3  # x = x - 3
print(x)

# round function
print(round(2.984848, 3))

# absolute value
print(abs(-2.9))

# comparison operators
x = 3 > 2
print(x)

x = 3 >= 2
print(x)

x = 3 < 2
print(x)

x = 3 == 2
print(x)

x = 3 != 2
print(x)

# casting
x = "102"
y = int(x) + 1
print(y)
