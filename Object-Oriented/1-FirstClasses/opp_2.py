# this is a function, not method
def func():
    pass


class Employee:
    # class variable is shared among all instances of a class
    num_of_emps = 0
    raise_amount = 1.04
    hi = "hi_class_variable"

    # constructor
    def __init__(self, first, last, pay):
        self.first = first  # instance variable
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1  # this is a class variable, do not use self, use class name, otherwise it will be an instance variable
        self.hi = "hi_instance_variable"

    # this is a method, because it has self as the first argument, also self is mandatory
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # both are valid
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)

print(emp_1.num_of_emps)  # 2
print(emp_2.num_of_emps)  # 2
print(Employee.num_of_emps)  # 2


print("before raise:", emp_1.pay)  # 50000
emp_1.apply_raise()
print("after rainse:", emp_1.pay)  # 52000


# there is no raise_amount in emp_1, so it will look for raise_amount in the class
# {'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com', 'hi': 'hi_instance_variable'}
print(emp_1.__dict__)

print(Employee.__dict__)

# {'__module__': '__main__', 'num_of_emps': 2, 'raise_amount': 1.04, 'hi': 'hi_class_variable', '__init__': <function Employee.__init__ at 0x00000269B70E9F80>, 'fullname': <function Employee.fullname at 0x00000269B70EA020>, 'apply_raise': <function Employee.apply_raise at 0x00000269B70EA0C0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
emp_1.num_of_emps = (
    5  # we are not changing the class variable, we are creating a new instance variable
)

# {'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com', 'hi': 'hi_instance_variable', 'num_of_emps': 5}
print(emp_1.__dict__)

print(emp_1.num_of_emps)  # 5

del emp_1.num_of_emps  # this will delete the instance variable, not the class variable

# {'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com', 'hi': 'hi_instance_variable'}
print(emp_1.__dict__)

print(emp_1.num_of_emps)  # 2
print(emp_2.num_of_emps)  # 2
print(Employee.num_of_emps)  # 2

emp_1.hello = "hello"  # this is a new instance variable for emp_1
print(emp_1.hello)  # hello

print(emp_1.hi)  # hi_instance_variable
print(Employee.hi)  # hi_class_variable
emp_1.hi = "hi_instance_variable_changed"
print(emp_1.hi)  # hi_instance_variable_changed
print(Employee.hi)  # hi_class_variable
del emp_1.hi

# {'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com', 'num_of_emps': 5, 'hello': 'hello'}
print(emp_1.__dict__)


# del emp_1.first
# print(emp_1.first)  # AttributeError: 'Employee' object has no attribute 'first'


print(emp_1.fullname())  # "Corey Schafer"
# this is equivalent to, emp_1 is the first argument(self)
print(Employee.fullname(emp_1))  # "Corey Schafer"
