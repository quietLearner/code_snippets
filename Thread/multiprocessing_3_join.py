import multiprocessing
import time

"""
this is why it's not working
https://stackoverflow.com/questions/68839960/why-multiprocessing-process-does-not-work-here


https://stackoverflow.com/questions/18114285/what-are-the-differences-between-the-threading-and-multiprocessing-modules
"""


def do_something():
    print("sleeping 1 sec...")
    time.sleep(1)
    print("done sleeping")


if __name__ == "__main__":
    start = time.perf_counter()

    ps = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    finish = time.perf_counter()

    print(f"finished in {round(finish-start,2)} seconds(s)")
