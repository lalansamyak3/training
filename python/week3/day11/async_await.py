import time


def fetch_user():
    time.sleep(1)
    return "user"


def fetch_order():
    time.sleep(1)
    return "order"


start = time.perf_counter()
fetch_user()
fetch_order()
end = time.perf_counter()
print(f"Total time taken: {end-start} seconds")

"""normally sync methods will take time to execute but if we use async await it will take less time to execute because it will not wait for the first function to complete before starting the second function. It will run both functions concurrently."""
"""sync methods cannot start other process untill the first is completed so first methods takes 1 second then return user then second method again dont do anything for 1 sec then start return the oders
sync methiods like ly takes lkonger as to fetch data in db waiting for the response after calling an api it cannot start the other process
"""


from threading import Thread


def count():
    n = 0
    for i in range(300000):
        n = n + 1


start = time.perf_counter()
count()
count()
end = time.perf_counter()
print(f"Total time taken: {end-start} seconds")
"""without therading it will take more time to excecute because it will wait for the first function to complete before starting the second function. It will run both functions sequentially."""


start = time.perf_counter()
t1 = Thread(target=count)
t2 = Thread(target=count)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.perf_counter()
print(f"Total time taken: {end-start} seconds")
"""with therading it will take less time as it will not wait for the first function to complete before starting the second function. It will run both functions concurrently."""
"""thread dont work for cpu bound exceuting the fucntion we can see both are tajking the same time with or withot thread """
"""thread only helps in input output bounds likej api calling response,db queries etc"""


# input output bpunding
"""async await is used for input output bound tasks like api calling, db queries etc.
 It will not wait for the first function to complete before starting the second function.
 It will run both functions concurrently."""
"""because oif gil cpu bound wwith or without thread will same time but
 input output bound like caling api ,db queries will take less time as gil switches as
   one relases gil so other can run so it will take less time to excecute with thread or async await
"""

import time
from threading import Thread


def wait():
    time.sleep(1)


# Without threads
start = time.perf_counter()
wait()
wait()
print(f"no threads: {time.perf_counter() - start:.2f}s")  # ~2s

# With threads
start = time.perf_counter()
t1, t2 = Thread(target=wait), Thread(target=wait)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"2 threads:  {time.perf_counter() - start:.2f}s")  # ~1s
# run and see the diff now


# thread implementation
import threading
import time


def worker(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} done")


t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()
t1.join()  # wait for t1 to finish
t2.join()  # wait for t2 to finish
print("all done")  # ~1s total, not 2s


"""Thread pool excecutor allows you to run multiple threads concurrently and manage them easily.
It is a high-level interface for asynchronously executing callables."""
import time
from concurrent.futures import ThreadPoolExecutor


def fetch(n):
    time.sleep(1)  # pretend network call
    return n * 10


start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, [1, 2, 3, 4, 5, 6]))


print(results)  # [10, 20, 30, 40, 50, 60] in ~2s
end = time.perf_counter()
print(end - start)
"""10,20,30 IN 1 SEC THEN 40,50,60 IN ONE SEC SO TAOTAL IS 2 SEC """
"""3 WORKER FOR 6 TASK IF WE HAVE 6 THREAD IT MIGHT GAVE TAKEN  6 SECONDS """
strat = time.perf_counter()
T1 = Thread(target=fetch, args=(1,))
T2 = Thread(target=fetch, args=(2,))
T3 = Thread(target=fetch, args=(3,))
T4 = Thread(target=fetch, args=(4,))
T5 = Thread(target=fetch, args=(5,))
T1.start()
T2.start()
T3.start()
T4.start()
T5.start()
T1.join()
T2.join()
T3.join()
T4.join()
T5.join()
end = time.perf_counter()
print(end - start)
