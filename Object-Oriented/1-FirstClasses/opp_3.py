import datetime


class Employee:
    # class variable is shared among all instances of a class
    num_of_emps = 0
    raise_amount = 1.04

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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # cls is Employee
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor, look into datetime module for more examples
    @classmethod
    def create_instance(cls, emp_str):
        first, last, pay = emp_str.split("-")
        # Employee("Corey", "Schafer", 50000) is the same as cls(first, last, pay)!!
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)


Employee.set_raise_amount(1.05)


Employee.raise_amount = 1.06


emp_1.set_raise_amount(1.07)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

first, last, pay = emp_str_1.split("-")

new_emp_1 = Employee(first, last, pay)

print(new_emp_1)

new_emp_2 = Employee.create_instance(emp_str_2)

print(new_emp_2)


my_date = datetime.date(2024, 7, 10)

print(Employee.is_workday(my_date))
