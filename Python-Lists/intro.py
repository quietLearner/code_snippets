# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()

courses = ["History", "Math", "Physics", "CompSci"]

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])  # Last item
print(courses[-2])  # Second last item

print(courses[0:2])  # Slicing, not including the end index
print(courses[2:])  # From index 2 to the end
print(courses[:2])  # From start to index 2

# Adding elements to the list
courses.append("Art")
print(courses)

# Inserting elements to the list
courses.insert(0, "Art")
print(courses)

courses2 = ["Education", "Society"]

# Extending the list
courses.extend(courses2)
print(courses)


# courses.insert(0, *courses2), not working
# print(courses)

# Removing elements from the list
courses.remove("Math")
print(courses)

# Removing elements from the end of the list
popped = courses.pop()
print(popped)
print(courses)

# Removing elements from the list by index
courses.pop(0)
print(courses)

# Reversing the list
courses.reverse()
print(courses)

# Sorting the list
courses.sort()
print(courses)

# Sorting the list in reverse order
courses.sort(reverse=True)
print(courses)

# Sorting the list in reverse order
nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

# Sorting without changing the original list
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

# Finding the index of an element
print(courses.index("CompSci"))

# Checking if an element exists in the list
print("Math" in courses)

nums = [1, 5, 2, 4, 3]

print(min(nums))
print(max(nums))
print(sum(nums))

# Finding the index of an element
print(courses.index("CompSci"))

# Counting the number of elements in the list
print(courses.count("CompSci"))

# Converting the list to a string
course_str = " - ".join(courses)
print(course_str)

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

# Enumerate with start
for index, course in enumerate(courses, start=1):
    print(index, course)
