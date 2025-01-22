import random
import time

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
majors = ["Math", "Engineering", "CompSci", "Arts", "Business"]


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        yield person


t1 = time.time()
people = people_list(10_000_000)
t2 = time.time()

print("list ook {} Seconds".format(t2 - t1))

t1 = time.time()
people = people_generator(10_000_000)
t2 = time.time()

print("generator took {} Seconds".format(t2 - t1))
