import datetime
import getpass
import math
import os

import requests


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        print("Created Employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("John", "Smith")

name = input("your name?")
password = getpass.getpass("your password?")

print(name, password)