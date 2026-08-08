import asyncio
from context_managers import time_it
""" Semaphores are like locks only they can be used to limit how many requests or
    concurrent access requests for a resource are made. """
inc = 0
semaphore = asyncio.Semaphore(2) # run 2 tasks concurrently

async def func(id):
    global inc
    # some heavy work.
    with time_it():
        async with semaphore:
            print(f"Starting task {id}")
            await asyncio.sleep(2)
            inc += 1

async def main():
    run = await asyncio.gather(*[func(id) for id in range(0, 4)]) # run the func 4 times
    print(inc)
    # With the semaphore being set at 2 we get total time = 4s because 2 tasks run concurrently
asyncio.run(main())