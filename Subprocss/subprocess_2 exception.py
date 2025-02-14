import subprocess

p1 = subprocess.run(
    ["dir", "/L", "directory does not exist"],
    shell=True,
    # capture_output=True,
    stderr=subprocess.DEVNULL,
    # text=True,
    # check=True,
)

print(p1.returncode)
print(p1.stderr)
# print(p1.args)
print(p1.stdout)
