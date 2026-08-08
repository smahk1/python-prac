import asyncio, aiohttp

gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542', 
        'https://gist.github.com/recluze/a98aa1804884ca3b3ad3', 
        'https://gist.github.com/recluze/5051735efe3fc189b90d', 
        'https://gist.github.com/recluze/460157afc6a7492555bb', 
        'https://gist.github.com/recluze/5051735efe3fc189b90d', 
        'https://gist.github.com/recluze/c9bc4130af995c36176d']

# Defining an async function
async def get_gist(url):
    print("Get: " + url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as responce:
            page_text = await responce.text()
            g_length = len(page_text)
            print(f"Length: {g_length}")
            return g_length

# Creating the event loop, which is the part of the code where async code executes.
asyncio.set_event_loop(asyncio.new_event_loop())  # create the event loop first
loop = asyncio.get_event_loop()             

tasks = []
for g in gists:
    future = asyncio.ensure_future(get_gist(g))
    tasks.append(future)

print(loop.run_until_complete(asyncio.wait(tasks)))

loop.close()

for task in tasks:
    print(task.result())

