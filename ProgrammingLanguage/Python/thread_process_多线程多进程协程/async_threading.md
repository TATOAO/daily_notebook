


```python
# 如果在一个新的线程，有两个等价的创建新loop的方法

# Option 1 
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(self.start()) 
finally:
    loop.close()

# Option 2
asyncio.run(self.start())

```


# create task

```python
import asyncio

async def download_file(url, delay):
    print(f"Downloading {url}...")
    await asyncio.sleep(delay)
    print(f"Finished {url}")

async def main():
    task1 = asyncio.create_task(download_file("url1", 2))
    task2 = asyncio.create_task(download_file("url2", 1))
    await task1
    await task2

asyncio.run(main())
# Output:
# Downloading url1...
# Downloading url2...
# Finished url2 (after 1s)
# Finished url1 (after 2s)

```
