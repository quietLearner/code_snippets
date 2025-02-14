import subprocess

subprocess.run("dir", shell=True)

# not safe to pass the command as string
subprocess.call("dir /L", shell=True)

subprocess.call(["dir", "/L"], shell=True)

# p1 = subprocess.run(["dir", "/L"], shell=True, capture_output=True, text=True)

p1 = subprocess.run(["dir", "/L"], shell=True, capture_output=True)


print(p1)
# print(p1.args)
print(p1.stdout)
print(p1.stdout.decode())
