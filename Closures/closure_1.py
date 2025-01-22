# what is closure


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


# my_func is a closure function, even outer_func is executed, my_func still has access to the message variable
hello_func = outer_func("hello")
hi_func = outer_func("hi")
print(hello_func.__name__)
hi_func()
hello_func()
