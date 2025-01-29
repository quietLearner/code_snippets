from pathlib import Path
from contextlib import contextmanager
import os

print(os.getcwd())

script_location = Path(__file__).absolute().parent


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)  # change back to the original directory


with change_dir(script_location):
    print(os.getcwd())
    print(os.listdir())  # This will print the files in the directory

print(os.getcwd())
