import asyncio 

number = 0
lock = asyncio.Lock()

async def func(id):
    global number
    
    """ Some random function """
    print(f'{id} Starting processing...')
    async with lock:  
        new_num = number
        await asyncio.sleep(2)
        new_num += 1
        number = new_num
    print(f'{id} Processing sucessful...')

async def main():  
    process = await asyncio.gather(*[func(id) for id in range(1,4)])
    print(number)


asyncio.run(main())