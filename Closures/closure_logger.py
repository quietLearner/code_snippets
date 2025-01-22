import logging
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "example.log"


logging.basicConfig(filename=file_location, level=logging.INFO, filemode="a")


def logger(func):

    # take any number of args
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


log_add = logger(add)
log_add(3, 3)
log_add(4, 5)

log_sub = logger(sub)
log_sub(3, 3)
