li = [9, 1, 8, 2, 7, 3, 6, 4, 5, 0]

s_li = sorted(li, reverse=True)

print("sorted:\t", s_li)
print("original:\t", li)

li.sort(reverse=True)

print("sorted:\t", li)
print("original:\t", li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5, 0)
s_tup = sorted(tup, reverse=True)

print("sorted:\t", s_tup)
print("original:\t", tup)


di = {"name": "Corey", "job": "Programmer", "age": 28, "os": "Mac"}

s_di = sorted(di)

# odd, sorts by key, and only return keys
print("sorted:\t", s_di)  # ['age', 'job', 'name', 'os']
print("original:\t", di)


li_1 = [-6, -5, -4, 8, 9, 1, 4, -1]
# s_li_1 = sorted(li_1, key=abs)
s_li_1 = sorted(li_1, key=lambda x: abs(x))
print("sorted:\t", s_li_1)
print("original:\t", li_1)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return "Employee({}, ${})".format(self.name, self.salary)


employees = [
    Employee("Tim", 50000),
    Employee("Jane", 60000),
    Employee("John", 70000),
    Employee("John", 20000),
    Employee("Bob", 40000),
]

s_employees = sorted(employees, key=lambda x: x.salary)
print("sorted:\t", s_employees)
print("original:\t", employees)  # Not sorted


# sort by name, then salary
def e_sort(emp):
    return (emp.name, emp.salary)


# sort by name, then salary reversed
def e_sort(emp):
    return (emp.name, -emp.salary)


s_employees = sorted(employees, key=e_sort)
print("sorted:\t", s_employees)
print("original:\t", employees)

from operator import attrgetter

s_employees = sorted(employees, key=attrgetter("name", "salary"))
print("sorted:\t", s_employees)
print("original:\t", employees)
