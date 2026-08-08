import asyncio 

r""" Task groups are essentially gather() with built-in error handling """

async def fetch_data(id, delay):
    print("fetching data...")
    await asyncio.sleep(delay) # some IO task
    print("data fetched!")
    return f"some data {id}"

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for id, delay in enumerate([2,3,4], start=1): # enumerate returns an id with every element (starting from 0 by default)
            task = tg.create_task(fetch_data(id, delay))
            tasks.append(task)
    # The task object contains our results now
    for task in tasks:
        print(f"Result: {task.result()}")

asyncio.run(main())