"""
LEGB
Local, Enclosing, Global, Built-in
checking order of execution
"""

import builtins

print(dir(builtins))


# because it's in the main body of the file
x = "global x"


def test(z):
    # don't use this way... not recommended in my opinion
    # global x

    x = "local x"
    y = "local y"
    print(y)
    print(x)


test("local z")
print(x)


# python does not prevent us overwriting built-in functions
def my_min():
    pass


# min is a built-in function in python, it's in the builtins module
m = min([5, 1, 3, 2, 4])
print(m)


for a in range(2):
    x = "global {}".format(a)


# enclosing
def outer():
    x = "outer x"
    for b in range(3):
        x = "outer {}".format(b)

    def inner():
        # this is change the value of x in the enclosing scope, not in the global scope
        # nonlocal x

        x = "inner x"
        for c in range(4):
            x = "inner {}".format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)


outer()
print(x)
print(a)
