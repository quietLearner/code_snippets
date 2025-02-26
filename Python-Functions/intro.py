# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    # docstring - documentation string
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2017, 2))


# *args - tuple, positional arguments
# **kwargs - dictionary,key word arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info("Math", "Art", name="John", age=22)

courses = ("Math", "Art")
info = {"name": "John", "age": 22}

print(*courses)
print(*info)
# print(**info)

student_info(*courses, **info)


def hello_func(greeting, name="you"):
    return "{}, {}".format(greeting, name)


print(hello_func("hello"))
print(hello_func("hello", "Corey"))
