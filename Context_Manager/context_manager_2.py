from pathlib import Path
from contextlib import contextmanager

script_location = Path(__file__).absolute().parent
file_location = script_location / "sample.txt"


@contextmanager
def open_file(file_location, mode):
    try:
        f = open(file_location, mode)
        yield f
    finally:
        f.close()


with open_file(file_location, "w") as f:
    f.write("Lorem ipsum")  # This will write to the file

print(f.closed)  # This will return True
