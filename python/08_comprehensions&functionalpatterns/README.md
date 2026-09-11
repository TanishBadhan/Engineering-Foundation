# 8. Comprehensions & Functional Patterns

Comprehensions provide concise ways to build collections, while functional tools such as `map()`, `filter()`, `reduce()`, and `sorted()` help transform, select, aggregate, and order data.

## 📖 Subtopics

1. **List comprehensions** — Build lists from an iterable in one expression.
2. **Set comprehensions** — Build sets while automatically removing duplicates.
3. **Dictionary comprehensions** — Build dictionaries from key/value expressions.
4. **Conditional comprehensions** — Use `if` to include or transform values conditionally.
5. **Nested comprehensions** — Process nested iterables; use only when the logic remains readable.
6. **Generator expressions** — Produce values lazily instead of creating the whole collection immediately.
7. **`map()`** — Apply a function to every item and return an iterator.
8. **`filter()`** — Keep items for which a predicate is true and return an iterator.
9. **`reduce()`** — Repeatedly combine items into one result; imported from `functools`.
10. **`sorted()`** — Return a new sorted list without modifying the original iterable.
11. **`key=`** — Supply the value used for comparison when sorting.
12. **When comprehensions improve code** — Use them for short, obvious transformations or filtering.
13. **When comprehensions become harmful** — Avoid deeply nested, heavily conditional, or side-effect-heavy expressions.

## Core Concepts

- Comprehensions are expressions, not a replacement for every loop.
- Generator expressions are lazy and useful when processing large data streams.
- `map()` and `filter()` are lazy in Python 3, so convert them to `list()` only when a list is actually needed.
- `reduce()` is useful for some cumulative operations, but a normal loop or built-in such as `sum()` may be clearer.
- `sorted()` creates a new list; `.sort()` modifies a list in place.
- A good comprehension should be understandable at a glance.

## Common Mistakes

- Confusing a generator expression with a list comprehension.
- Using `reduce()` when `sum()`, `max()`, `min()`, or another clearer operation exists.
- Writing multi-level comprehensions that are harder to read than ordinary loops.
- Accidentally creating side effects inside comprehensions.
- Forgetting that `sorted()` does not mutate the original list.

## 🗂️ Files

- `exercise.py` — Runnable demonstrations.
- `fundamentals.py` — 10 practice questions.

## Expected Outcome

You should be able to choose between loops, comprehensions, generators, and functional tools based on clarity, memory use, and the operation being performed.
