import logging
from pathlib import Path

script_path = Path(__file__).resolve().parent
log_path = script_path / "test.log"

# logging levels

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(funcName)s:%(process)s:%(levelname)s:%(message)s",
    filemode="a",
)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.info("Div: {} / {} = {}".format(num_1, num_2, div_result))
