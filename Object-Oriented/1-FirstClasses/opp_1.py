# this is object here?
class Employee(object):
    print(object)


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# instance variables
# not efficient
emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "Employee"
emp_2.email = "Test.Employee@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
