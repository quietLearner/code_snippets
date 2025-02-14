import os
import subprocess
from pathlib import Path

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


script_location = Path(__file__).absolute().parent
file_location = script_location / "output.txt"


p1 = subprocess.run("dir", shell=True, capture_output=True, text=True)

print(p1.stdout)

p2 = subprocess.run(["dir"], capture_output=True, text=True, input=p1.stdout)

print(p2.stdout)
