# 19. Concurrency Foundations

Concurrency lets a program make progress on multiple tasks during overlapping periods. Python offers threads, processes, and asynchronous programming, each with different execution and coordination models. The correct choice depends on whether work is I/O-bound, CPU-bound, or naturally asynchronous.

## 📖 Subtopics

### 1. Processes vs threads
A process has its own memory space; threads share memory within a process. Processes provide stronger isolation, while threads can share data more directly.

### 2. Threading fundamentals
`threading` runs tasks in threads within one process. Threads are useful for many I/O-bound workloads, but shared state requires synchronization.

### 3. Multiprocessing fundamentals
`multiprocessing` creates separate processes and can achieve true parallel CPU execution in CPython for suitable workloads.

### 4. Concurrency vs parallelism
Concurrency means multiple tasks can make progress during overlapping periods. Parallelism means tasks execute simultaneously on multiple execution resources.

### 5. Synchronization concepts
Locks, events, semaphores, queues, and other primitives coordinate concurrent work and protect shared state.

### 6. Async programming fundamentals
Async programming uses cooperative scheduling: tasks yield control while waiting, allowing another task to run.

### 7. `async`
`async def` defines a coroutine function. Calling it returns a coroutine object that must be awaited or scheduled to execute.

### 8. `await`
`await` pauses the current coroutine until an awaitable completes, giving the event loop an opportunity to run other tasks.

### 9. Event loops
An event loop schedules and drives asynchronous tasks, especially around I/O readiness and other awaitable operations.

### 10. `asyncio`
The standard-library `asyncio` framework provides event-loop-based asynchronous programming tools, tasks, synchronization primitives, and networking integrations.

### 11. When concurrency is useful
Concurrency is valuable when tasks spend time waiting, such as network requests, file operations, or service calls. CPU-heavy work often benefits more from processes or specialized native/vectorized tools.

## 🧠 Core Concepts

- Threads share process memory; processes isolate memory.
- Async code is cooperative rather than automatically parallel.
- `async def` creates coroutine functions; `await` yields control while waiting.
- Concurrency introduces coordination problems such as races and deadlocks.
- Choose a model based on workload and library support, not fashion.

## ⚠️ Common Mistakes

- Assuming threads automatically make CPU-bound Python code parallel in CPython.
- Blocking the event loop with long synchronous work.
- Sharing mutable state without synchronization.
- Creating concurrency before measuring a real bottleneck.
- Confusing concurrency with parallelism.

## 🗂️ Files

- `exercise.py` — runnable threading, multiprocessing, and asyncio fundamentals.
- `fundamentals.py` — 10 concurrency reasoning exercises.

## 🎯 Expected Outcome

You should be able to distinguish processes, threads, and async tasks, explain the event loop, identify synchronization risks, and choose an appropriate concurrency model for common workloads.