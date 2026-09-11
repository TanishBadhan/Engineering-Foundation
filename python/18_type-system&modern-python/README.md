# 18. Type System & Modern Python

Python is dynamically typed, but it also provides a rich annotation system that tools can use for static analysis, IDE support, documentation, and API design. Modern Python typing is primarily about communicating contracts; normal annotations do not automatically enforce types at runtime.

## 📖 Subtopics

### 1. Type annotations
Annotations describe intended types for variables, parameters, and return values, such as `count: int` or `def add(a: int, b: int) -> int`.

### 2. Built-in generic types
Modern Python supports forms such as `list[int]`, `dict[str, float]`, and `tuple[int, ...]` for describing parameterized containers.

### 3. `Optional`
`Optional[T]` traditionally means `T | None`. In modern Python, `T | None` is usually the clearer spelling when supported by the target version.

### 4. `Union`
A union describes a value that may have one of several types. Modern syntax is commonly `int | str`; `typing.Union` remains available.

### 5. `Any`
`Any` effectively disables type checking for that value. Use it deliberately because excessive `Any` removes useful static guarantees.

### 6. Type aliases
An alias gives a meaningful name to a type expression, improving readability and reuse.

### 7. `Callable`
`Callable` describes callable objects, including their argument and return types when specified.

### 8. Generics fundamentals
Generics let a reusable type or function preserve relationships between input and output types rather than replacing them with broad types.

### 9. Static type checking concepts
Tools such as mypy and pyright analyze annotations without executing the program. They can detect many inconsistencies before runtime.

### 10. `typing`
The `typing` module provides typing constructs for compatibility and advanced annotations, although many common forms are now built into Python syntax.

### 11. Structural typing fundamentals
Structural typing checks whether an object supports the required structure/operations rather than requiring a specific inheritance relationship. `Protocol` expresses this idea for static type checkers.

## 🧠 Core Concepts

- Annotations are usually metadata for humans and tools, not runtime enforcement.
- Prefer modern built-in generic syntax when your Python version supports it.
- Use `Any` sparingly.
- Static typing complements, rather than replaces, runtime validation at trust boundaries.
- Structural typing focuses on capabilities rather than class ancestry.

## ⚠️ Common Mistakes

- Assuming annotations automatically reject incorrect runtime values.
- Using `Any` everywhere to silence a type checker.
- Confusing `Optional[T]` with an omitted argument; it specifically means `T` or `None`.
- Adding complex annotations that make a simple API harder to understand.

## 🗂️ Files

- `exercise.py` — runnable examples of annotations and protocols.
- `fundamentals.py` — 10 typing exercises.

## 🎯 Expected Outcome

You should be able to annotate ordinary Python code, understand modern union/generic syntax, use static checking conceptually, and recognize when structural typing is useful.