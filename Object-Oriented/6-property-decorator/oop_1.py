class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@email.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Jim"

print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# print(emp_1.email())  # TypeError: 'str' object is not callable

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
