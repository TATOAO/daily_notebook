import asyncio
import random

"""
async def fetch_data(name: str, delay: float):
    await asyncio.sleep(delay)
    if random.random() < 0.5:  # Simulate random failure
        raise RuntimeError(f"Fetch failed from {name}")
    print(f"[{name}] Finished fetching after {delay:.2f}s")
    return f"{name}-data"

async def main():
    sources = [("API-A", 1.0), ("API-B", 2.0), ("API-C", 1.5), ("API-D", 0.5)]
    
    results = {}

    try:
        async with asyncio.TaskGroup() as tg:
            for name, delay in sources:
                tg.create_task(
                    fetch_and_store(name, delay, results)
                )
    except* Exception as e:
        print("❌ One or more fetches failed:", e)

    print("\n✅ Final results:", results)

async def fetch_and_store(name, delay, results: dict):
    result = await fetch_data(name, delay)
    results[name] = result

"""

##########  example 2 ################


"""
async def fetch_data(name: str, delay: float):
    await asyncio.sleep(delay)
    if "fail" in name:
        raise RuntimeError(f"{name} failed on purpose")
    print(f"[{name}] Finished fetching after {delay:.2f}s")
    return f"{name}-data"

async def fetch_and_store(name, delay, results: dict):
    result = await fetch_data(name, delay)
    results[name] = result

async def main():
    sources = [
        ("API-success-1", 1.0),
        ("API-fail-A", 0.5),
        ("API-fail-B", 0.8),
        ("API-success-2", 1.2),
    ]
    
    results = {}

    try:
        async with asyncio.TaskGroup() as tg:
            for name, delay in sources:
                tg.create_task(fetch_and_store(name, delay, results))
    except* RuntimeError as err_group:
        print("❌ Multiple fetch tasks failed:")
        for e in err_group.exceptions:
            print(f"  - {e}")

    print("\n✅ Final results (only successes):", results)

"""

####### example 3 ########################################################

async def always_fail(name: str):
    await asyncio.sleep(0)  # Let event loop cycle
    raise RuntimeError(f"{name} failed intentionally")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(always_fail("Task-A"))
            tg.create_task(always_fail("Task-B"))
            tg.create_task(always_fail("Task-C"))
    except* RuntimeError as group_exc:
        print("❌ Multiple RuntimeErrors caught:")
        for err in group_exc.exceptions:
            print(f"  - {err}")




# python3 ProgrammingLanguage/Python/thread_process_多线程多进程协程/async_task_groups.py
if __name__ == "__main__":
    asyncio.run(main())


"""
Very much like asyncio.gather but with
Propagates multiple errors


"""
