"""freezing problem occurs when we have a large number of tasks and a small number of workers
. In this case, the workers will be busy processing the tasks, and the tasks will be waiting in the queue.
 This can lead to a situation where the workers are idle, but the tasks are not being processed.
 This is known as the freezing problem."""

import asyncio
import time


async def ticker():
    for i in range(5):
        print("tick", i)
        await asyncio.sleep(0.5)  # gives other tasks a turn


async def bad_worker():
    time.sleep(5)
    # locks the event loop
    print("bad worker done")


async def main():
    await asyncio.gather(ticker(), bad_worker())


asyncio.run(main())


"""tick 0 excecute see sleep for 0.5 starts bad_orker for 5 seconds but 0.5 was completed already cannot
move to it it will have to complete the bad_worker first """
##########################################################################################################################
"""SOLVING THE FREEZING PROVBLEM HERE """

"""now god_worker has async not the timer so async allow switching when async operation is there so
tick ,0 then move togood_worker as 0.5 secwait is there then good_worker takes 5 seconds but it will
excecute it only for 0.5 seconds or upto the time when wait(0.5) is over again comes to the ticker
 function then
"""


async def ticker1():
    for i in range(5):
        print("tick", i)
        await asyncio.sleep(0.5)


async def good_worker():
    await asyncio.sleep(3)  # now the loop can run other tasks while waiting
    print("good done")


async def main1():
    await asyncio.gather(ticker1(), good_worker())


asyncio.run(main1())
#############################################################################################################
"""to solve the problem of the freezing we also have threading.to_thread() to solve the problem it will allow excecute blocking function
with someother tjhread so original thread remin the same """

import asyncio, time, threading  # NEW


async def ticker222():
    for i in range(5):
        print("tick", i, "| ticker thread:", threading.current_thread().name)  # NEW
        await asyncio.sleep(0.5)


async def ok_worker():
    print("ok_worker thread:", threading.current_thread().name)  # NEW
    await asyncio.to_thread(time.sleep, 3)  # runs in another thread
    print("ok done | ok_worker thread:", threading.current_thread().name)  # NEW


async def main():
    await asyncio.gather(ticker222(), ok_worker())


asyncio.run(main())


############################################################################################################
import asyncio, time


async def fetch_user():
    print("fetch_user start")
    await asyncio.sleep(1)
    return "user"


async def fetch_orders():
    print("fetch_orders start")
    await asyncio.sleep(1)
    return "orders"


async def main():
    start = time.perf_counter()

    t1 = asyncio.create_task(fetch_user())  # scheduled, not started yet
    t2 = asyncio.create_task(fetch_orders())

    print("both started, doing other work...")
    await asyncio.sleep(0.2)  # loop now runs t1 and t2

    user = await t1  # wait for results
    orders = await t2
    print(user, orders, f"{time.perf_counter() - start:.1f}s")


asyncio.run(main())
#############################################################################################################
"""why use of task group"""
import asyncio


async def slow():
    await asyncio.sleep(1)
    print("slow finished")  # still prints, even though gather already failed
    return "slow result"


async def fails():
    await asyncio.sleep(0.5)
    raise ValueError("boom")


async def main():
    try:
        await asyncio.gather(slow(), fails())
    except ValueError:
        print("caught: boom")  # at 0.5s
    await asyncio.sleep(1)  # stay alive to watch what slow() does


asyncio.run(main())
