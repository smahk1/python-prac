import sys
from pathlib import Path

# Add the parent directory (Intermediate_Python) to Python's module search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import asyncio
from context_managers import time_it
async def fetch_data(delay):
    print("fetching data...")
    await asyncio.sleep(delay) # some IO task
    print("data fetched!")
    return "some data"

async def main():
    r""" for concurrency we will create some 'tasks' """
    with time_it():
        data1 = asyncio.create_task(fetch_data(2)) # create_task starts a process in the back
        data2 = asyncio.create_task(fetch_data(3))
        data3 = asyncio.create_task(fetch_data(4)) # should take 4s total if working concurrently
        data1 = await data1 # await simply makes the program wait for a reply but the process itself is running from earlier
        data2 = await data2
        data3 = await data3
    print("Ending main...")
asyncio.run(main())
     