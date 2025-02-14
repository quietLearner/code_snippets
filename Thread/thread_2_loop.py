import threading
import time

print(f"main thread {threading.current_thread().ident}")


def do_something(seconds):
    print(f"{threading.current_thread().ident} sleeping {seconds} seconds(s)...")
    time.sleep(seconds)
    print(f"{threading.current_thread().ident} done sleeping {seconds} seconds(s)")


start = time.perf_counter()

threads = []

for _ in range(5):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

# https://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-threading
# if we dont join the threads, the finish time makes no sense
# You could say join is (only) relevant for the execution-flow of the main-thread.
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(
    f"{threading.current_thread().ident} finished in {round(finish-start,2)} seconds(s)"
)

"""
main thread 12920
6708 sleeping 1.5 seconds(s)... 
11824 sleeping 1.5 seconds(s)...
13452 sleeping 1.5 seconds(s)...
10480 sleeping 1.5 seconds(s)...
15712 sleeping 1.5 seconds(s)...
6708 done sleeping 1.5 seconds(s)
13452 done sleeping 1.5 seconds(s)
11824 done sleeping 1.5 seconds(s)
15712 done sleeping 1.5 seconds(s)
10480 done sleeping 1.5 seconds(s)
12920 finished in 1.5 seconds(s) 

"""
