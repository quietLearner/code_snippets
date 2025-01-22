# what is decorator?
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


def my_decorator(original_func):
    def wrap_func():
        print("********")
        original_func()
        print("********")

    return wrap_func


def my_decorator_2(original_func):

    def wrap_func(*args, **kwargs):
        print("********")
        original_func(*args, **kwargs)
        print("********")

    return wrap_func


def hello():
    print("hello")


# @my_decorator is just a syntactic sugar, shorthand for hello = my_decorator(hello)
decorated = my_decorator(hello)
decorated()


@my_decorator
def hi():
    print("hi")


hi()


@my_decorator_2
# @my_decorator takes 0 positional arguments but 2 were given
def show_info(name, age):
    print(f"Name: {name}, Age: {age}")


show_info("Jerry", 30)
