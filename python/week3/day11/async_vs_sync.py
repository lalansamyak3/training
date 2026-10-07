def hel():
    print("hiii")


hel()
"""normla functoon return ouut[ut wehn called burt async function return coroutine object when called and need to be awaited to get the result"""


#############################################################################################################
async def hello():
    return "hello"


result = hello()
print(result)  # <coroutine object hello at 0x7f8c8e8c0>  # coroutine object

# to implement it we need to use await keyword to get the result of the coroutine object
# use another function that use await with the above function or use
# event loop asyncio.run() to run the coroutine object and get the result
import asyncio


# way1
def run_hello():
    result = asyncio.run(hello())
    print(result)  # hello


# way2
async def run_hello1():
    x = await hello()
    print(x)  # hello


####greet without async operations now ##########################################################################
async def greet():
    return "hello"


async def main():
    x = await greet()
    print(x)


print(asyncio.run(main()))
"""greet dont have async operations so fully excecutes at once so it will not take time to excecute
 but if we have async operations like api calling,db queries etc it will take time to excecute
 and we can see the difference in time taken to excecute the code"""


#####greet with async ipoperstion indide###########################################################################################################
async def greet1():
    await asyncio.sleep(1)
    return "hello"


async def main1():
    x = await greet1()
    print(x)


print(asyncio.run(main1()))
# it will take longer time to excecute because it has async operations inside it and we
# can see the difference in time taken to excecute the code
#############################################################################################################################

"""ASYnc first function to use """

import asyncio
import time
from threading import Thread


async def fetch_user():
    await asyncio.sleep(1)
    return "user"


async def fetch_order():
    await asyncio.sleep(1)
    return "order"


async def main2():
    start = time.perf_counter()
    user = await fetch_user()
    order = await fetch_order()
    print(user, order)
    end = time.perf_counter()
    print(
        f"Total time taken: {end-start} seconds"
    )  # Total time taken: 2.002345323562622 seconds


###########################################################################################################
import asyncio


async def dish(name, seconds):
    print(f"{name}: start")
    await asyncio.sleep(seconds)  # "simmering": loop runs other tasks
    print(f"{name}: done")


async def main():
    await asyncio.gather(dish("soup", 2), dish("rice", 1), dish("tea", 3))


asyncio.run(main())  # ~3s total, not 6s
"""waiting is ther just moveto the next method call or func calling immediateluy
"""
################################################################################################################
"""with async gather and without it """
"""Concept of concurrency and parallelism: Concurrency is when two or more tasks can start, run, and
complete in overlapping time periods. It doesn't necessarily mean they'll ever both be running at the
same instant. Parallelism is when tasks literally run at the same time, e.g., on a multi-core processor.
 In Python, due to the Global Interpreter Lock (GIL), true parallelism is not achieved with threads, but you
   can achieve concurrency with async/await and multiprocessing for CPU-bound tasks."""

""""""
import asyncio
import threading


async def task(n):
    print(n, threading.current_thread().name)
    await asyncio.sleep(1)


async def main():
    await asyncio.gather(task(1), task(2), task(3))


asyncio.run(main())  # every line prints MainThread


async def main3():
    await task(1)
    await task(2)
    await task(3)


asyncio.run(main3())  # every line prints MainThread

# see the diff gather allow func to start togethre and end together without gather
# it will waiut fior other one to completle before starting the next one
# concept of concurrency and parallelism: Concurrency is when two or more tasks can start,
# run, and
##################################################################################################################
