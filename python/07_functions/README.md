# 7. Functions

Functions package reusable behavior into named or anonymous callable objects. This module moves from basic function syntax to argument handling, scope, functional patterns, recursion, and writing maintainable functions.

---

## 📖 Subtopics

1. **Defining functions** — create reusable blocks with `def`.
2. **Calling functions** — execute a function and pass required inputs.
3. **Parameters and arguments** — parameters are names in the definition; arguments are values supplied at the call site.
4. **Positional arguments** — matched by parameter position.
5. **Keyword arguments** — matched explicitly by parameter name.
6. **Default arguments** — provide a fallback value when an argument is omitted.
7. **Variable-length arguments** — accept a flexible number of positional or keyword arguments.
8. **`*args`** — collects extra positional arguments into a tuple.
9. **`**kwargs`** — collects extra keyword arguments into a dictionary.
10. **Return values** — send a result back to the caller with `return`.
11. **Multiple return values** — Python returns them as a tuple that can be unpacked.
12. **Scope** — determines where a name can be accessed.
13. **Local and global variables** — local names belong to a function call; global names belong to the module scope.
14. **`global`** — explicitly binds assignment inside a function to a module-level name.
15. **`nonlocal`** — lets a nested function rebind a name from its enclosing function scope.
16. **Function composition** — build larger behavior by combining smaller functions.
17. **First-class functions** — functions can be stored, passed, and returned like other objects.
18. **Functions as objects** — functions have identity, attributes, and can be assigned to variables.
19. **Higher-order functions** — functions that accept functions, return functions, or both.
20. **Lambda functions** — small anonymous functions restricted to a single expression.
21. **Recursion** — a function solves a problem by calling itself on a smaller subproblem; it requires a correct base case.
22. **Documentation and docstrings** — document purpose, inputs, outputs, and important behavior inside the function.
23. **Type hints** — annotate parameters and return values to communicate intended types and improve tooling.
24. **Pure vs impure functions** — pure functions depend only on inputs and avoid observable side effects; impure functions interact with external or mutable state.

---

## 🧠 Learning Standard

For every function concept, understand:

**What it is → Why it exists → How it behaves → When to use it → Common mistakes → Practical use**

Do not memorize syntax without understanding argument binding, return flow, scope, and side effects.

---

## 🗂️ Files

```text
07_functions/
├── exercise.py       # Runnable examples covering every subtopic
├── fundamentals.py   # 10-question practice set covering the module
└── README.md         # Concepts, scope, and learning notes
```

### Practice rule

Attempt `fundamentals.py` without looking at `exercise.py`. The questions are intentionally designed to test reasoning about arguments, scope, functions as objects, recursion, and side effects rather than simple syntax recall.
