import asyncio
async def foo():
    raise ValueError("Boom")

async def main():
    asyncio.create_task(foo())
    await asyncio.sleep(5)


    
# python3 ProgrammingLanguage/Python/thread_process_多线程多进程协程/async_creat_task_handle_error.py
if __name__ == "__main__":
    asyncio.run(main())
