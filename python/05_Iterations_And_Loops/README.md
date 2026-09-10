# 5. Iteration & Loops

Iteration is how a program repeats work — over a fixed collection (`for`) or until a condition changes (`while`). This module covers both loop forms plus the iterator machinery underneath them, which is what makes Python's `for` loop work on anything "iterable," not just lists.

---

## 🔁 `for` Loops

**Iteration fundamentals — iterables, iterators, `iter()`, `next()`, the iteration protocol:**
A `for` loop doesn't know how to walk a list, a string, or a file directly — it relies on a two-part protocol. An **iterable** is anything with an `__iter__` method (lists, strings, dicts, files); calling `iter(obj)` on it produces an **iterator** — an object with `__next__`, which `for` calls repeatedly via `next()` until it raises `StopIteration`. `for item in x:` is syntactic sugar for exactly this loop.
> **Analogy:** the iterable is a bookshelf; the iterator is a bookmark that remembers where you are and gives you one book at a time until the shelf is empty.

**Iterating over sequences and dictionaries:**
`for x in my_list` walks values in order. `for key in my_dict` walks **keys** by default — use `.items()` for key-value pairs, `.values()` for values only.

**`range()`:** generates a sequence of numbers **lazily** (not stored all at once) — `range(5)` → 0,1,2,3,4. Used for counting loops when you need an index, not the items themselves.

**Nested `for` loops:** a loop inside another loop's body, for combinations of two dimensions (rows × columns, pairs of items). The inner loop completes fully for every single iteration of the outer one.

**Loop variables, `break`, `continue`, `pass`:** the loop variable is rebound each iteration. `break` exits the loop entirely; `continue` skips to the next iteration; `pass` is a no-op placeholder where a statement is syntactically required.

**`for...else`:** the `else` block runs only if the loop completes **without** hitting `break` — useful for "search and report not-found" patterns.

**`enumerate()` and `zip()`:** `enumerate(seq)` yields `(index, value)` pairs, avoiding manual counters. `zip(a, b)` walks two (or more) sequences in parallel, stopping at the shortest.

**Reverse iteration:** `reversed(seq)` or `seq[::-1]` walks a sequence back to front.

**Iteration patterns & common mistakes:** the biggest pitfall is mutating a list while iterating over it (items get skipped) — iterate over a copy (`for x in list(original):`) if you need to modify the original during the loop.

---

## 🔂 `while` Loops

**Loop conditions & state-controlled iteration:** a `while` loop repeats as long as its condition stays truthy, checked fresh **before every** iteration — used when the number of repetitions isn't known in advance (unlike `for`, which walks a fixed collection).

**Infinite loops & termination:** `while True:` runs forever unless something inside breaks out — usually a `break` triggered by a condition, or an explicit `return`. Every `while` loop must have a credible path to becoming false, or it never ends.

**`break`, `continue`, `while...else`:** behave the same as in `for` loops; `else` runs only if the loop exits normally (condition became false), not via `break`.

**Nested `while` loops:** same idea as nested `for` loops — an inner loop fully cycling within each iteration of an outer one.

**Counters and accumulators:** a counter tracks "how many times" (`count += 1`); an accumulator builds up a running result (`total += value`) — both are updated manually each iteration, unlike `for`, which advances automatically.

**Sentinel-controlled loops:** looping until a specific marker value appears (e.g. reading input until the user types `"quit"`), rather than a fixed count or numeric condition.

**Designing safe loop conditions:** always ensure the condition's controlling variable is actually modified inside the loop body — the most common `while` bug is forgetting to update it, producing an infinite loop by accident.

---

## ⚙️ Iteration Concepts

**Iterable vs. iterator:** an iterable can produce a *new* iterator every time (`iter(my_list)` twice gives two independent iterators); the iterator itself is single-use and remembers its position.

**Lazy iteration & iterator exhaustion:** many iterators (like `range` results, generators, `zip`, `map`) don't compute all their values upfront — they produce each one on demand. Once fully consumed, an iterator is **exhausted**: looping over it again yields nothing, since there's no way to "rewind" it.

**Generators & generator expressions:** a generator function (`yield` instead of `return`) produces values lazily, one at a time, pausing its state between each `yield` — ideal for large or infinite sequences you don't want to hold in memory all at once. A generator expression is the compact form: `(x**2 for x in range(10))`, syntactically like a list comprehension but with `()` instead of `[]`.

**Memory-efficient iteration:** the core payoff of laziness — `sum(x for x in range(10_000_000))` never builds a 10-million-item list in memory; it processes one number at a time.
> **Analogy:** a list is a fully baked batch of cookies sitting on a tray; a generator is a recipe that bakes one cookie the moment you ask for it, and never keeps the whole batch around.

---

## 🗂️ Files
```text
05_loops/
├── exercise.py    # Annotated, runnable demonstrations of every subtopic
├── fundamental.py    # Practice exercises (no answers given away)
└── README.md      # This file
```