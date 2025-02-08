import asyncio
from datetime import datetime

async def download_file(url, delay):
    print(f"Downloading {url}...")
    await asyncio.sleep(delay)
    print(f"Finished {url}")

async def main():
    task1 = asyncio.create_task(download_file("url1", 2))
    task2 = asyncio.create_task(download_file("url2", 10))
    print(datetime.now())
    await task1
    print(datetime.now())
    await task2
    print(datetime.now())

asyncio.run(main())
# Output:
# Downloading url1...
# Downloading url2...
# Finished url2 (after 1s)
# Finished url1 (after 2s)

# /home/atatlan/Documents/daily_notebook/ProgrammingLanguage/Python/thread_process_多线程多进程协程/test_async_create_task.py

