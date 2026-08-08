import asyncio

""" Events are a more primitive form of locks and can be used to make a coroutine wait for something 
    or in this case an 'event' to occur to continue its execution. They are useful in many cases. """

async def waiter(event):
    """Waits for some event to occur"""

    print("Waiting for event to be set")
    await event.wait()
    print("Event set, wait complete.")

async def setter(event):
    """Does something then sets the event"""
    print("Setting...")
    await asyncio.sleep(2)
    event.set()

async def main():
    event = asyncio.Event()

    await asyncio.gather(waiter(event), setter(event))
    
asyncio.run(main())