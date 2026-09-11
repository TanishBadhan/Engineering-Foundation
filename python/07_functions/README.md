# 7. Functions

Functions are a fundamental part of Python. They let you package logic into reusable units with defined inputs and outputs. Instead of repeating the same code, you can define it once and call it whenever needed.

This module covers functions from basic syntax through argument handling, return values, scope, first-class functions, higher-order functions, recursion, documentation, type hints, and side effects. The goal is not just to memorize syntax, but to understand how Python executes and manages functions.

---

## 📖 Subtopics

### 1. Defining functions
A function is created with `def`, followed by a name, parameters, and an indented body. Defining a function creates a callable object; its body executes only when the function is called.

### 2. Calling functions
A function is called by writing its name followed by parentheses. The call may provide arguments that are bound to the function's parameters before its body executes.

### 3. Parameters and arguments
A **parameter** is the name used in the function definition. An **argument** is the actual value supplied at the call site. Keeping this distinction clear helps when designing and debugging function calls.

### 4. Positional arguments
Positional arguments are matched to parameters according to their order. They are concise, but the caller must know the expected parameter order.

### 5. Keyword arguments
Keyword arguments explicitly identify parameters, such as `name="Tanish"`. They improve readability and allow arguments to be supplied by name rather than position.

### 6. Default arguments
A default value is used when the caller omits that argument. Defaults are useful for optional behavior. Avoid mutable defaults such as `[]` or `{}` because the same object can be reused across calls.

### 7. Variable-length arguments
Python allows functions to accept a flexible number of arguments. This is useful when the number of inputs is not known when the function is designed.

### 8. `*args`
`*args` collects additional positional arguments into a tuple. It is useful for functions that need to accept any number of positional values.

### 9. `**kwargs`
`**kwargs` collects additional keyword arguments into a dictionary. It is useful for flexible named options and for forwarding keyword arguments to other functions.

### 10. Return values
`return` sends a result back to the caller and immediately ends the current function execution. A returned value can be stored, compared, passed to another function, or used in an expression.

### 11. Multiple return values
Python can return multiple comma-separated values. These are packaged into a tuple and can be unpacked into separate variables.

### 12. Scope
Scope determines where a name can be found. Python's common name-resolution order is **LEGB**: Local → Enclosing → Global → Built-in.

### 13. Local and global variables
A local variable belongs to a function's local scope. A global variable is defined at module level. Functions can normally read an accessible global value, but assignment inside a function creates a local name unless `global` is used.

### 14. `global`
`global` tells Python that assignment to a name inside a function should modify the module-level variable. It should be used carefully because global mutation creates hidden dependencies between functions.

### 15. `nonlocal`
`nonlocal` allows a nested function to reassign a variable from its nearest enclosing function scope. It is commonly used when building closures that retain state.

### 16. Function composition
Function composition combines smaller functions so that the output of one becomes the input of another. This encourages small, reusable units instead of one large function containing unrelated logic.

### 17. First-class functions
Python functions are first-class objects. They can be assigned to variables, stored in collections, passed as arguments, and returned from other functions.

### 18. Functions as objects
A function can be referenced without executing it. `func` refers to the function object, while `func()` calls it. Functions also have attributes such as `__name__` and `__doc__`.

### 19. Higher-order functions
A higher-order function accepts another function, returns a function, or both. This pattern appears in callbacks, `sorted(key=...)`, `map`, `filter`, decorators, and many libraries.

### 20. Lambda functions
A lambda creates a small anonymous function containing one expression. Lambdas are useful for short, local operations such as sorting keys; named `def` functions are usually clearer for reusable or complex logic.

### 21. Recursion
Recursion occurs when a function calls itself to solve a smaller version of the same problem. A correct recursive function needs a **base case** and a recursive step that moves toward it. Otherwise, Python can raise `RecursionError`.

### 22. Documentation and docstrings
A docstring is the string placed at the beginning of a function body to document its purpose and behavior. Useful documentation describes important inputs, outputs, assumptions, and side effects. It is available through `function.__doc__`.

### 23. Type hints
Type hints communicate intended parameter and return types, for example `def add(a: int, b: int) -> int`. Python normally does not enforce these annotations at runtime; they mainly improve readability, IDE support, static analysis, and maintainability.

### 24. Pure vs impure functions
A **pure function** depends only on its inputs and does not produce observable external side effects. An **impure function** interacts with external or mutable state, such as modifying a global list, writing a file, printing, or making an external request.

---

## 🔍 Core Concepts

### Function execution
When a function is called, Python evaluates the supplied arguments, binds them to parameters, executes the function body, and returns a result. If execution reaches the end without `return`, the function returns `None`.

### `print()` vs `return`
`print()` displays information to the console. `return` gives a value back to the caller. A function intended for reuse will usually need `return`, not just `print()`.

### `func` vs `func()`
`func` refers to the function object. `func()` executes the function. This distinction is essential when passing functions to higher-order functions.

### Argument binding
Positional, keyword, default, `*args`, and `**kwargs` are different ways of supplying values. You should be able to determine exactly which parameter receives each value before moving to advanced Python.

### LEGB and assignment
Python searches for names using Local, Enclosing, Global, then Built-in scopes. Reading an outer variable and assigning to an outer variable are different operations; `global` and `nonlocal` affect assignment behavior.

### Side effects
Changing external state is observable behavior. Examples include modifying a global list, changing a mutable object supplied by a caller, writing to a file, or making a network request. Recognizing side effects is important for testing and debugging.

---

## ⚠️ Common Mistakes

- Confusing parameters with arguments.
- Using `print()` when the caller needs a returned value.
- Forgetting that `return` ends the current function.
- Confusing `func` with `func()`.
- Supplying positional and keyword arguments incorrectly.
- Using mutable objects as default parameters.
- Assuming `global` or `nonlocal` is required merely to read an outer value.
- Writing recursion without a base case or without progress toward it.
- Using lambdas for logic that deserves a named function.
- Treating type hints as runtime validation.
- Ignoring side effects when reasoning about function behavior.

---

## 🧪 Expected Outcome

After completing this module, you should be able to:

- Design functions with clear inputs and outputs.
- Choose appropriate argument styles, including `*args` and `**kwargs`.
- Return and unpack multiple values.
- Trace variable lookup using LEGB.
- Explain the purpose of `global` and `nonlocal`.
- Pass functions as values and use basic higher-order functions.
- Use lambdas appropriately.
- Trace and write basic recursive functions.
- Add useful docstrings and type hints.
- Distinguish pure functions from functions with side effects.

---

## 🗂️ Files

```text
07_functions/
├── README.md         # Concepts and learning notes
├── exercise.py       # Runnable example for every subtopic
└── fundamentals.py   # 10-question practice set
```

### Practice rule

Attempt `fundamentals.py` before studying the examples in `exercise.py`. The questions focus on reasoning and application rather than copying syntax.
