import subprocess

p1 = subprocess.run(["dir", "/L"], shell=True, stdout=subprocess.PIPE, text=True)

# print(p1)
# print(p1.args)
print(p1.stdout)
