import os
from pathlib import Path

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


script_location = Path(__file__).absolute().parent
file_location = script_location / "test.txt"
# file = file_location.open()


f_1 = open(file_location, "r")

print(f_1.name, f_1.mode)

f_1.close()

print(f_1.closed, f_1.mode)


# context manager, this is the preferred way to open files
with open(file_location, "r") as f:
    print(f.name, f.mode)
    f_contents = f.read(10)
    print(f_contents)

# this is cool
print(f.closed, f.mode)


with open(file_location, "r") as f:
    print(f.readline())
    print(f.readline())

    print(f.readline(), end="")

    print(f.readline(), end="")

with open(file_location, "r") as f:
    for line in f:
        print(line, end="")

with open(file_location, "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end="")
        f_contents = f.read(size_to_read)

print("\n")

with open(file_location, "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end="\n")

    print(f.tell())  # tell us where we are in the file

    f.seek(0)  # move the cursor to the beginning of the file

    print(f.read(size_to_read))

file_write = script_location / "test_2.txt"

with open(file_write, "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("R")


file_write_3 = script_location / "test_3.txt"


with open(file_location, "r") as rf, open(file_write_3, "w") as wf:
    wf.write(rf.read())

file_location_jpg = script_location / "dog.jpeg"

file_write_3 = script_location / "dog_copy.jpg"

with open(file_location_jpg, "rb") as rf, open(file_write_3, "wb") as wf:
    chunk_size = 4096
    rf_chunk = rf.read(chunk_size)

    while len(rf_chunk) > 0:
        wf.write(rf_chunk)
        rf_chunk = rf.read(chunk_size)
