import datetime

a = [1, 2, 3, 4]
b = "sample string"

print(str(a))  # make it look nice, for user
print(repr(a))  # make it umambiguous, for developer

print(str(b))
print(repr(b))

now = datetime.datetime.now()
print(now)
print(str(now))
print(repr(now))
