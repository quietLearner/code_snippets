import os
from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent

print(os.getcwd())

print(Path.cwd())

# current file path
print(Path(__file__).resolve())


print(Path(__file__).resolve().parent)

print(Path(__file__).resolve().parent.parent)


print("Path()", Path())

# dont understand this
# for p in Path().iterdir():
#     print(p)


my_dir = Path("PATHLIB")
my_file = Path("file_1.txt")

print(my_dir.suffix, my_dir.stem)
print(my_file.suffix, my_file.stem)

print(os.path.join(my_dir, "media.txt"))

new_file = my_dir / "media.txt"
new_file = my_dir.joinpath("media.txt")
print(new_file, new_file.exists())


print(my_dir.parent)
print(my_file.parents[0])
print(new_file.parent.parent)

print(my_dir.absolute().parent.parent)
print(my_file.parent.absolute())

print(my_dir.resolve())
print(my_dir.absolute())

# D:\code_snippets\..
print(Path("..").absolute())

# d:\, we warnt parent of the current directory
print(Path("..").resolve())

# D:\code_snippets, why the current directory is not D:\code_snippets\PATHLIB???
print(Path.cwd(), os.getcwd())

# https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory

# get current working directory
print(Path.cwd())

# To get an absolute path to your script file,
print(Path(__file__).resolve())

# to get the path of a directory where the script is located
print(Path(__file__).resolve().parent)

# to get current user home directory
print(Path.home())  # C:\Users\dtw20

print(Path("~").expanduser())  # C:\Users\dtw20

# not working
print(Path("~").resolve())  # D:\code_snippets\~

# C:\Users\dtw20\abc
print(Path("~/abc").expanduser())
print(Path.home().joinpath("abc"))

# all the subdirectories and files in the current directory
for p in Path.cwd().glob("**/*.py"):
    print(p)

file = Path.cwd() / "Str_Repr" / "test.py"

with file.open() as f:
    print(f.read())

# with open(file, "r") as f:
#     print(f.read())


# create a new directory
new_dir = Path.cwd() / "temp_dir/sub_dir"

new_dir.mkdir(exist_ok=True, parents=True)

# remove empty directory
# new_dir.rmdir()

new_file = Path.cwd() / "temp_dir" / "temp_file.txt"
new_file.touch()

# replace will create a new file, if the file already exists, without any warning
new_file = new_file.replace(Path.cwd() / "temp_dir" / "temp_file_1.txt")

new_file.unlink()
