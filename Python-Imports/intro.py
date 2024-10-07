import sys

# not the best way to add path
sys.path.append("d:\\code_snippets\\Python-Imports\\modules")

print(sys.path)

# import my_module as mm

from my_module import find_index as fi, test


# from my_module import * dont do that

courses = ["History", "Math", "Physics", "CompSci"]

# index = mm.find_index(courses, "Math")
index = fi(courses, "History")

print(index)

print(test)

# this is  the path, where python will look for modules to import
print(sys.path)
