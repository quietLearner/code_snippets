import concurrent.futures
import threading
import time

print(f"main thread {threading.current_thread().ident}")


def do_something(seconds):
    print(f"{threading.current_thread().ident} sleeping {seconds} seconds(s)...")
    time.sleep(seconds)
    return f"{threading.current_thread().ident} done sleeping {seconds} seconds(s)"


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # this is wrong, the order is sequential. not parallel
    # for _ in range(10):
    #     f1 = executor.submit(do_something, 1.3)
    #     print(f1.result())

    # also wrong way?
    # f1 = executor.submit(do_something, 1.2)
    # print(f1.result())

    # f2 = executor.submit(do_something, 1.2)
    # print(f2.result())

    secs = [2, 5, 3, 1.5, 2.1]

    fs = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(fs):
        print(f.result())


# no need to join threads

finish = time.perf_counter()

print(
    f"{threading.current_thread().ident} finished in {round(finish-start,2)} seconds(s)"
)
