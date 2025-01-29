from pathlib import Path
from contextlib import contextmanager

script_location = Path(__file__).absolute().parent
file_location = script_location / "sample.txt"


class Open_File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


print(dir(Open_File))

with Open_File(file_location, "w") as f:
    f.write("Testing")  # This will write to the file

print(f.closed)  # This will return True
