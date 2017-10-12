import asyncio

async def slow_operation(future):
    await(asyncio.sleep(1.0))
    future.set_result("Future is done!")

loop = asyncio.get_event_loop()

# simple asyncio.Future usage
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)

# simple asyncio.Task

async def sleep_task(num):
    for i in range(5):
        print(f"process task:{num} iter:{i}")
        await asyncio.sleep(1.0)
    return num

task_list = [loop.create_task(sleep_task(i)) for i in range(2)]
loop.run_until_complete(asyncio.wait_for(task_list, timeout=None))

# append single task
loop.run_until_complete(loop.create_task(sleep_task(3)))

# pass a callable
loop.run_until_complete(asyncio.gather(sleep_task(10),sleep_task(20)))

from urllib.request import urlopen

# a synchronous function
def sync_get_url(url):
    return urlopen(url).read()

async def load_url(url, loop=None):
    future = loop.run_in_executor(None, sync_get_url, url)
    responce = await future
    print(len(responce))

loop = asyncio.get_event_loop()
loop.run_until_complete(load_url("https://www.google.com/",loop=loop))


