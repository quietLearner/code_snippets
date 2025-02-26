class Employee:

    raise_amt = 1.04

    # special method, Dunder Methods, dunder” is the short for “double underscores"
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # used for debugging and logging, at least has this method, used by other developers?
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # used for display to end user, if not defined, __repr__ will be used
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)

# print(emp_1 + emp_2)

print(len(emp_1))

print("test".__len__())

print(repr(emp_1))
print(str(emp_2))
print(emp_2)

print(emp_1.__repr__())
print(emp_1.__str__())

# the following two lines are the same
print(1 + 2)
print(int.__add__(1, 2))

print(str.__add__("a", "b"))

# the following two lines are the same
print(emp_1 + emp_2)
print(emp_1.__add__(emp_2))

print(len("test"))
print(len(emp_1))
