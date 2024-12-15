import asyncio
import random

counter = 0.0
the_lock = asyncio.Lock()

'''
async def async_add_count(seed):
    global counter
    for _ in range(1000):
        tmp = counter
        await asyncio.sleep(random.random() * 0.001)
        counter = tmp + seed
        await asyncio.sleep(random.random() *0.001)
'''

async def async_add_count(seed):
    global counter
    for _ in range(1000):
        async with the_lock:
            tmp = counter
            await asyncio.sleep(random.random() * 0.001)
            counter = tmp + seed
            await asyncio.sleep(random.random() *0.001)

async def main():

    t1 = asyncio.create_task(async_add_count(1.0))
    t2 = asyncio.create_task(async_add_count(2.0))

    await asyncio.gather(t1, t2)
    print('final', counter)

if __name__ == "__main__":
    asyncio.run(main())



