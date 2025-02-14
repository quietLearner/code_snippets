import threading
import time

print(f"main thread {threading.current_thread().ident}")


def do_something():
    print(f"{threading.current_thread().ident} sleeping 1 sec...")
    time.sleep(1)
    print(f"{threading.current_thread().ident} done sleeping")


start = time.perf_counter()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# if we dont join the threads, the finish time makes no sense
t1.join()
t2.join()

finish = time.perf_counter()

print(
    f"{threading.current_thread().ident} finished in {round(finish-start,2)} seconds(s)"
)

"""
sleeping 1 sec...
sleeping 1 sec...
finished in 0.0 seconds(s)
done sleeping
done sleeping

"""
