import time

start = time.perf_counter()


def do_something():
    print("sleeping 1 sec...")
    time.sleep(1)
    print("done sleeping")


do_something()
do_something()

finish = time.perf_counter()

print(f"finished in {round(finish-start,2)} seconds(s)")
