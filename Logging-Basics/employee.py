import logging
from pathlib import Path

script_path = Path(__file__).resolve().parent
log_path = script_path / "employee.log"

formatter = logging.Formatter(
    "%(asctime)s:%(levelname)s:%(filename)s:%(name)s:%(process)s:%(thread)s:%(funcName)s:%(message)s"
)
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("Created Employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        return result


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Corey", "Schafer")
emp_3 = Employee("Jane", "Doe")

divide(1, 1)
divide(10, 0)
