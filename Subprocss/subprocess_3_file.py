import os
import subprocess
from pathlib import Path

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


script_location = Path(__file__).absolute().parent
file_location = script_location / "output.txt"

with open(file_location, "w") as f:
    p1 = subprocess.run(["dir", "/L"], shell=True, stdout=f, text=True)

    # print(p1)
    # print(p1.args)
    print(p1.stdout)
