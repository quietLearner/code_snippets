nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

print([n for n in nums])

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n*n)
# print my_list

# Using a map + lambda(anonymous function)
my_list_1 = map(lambda n: n * n, nums)
print(list(my_list_1))


my_list_2 = [n * n for n in nums]
print(my_list_2)

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# print my_list

# Using a filter + lambda
my_list_3 = filter(lambda n: n % 2 == 0, nums)
print(list(my_list_3))


my_list_4 = [n for n in nums if n % 2 == 0]
print(my_list_4)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# print my_list

my_list_5 = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list_5)


# what is zip(), join 2 tuples together
a = ("John", "Charles", "Mike")
b = (
    "Jenny",
    "Christy",
)

x = zip(a, b)
print(list(x))

# Dictionary Comprehensions
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
print(list(zip(names, heros)))


# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict

# zip(iterator1, iterator2, iterator3 ...)
my_dict_1 = {name: hero for name, hero in zip(names, heros)}
print(my_dict_1)

# If name not equal to Peter
my_dict_2 = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict_2)

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set

my_set_1 = {n for n in nums}
print(my_set_1)


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_gen = (n * n for n in nums)

print(my_gen)

for i in my_gen:
    print(i)


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen_1 = gen_func(nums)

for i in my_gen_1:
    print(i)
