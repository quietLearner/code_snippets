import multiprocessing
import os
import time

"""
this is why it's not working
https://stackoverflow.com/questions/68839960/why-multiprocessing-process-does-not-work-here


https://stackoverflow.com/questions/18114285/what-are-the-differences-between-the-threading-and-multiprocessing-modules
"""


def do_something(seconds):
    print(f"{os.getpid()} sleeping {seconds} sec...")
    time.sleep(seconds)
    print(f"{os.getpid()} done sleeping {seconds} sec")


if __name__ == "__main__":
    print(f"main process {os.getpid()}")

    start = time.perf_counter()

    ps = []
    for _ in range(5):
        p = multiprocessing.Process(target=do_something, args=[2.5])
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    finish = time.perf_counter()

    print(f"main process {os.getpid()} finished in {round(finish-start,2)} seconds(s)")
