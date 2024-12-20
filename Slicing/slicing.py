# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print(my_list[5])
print(my_list[-2])

# not inclusive, get everything except the last
print(my_list[0:9])
print(my_list[:9])
print(my_list[0:-1])  # if you dont know the end, use -1
print(my_list[:-1])

# get everything
print(my_list[:])


print(my_list[0::1])

# get every other item
print(my_list[::2])

#
print("my_list[2:-1:]", my_list[2:-1:])

# https://stackoverflow.com/questions/48792231/list-slicing-with-negative-step-size
# t starts counting from "2" going backwards (step -1) until "-1" is reached -
# but reaching the element "-1" would require positive step in this case., so the output is empty
print("my_list[2:-1:-1]", my_list[2:-1:-1])


print("my_list[-12:1:1]", my_list[-12:2:1])

print("my_list[-1:2:-1]", my_list[-1:2:-1])
# get the list in reverse
# https://www.pythonmorsels.com/slicing/#out-of-bounds-slicing-is-allowed
# Whenever a negative step value is given, the default meaning of start and stop change. With a negative step value,
# the start value will default to the last item in the list and the stop value will default to just before the beginning of the list.
print(my_list[::-1])

# start at the back and get every other item
print(my_list[::-2])

first_three = my_list[:3]
print(first_three)

last_three = my_list[-3:]
print(last_three)

all_but_first = my_list[1:]
print(all_but_first)
all_but_last = my_list[:-1]
print(all_but_last)

sample_url = "http://coreyms.com"
print(sample_url)

# Reverse the url
print(sample_url[::-1])

# Get the top level domain
print(sample_url[-4:])

# Print the url without the http://
print(sample_url[7:])

# Print the url without the http:// or the top level domain
print(sample_url[7:-4])
print(sample_url[7:-4])
