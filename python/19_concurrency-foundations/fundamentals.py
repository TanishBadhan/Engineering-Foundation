"""10-question practice set for Concurrency Foundations."""

# Q1 — Processes vs threads
# Explain the memory-isolation difference between a process and a thread and
# give one suitable use case for each.

# Q2 — Threading
# Create two threads that perform independent I/O-like waiting and join both.
# Explain why the main thread must coordinate their completion when needed.

# Q3 — Multiprocessing
# Use ProcessPoolExecutor to calculate squares for several inputs. Explain why
# processes are useful for CPU-bound work in CPython.

# Q4 — Concurrency vs parallelism
# Give a concrete example of concurrent tasks that are not necessarily executing
# simultaneously and another example of true parallel execution.

# Q5 — Synchronization
# Create a shared counter updated by multiple threads. Protect the critical
# section with a Lock and explain what race condition the lock prevents.

# Q6 — Async basics
# Write an async coroutine that awaits asyncio.sleep() and returns a value.

# Q7 — await
# Write two coroutines and use asyncio.gather() so their waiting periods overlap.
# Explain what await gives the event loop the opportunity to do.

# Q8 — Event loop
# Explain the role of an event loop and why blocking synchronous work inside an
# async function can hurt responsiveness.

# Q9 — asyncio
# Build a small asyncio program that schedules several independent tasks and
# collects their results.

# Q10 — Choosing a model
# For each workload, choose threads, processes, async, or ordinary synchronous
# code and justify it: HTTP requests, CPU-heavy image processing, simple local
# calculation, and many concurrent socket connections.
