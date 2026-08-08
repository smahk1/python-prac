import asyncio
from context_managers import time_it

async def fetch_data(id, delay):
    print("fetching data...")
    await asyncio.sleep(delay) # some IO task
    print("data fetched!")
    return f"some data {id}"

async def main():
    with time_it():
        print("starting main")
        result_list = await asyncio.gather(fetch_data(2, 1), fetch_data(3, 2), fetch_data(4, 3)) # This works concurrently now
        print(result_list)

asyncio.run(main())