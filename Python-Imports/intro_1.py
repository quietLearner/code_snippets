import random
import math
import datetime
import calendar
import os

import antigravity

courses = ["History", "Math", "Physics", "CompSci"]

random_course = random.choice(courses)

print(random_course)

rads = math.radians(90)

print(rads, math.sin(rads))


print(datetime.date.today())
print(calendar.isleap(2021))


print(os.getcwd())

# __file__ is the module itselfs
print(os.__file__)

antigravity.geohash()
