from datetime import datetime
import os

# print(dir(os))

# get current working directory
print(os.getcwd())


os.chdir("d:/1/")

# print(os.listdir())

print(os.getcwd())

print(os.listdir())

if not os.path.isdir("test2/test3"):
    os.makedirs("test2/test3")

# remove directories
# os.removedirs("test2/test3/")

# only removes the last directory
os.rmdir("test2/test3")

if not os.path.isdir("test22"):
    os.rename("test2", "test22")

print(os.stat("test22"))

print(datetime.fromtimestamp(os.stat("test22").st_mtime))

for dirpath, dirname, filename in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirname)
    print("Files: ", filename)
    print()

# print(os.environ)

print(os.environ.get("HOME"))

file_path = os.path.join(os.getcwd(), "test.txt")
print(file_path)

print(os.path.basename("/tmp/test.txt"))

print(os.path.dirname("/tmp/test.txt"))

print(os.path.split("/tmp/2/3/test.txt"))


print(os.path.split("/tmp/2/3/"))

print(os.path.exists("/tmp/2/3/"))

print(os.path.isdir("/tmp/2/3/"))
print(os.path.isfile("/tmp/2/3/"))

print(os.path.splitext("/tmp/2/3/test.txt"))
