import logging
from pathlib import Path

script_path = Path(__file__).resolve().parent
log_path = script_path / "employee_1.log"


logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(filename)s:%(name)s:%(process)s:%(thread)s:%(funcName)s:%(message)s",
    filemode="a",
)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info("Created Employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Corey", "Schafer")
emp_3 = Employee("Jane", "Doe")
