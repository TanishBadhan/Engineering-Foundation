# 14. Decorators & Closures

Closures allow nested functions to retain access to variables from an enclosing scope. Decorators use that behavior to wrap and extend functions without changing their core implementation. These patterns are common in logging, authentication, timing, validation, and frameworks.

## 📖 Subtopics

### 1. Nested functions
A function can be defined inside another function. The inner function can access names from the enclosing function.

### 2. Closures
A closure is a function that retains access to free variables from its enclosing scope after the outer function has returned.

### 3. Free variables
A free variable is referenced by a nested function but is defined outside that function's local scope.

### 4. Function decorators
A decorator takes a callable and returns a callable, commonly adding behavior around the original function.

### 5. Decorator syntax
`@decorator` above a function is syntactic sugar for rebinding the function through the decorator.

### 6. Preserving metadata with `functools.wraps`
`wraps` copies important metadata such as `__name__` and `__doc__` from the wrapped function to the wrapper.

### 7. Decorators with arguments
A decorator factory accepts configuration first, returns a decorator, and that decorator then wraps the target function. This creates multiple layers of calls.

### 8. Practical decorator patterns
Common uses include logging, timing, authorization checks, caching, validation, retries, and instrumentation. Decorators should remain focused and predictable.

## 🧠 Core Concepts

- Closures capture values through enclosing scope rather than copying a function's code.
- Decorating a function changes what name refers to after decoration.
- `wraps` helps preserve introspection and debugging information.
- Parameterized decorators are usually implemented as a function returning a decorator.

## ⚠️ Common Mistakes

- Forgetting to return the wrapper's result.
- Forgetting `*args, **kwargs` when the decorator should support arbitrary calls.
- Losing function metadata by omitting `functools.wraps`.
- Creating decorators that hide too much control flow.

## 🗂️ Files

- `exercise.py` — runnable closure and decorator examples.
- `fundamentals.py` — 10 practice problems.

## 🎯 Expected Outcome

You should be able to explain closures, write basic decorators, preserve metadata, and build parameterized decorators for practical cross-cutting behavior.