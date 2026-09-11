# 13. Iterators, Generators & Context Managers

Iterators control sequential access to values, generators provide a convenient lazy iterator implementation, and context managers define resource setup and cleanup. These ideas connect Python syntax to efficient execution and reliable resource handling.

## 📖 Subtopics

### 1. Iterator protocol
An iterator supplies values one at a time and follows the `__iter__()` / `__next__()` protocol.

### 2. `__iter__`
Returns an iterator. An iterator normally returns itself from `__iter__`.

### 3. `__next__`
Returns the next value or raises `StopIteration` when exhausted.

### 4. Custom iterators
A class can implement the protocol to control how values are produced.

### 5. Generator functions
A function containing `yield` is a generator function. Calling it creates a generator object rather than executing the whole body immediately.

### 6. `yield`
`yield` produces a value and suspends execution, preserving the generator's state for the next request.

### 7. Generator state
Local variables and the execution position are preserved between `next()` calls.

### 8. Generator expressions
`(expression for item in iterable)` creates a compact lazy generator.

### 9. Lazy evaluation
Values are computed when requested rather than all at once. This can reduce memory use and avoid unnecessary work.

### 10. Context managers
Context managers define setup/cleanup around a `with` block.

### 11. `__enter__`
Runs when entering a `with` block and returns the value bound by `as`.

### 12. `__exit__`
Runs when leaving the block and can perform cleanup or optionally suppress an exception.

### 13. `with`
The `with` statement coordinates context-manager entry and guaranteed exit behavior.

### 14. Resource lifecycle
Resources such as files, locks, and connections should have clear acquisition and release points. Context managers make that lifecycle explicit.

## 🧠 Core Concepts

- Iterables can produce iterators; iterators produce values with `next()`.
- Generators are stateful lazy iterators.
- `yield` pauses and resumes execution.
- Context managers separate resource setup from guaranteed cleanup.

## ⚠️ Common Mistakes

- Calling `next()` after exhaustion without handling `StopIteration`.
- Assuming generators can be restarted after exhaustion.
- Converting a huge generator to a list and losing the memory advantage.
- Forgetting that `__exit__` can suppress exceptions if it returns true.

## 🗂️ Files

- `exercise.py` — runnable iterator, generator, and context-manager examples.
- `fundamentals.py` — 10 practice problems.

## 🎯 Expected Outcome

You should be able to explain iterator behavior, write generators, reason about lazy execution, and implement basic context managers with correct cleanup.