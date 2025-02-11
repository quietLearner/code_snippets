# https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument


# https://web.archive.org/web/20200221224620id_/http://effbot.org/zone/default-values.htm
# list is mutable
# Default parameter values are always evaluated when, and only when, the “def” statement they belong to is executed; see:
def add_emp(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)


print(add_emp.__defaults__)

emps = ["john", "jane"]
add_emp("tom", emps)
print(emps)

add_emp("tim")
print(add_emp.__defaults__)
add_emp("dave")
print(add_emp.__defaults__)

print("*" * 50)


def add_emp_safe(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


print(add_emp_safe.__defaults__)  # (None,)
add_emp_safe("john")
print(add_emp_safe.__defaults__)  # (None,)
add_emp_safe("jane")
print(add_emp_safe.__defaults__)  # (None,)

import time
from datetime import datetime

print(datetime.now())
time.sleep(1)
print(datetime.now())
