from pathlib import Path
import time
import logging
from functools import wraps


def my_logger(orig_func):

    script_location = Path(__file__).absolute().parent

    file_location = script_location / f"{orig_func.__name__}.log"

    logging.basicConfig(filename=file_location, level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")


display_info("Tom", 22)
display_info("Jerry", 23)


# this is equivalent to the following:
# @my_logger
# @my_timer
# display_info = my_logger(my_timer(display_info))

# display_info = my_timer(display_info)
# print(display_info.__name__)
# # this will print wrapper
