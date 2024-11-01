import sys

# not the best way to add module path
sys.path.append("d:\\code_snippets\\Python-Imports\\modules")

# in windows https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages


# this is the path, where python will look for modules to import
print(sys.path)

# import my_module as mm

from my_module import find_index as fi, test

# dont do that, because we have hard time to know where the funtions come from
# from my_module import *

courses = ["History", "Math", "Physics", "CompSci"]

# index = mm.find_index(courses, "Math")
index = fi(courses, "History")

print("find history", index)

print(test)
