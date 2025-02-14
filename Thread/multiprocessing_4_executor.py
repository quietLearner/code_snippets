import concurrent.futures
import multiprocessing
import os
import random
import time
from random import randrange, uniform

"""
this is why it's not working
https://stackoverflow.com/questions/68839960/why-multiprocessing-process-does-not-work-here


https://stackoverflow.com/questions/18114285/what-are-the-differences-between-the-threading-and-multiprocessing-modules
"""


def do_something(seconds):
    print(f"{os.getpid()} sleeping {seconds} sec...")
    time.sleep(seconds)
    return f"{os.getpid()} done sleeping {seconds} sec"


if __name__ == "__main__":
    print(f"with {multiprocessing.cpu_count()} cpus")
    print(f"main process {os.getpid()}")

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # fs = []
        # for _ in range(5):
        #     f = executor.submit(do_something, 1.3)
        #     fs.append(f)
        fs = [executor.submit(do_something, round(uniform(1, 3), 2)) for _ in range(20)]

        for f in concurrent.futures.as_completed(fs):
            print(f.result())

    finish = time.perf_counter()

    print(f"main process {os.getpid()} finished in {round(finish-start,2)} seconds(s)")
