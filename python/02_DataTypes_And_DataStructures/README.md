# 2. Data Types & Data Structures

Every value in Python is an object, and every object has a **type** that determines what it can do and how it behaves. This module builds a solid mental model of Python's core types (numbers, booleans, strings, `None`) and its core containers (lists, tuples, sets, dictionaries) — the vocabulary used in almost every program that follows.

**Learning approach for each concept:**
What it is → Why it exists → How it works → When to use it → Common mistakes → Practical application

---

## 📖 Subtopics Covered

### 1. Integers (`int`)
Whole numbers with no fractional part, and no fixed size limit (Python grows them automatically).
> **Analogy:** like counting on your fingers, but Python never runs out of fingers.
- Arbitrary precision (no overflow like in C/Java)
- Integer division (`//`) vs true division (`/`)
- Common mistake: assuming `/` always returns an `int` (it always returns a `float`).

### 2. Floating-Point Numbers (`float`)
Numbers with a decimal point, stored using binary approximation (IEEE 754).
> **Analogy:** like a ruler with fine but imperfect markings — close enough, rarely exact.
- Why `0.1 + 0.2 != 0.3`
- Rounding with `round()`
- When precision matters, `decimal` or `fractions` is safer than `float`.

### 3. Complex Numbers (`complex`)
Numbers with a real and imaginary part (`3 + 4j`), used in specialized math/engineering domains.
- Rare in everyday scripting, but built into the language
- Accessed via `.real` and `.imag`

### 4. Booleans (`bool`)
Represents `True`/`False`; technically a subtype of `int` (`True == 1`, `False == 0`).
> **Analogy:** a light switch — only two states, nothing in between.
- Result of comparisons and logical operations
- Common mistake: comparing `if x == True:` instead of just `if x:`

### 5. Strings (`str`)
Immutable sequences of characters used to represent text.
> **Analogy:** a string is like a sealed necklace of beads (characters) — you can look at any bead, but you can't swap one out without making a whole new necklace.
- Covered at introductory depth here; full depth in Module 6 (Strings)

### 6. `None`
The single value representing "no value" or "nothing here."
> **Analogy:** an empty mailbox — it's not zero, not false, just... absent.
- Used as a default/placeholder, not an empty container
- Checked with `is None`, never `== None`

### 7. Type Conversion & Coercion
Converting a value from one type to another, either explicitly (`int("5")`) or implicitly (Python doing it for you, e.g. `1 + 2.0 → 3.0`).
- Explicit: `int()`, `float()`, `str()`, `bool()`, `list()`, etc.
- Common mistake: assuming `int("3.5")` works (it doesn't — must go through `float` first)

### 8. Lists
Ordered, **mutable** collections that can hold mixed types.
> **Analogy:** a shopping list — items in order, and you can freely add, remove, or reorder them.
- Created with `[]`
- Best for: sequences that change over time

### 9. Tuples
Ordered, **immutable** collections.
> **Analogy:** a printed receipt — the order and contents are fixed once issued.
- Created with `()`
- Best for: fixed groups of values (like coordinates `(x, y)`) or dictionary keys

### 10. Sets
Unordered collections of **unique** elements.
> **Analogy:** a bag of unique stamps — duplicates just don't stick.
- Created with `{}` or `set()`
- Best for: membership testing and removing duplicates
- Fast `in` checks (backed by hashing)

### 11. Dictionaries
Unordered (insertion-ordered since 3.7+) collections of **key → value** pairs.
> **Analogy:** a real dictionary — you look up a word (key) to find its definition (value).
- Created with `{}` or `dict()`
- Best for: fast lookups by a meaningful label instead of a numeric position

### 12. Nested Data Structures
Structures containing other structures — a list of dictionaries, a dictionary of lists, etc.
> **Analogy:** boxes inside boxes — useful for representing real-world, hierarchical data (like JSON).
- Common in real applications (API responses, config files)
- Common mistake: losing track of how many "levels deep" you are

### 13. Mutability & Immutability
Whether an object's contents can be changed after creation.
- **Mutable:** list, dict, set
- **Immutable:** int, float, bool, str, tuple, frozenset
> **Analogy:** mutable = a whiteboard (erase and rewrite), immutable = a printed page (make a new page instead).
- Affects function arguments, default values, and safe sharing of data

### 14. Hashability
Whether an object has a fixed hash value, making it usable as a dict key or set member.
- Immutable types are (usually) hashable; mutable types are not
- Common mistake: trying to use a `list` as a dictionary key (raises `TypeError`)

### 15. Indexing
Accessing a single element by its position.
> **Analogy:** picking one item off a numbered shelf.
- Zero-based (`my_list[0]` is the first item)
- Negative indices count from the end (`my_list[-1]` is the last item)

### 16. Slicing
Accessing a *range* of elements using `start:stop:step`.
> **Analogy:** cutting a slice out of a loaf of bread instead of taking one crumb.
- Works on strings, lists, and tuples
- The `stop` index is never included

### 17. Membership
Checking whether a value exists inside a container, using `in` / `not in`.
- Works on strings, lists, tuples, sets, and dict keys
- Sets and dicts check membership fastest (via hashing)

### 18. Common Built-in Operations & Built-in Functions
Operations and functions that work across many data types: `len()`, `sum()`, `min()`, `max()`, `sorted()`, `+` (concatenation), `*` (repetition), and more.
- Knowing these well avoids reinventing basic logic
- Practical application: quick aggregation and inspection of any collection

---

## 🗂️ Files

```text
02_data_types/
├── examples.py    # Annotated, runnable demonstrations of every subtopic
├── practice.py    # Practice exercises (with guidance, no answers given away)
└── README.md      # This file
```