class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # so this is wrong, because it will not update the email if first or last name is changed after the object is created
        # we can use a method to get the email, but it is better to use a property decorator
        # self.email = first + "." + last + "@email.com"

    # call this without parenthesis, not as a method
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        pass

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.getter
    def fullname(self):
        return "getter {} {}".format(self.first, self.last)

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

# print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# print(emp_1.email())  # TypeError: 'str' object is not callable

del emp_1.fullname

# print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
