"""Runnable examples for Concurrency Foundations."""

import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 1–2. Threads

def thread_task(name):
    print("thread:", name)

thread = threading.Thread(target=thread_task, args=("worker",))
thread.start()
thread.join()

# 3. Multiprocessing
# ProcessPoolExecutor runs CPU-oriented work in separate processes.
def square(value):
    return value * value

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        print("process result:", list(executor.map(square, [2, 3, 4])))

# 4–5. Concurrency / synchronization concepts
# A Lock protects a shared critical section. Prefer Queue or other safer
# coordination mechanisms when possible.
lock = threading.Lock()
with lock:
    print("protected critical section")

# 6–10. Async programming, async/await, event loop, asyncio
async def task(name, delay):
    print("start:", name)
    await asyncio.sleep(delay)
    print("finish:", name)
    return name

async def main():
    results = await asyncio.gather(task("A", 0.1), task("B", 0.1))
    print("async results:", results)

asyncio.run(main())

# 11. Use concurrency when waiting/independent work makes overlapping progress
# worthwhile. Measure first and consider library-specific constraints.
