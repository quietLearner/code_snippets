# what is first class function?
# 1. A function is an instance of the Object type.
# 2. You can store the function in a variable.
# 3. You can pass the function as a parameter to another function.
# 4. You can return the function from a function.
# 5. You can store them in data structures such as hash tables, lists, …


# Example 1: Functions are objects
def square(x):
    return x * x


def cube(x):
    return x * x * x


fn = square

print(fn(6))

f = square(5)
print(square)
print(f)


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


r = my_map(square, [1, 2, 3, 4, 5])
print(r)


# Example 2: Functions can be passed as arguments to other functions
# what's the point, why is this useful?
def logger(msg):
    # This is a closure function
    def log_message():
        print("Log:", msg)

    return log_message


# log_hi is a function
log_hi = logger("Hi!")
log_hi()


# this is why it's useful
def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text


# this example is a closure function and a first class function
print_h1 = html_tag("h1")
print_h1("Test Headline!")
print_h1("Another Headline!")

print_p = html_tag("p")
print_p("Test Paragraph!")
print_p("Another Paragraph!")
