import asyncio

r""" The resutls of this program are weird since its running like any serial program would
    but this is just for explanation so it's fine."""

# this is a coroutine function
async def fetch_data(delay): # due to the async keyword this returns a coroutine object now
    print("fetching data...")
    await asyncio.sleep(delay) # some IO task
    print("data fetched!")
    return "some data"

async def main():
    print("calling fetch 1...")
    data1 = await fetch_data(2) # coroutines must be awaited to get results
    print("1 done")
    print("calling fetch 2...")
    data2 = await fetch_data(2)
    print("2 done")
    


# This is how the coroutine run
asyncio.run(main())
