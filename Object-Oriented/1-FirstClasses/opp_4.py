import datetime


class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  # instance variable
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    # instance method
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # self is instance
    def apply_raise(self):
        # both are valid
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)

    # self is mandatory
    def hello(self):
        print("hello world")


emp_1 = Employee("Corey", "Schafer", 50000)

emp_1.hello()
