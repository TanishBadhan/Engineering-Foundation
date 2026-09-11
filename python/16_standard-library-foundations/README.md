# 16. Standard Library Foundations

Python's standard library provides mature tools for common tasks. The goal is not to memorize APIs; it is to recognize which module solves a problem and know how to read its documentation.

## 📖 Subtopics

### 1. `math`
Provides mathematical functions and constants such as `sqrt`, `ceil`, `floor`, and `pi`.

### 2. `random`
Generates pseudo-random values. Use an appropriate secure source instead for security-sensitive tokens or secrets.

### 3. `datetime`
Handles dates, times, timedeltas, and timezone-aware datetime values.

### 4. `os`
Provides operating-system interfaces such as environment variables and process/filesystem-related operations.

### 5. `pathlib`
Provides object-oriented filesystem paths and is usually preferable to manual path-string manipulation.

### 6. `sys`
Exposes interpreter/runtime information such as command-line arguments, module cache, and standard streams.

### 7. `collections`
Provides specialized containers such as `Counter`, `defaultdict`, and `deque`.

### 8. `itertools`
Provides efficient iterator-building tools such as `chain`, `islice`, `product`, and `groupby`.

### 9. `functools`
Provides higher-order-function utilities such as `reduce`, `partial`, `wraps`, and caching tools.

### 10. `re`
Provides regular-expression matching and substitution. Use it when pattern matching is genuinely appropriate, not for every string task.

### 11. `json`
Encodes and decodes JSON data for common configuration and API interchange tasks.

### 12. `csv`
Reads and writes comma-separated and similar tabular text formats while handling quoting correctly.

### 13. `statistics`
Provides common statistical calculations such as mean, median, and standard deviation.

## 🧠 Core Concepts

- Choose a standard-library tool before reinventing common functionality.
- Read official documentation for exact behavior and edge cases.
- `pathlib` is the preferred modern path abstraction for many applications.
- `datetime` requires care around naive vs timezone-aware values.
- Regular expressions are powerful but can reduce readability when simpler string operations work.

## ⚠️ Common Mistakes

- Using `random` for security-sensitive secrets.
- Mixing naive and timezone-aware datetimes carelessly.
- Building filesystem paths with hard-coded separators.
- Writing a complex regex for a problem solved by `split()` or `startswith()`.
- Memorizing functions instead of learning how to search documentation.

## 🗂️ Files

- `exercise.py` — runnable examples from the major standard-library modules.
- `fundamentals.py` — 10 tool-selection and usage problems.

## 🎯 Expected Outcome

You should recognize the major standard-library modules, use their core capabilities, and quickly find unfamiliar APIs in documentation.