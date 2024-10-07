def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)


def square_numbers_generator(nums):
    for i in nums:
        yield (i * i)  # yield is a return statement that returns a generator


my_nums = square_numbers_generator([1, 2, 3, 4, 5])

# because it's a generator, it's not stored in memory, it's stored in a special object that generates values on the fly
print(my_nums)  # <generator object square_numbers_generator at 0x0000022B1778F9D0>

print(next(my_nums))  # 1

print("*" * 20)

for num in my_nums:  # it start from 4, not 1
    print(num)

for num in my_nums:
    print(num)

print("*" * 20)


# list comprehension
my_nums = [x * x for x in [1, 2, 3, 4, 5]]
print(my_nums)

# generator expression, replace the square brackets with parentheses
my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(list(my_nums), "lol")

# generator expression is more memory efficient than list comprehension
# it wont print, because it only generate once
for num in my_nums:
    print(num)

# print(next(my_nums))  # won't work, it only generate once
