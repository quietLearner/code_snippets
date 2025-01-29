import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()

# c.execute(
#     """CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )"""
# )


def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


emp_1 = Employee("John", "Doe", 80000)

insert_emp(emp_1)
conn.commit()


c.execute("select * from employees")

print(c.fetchone())

print(c.fetchall())

conn.close()
