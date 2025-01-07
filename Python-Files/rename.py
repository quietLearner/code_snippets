import os
from pathlib import Path

os.chdir("d:/CODE_SNIPPETS/Python-Files")

print(os.getcwd())

f = script_location = (
    Path(__file__).absolute().parent / "earth - Our Solar System - #1.txt"
)


# for f in os.listdir():
f_name, f_ext = os.path.splitext(os.path.basename(f))
print(f_name, f_ext)

print(f_name.split("-"))

f_title, f_course, f_num = f_name.split("-")
f_title = f_title.strip()
f_course = f_course.strip()
f_num = f_num.strip()[1:].zfill(3)
new_name = f"{f_num}-{f_course}-{f_title}{f_ext}"
print(new_name)
# os.rename(f, new_name)
# print(f"Renamed {f} to {new_name}")
