# 11. Error Handling & Exceptions

Errors can prevent a program from running correctly. Python distinguishes syntax problems, runtime exceptions, and logical mistakes. Exception handling lets software detect expected failures, recover when appropriate, and fail clearly when recovery is not possible.

## 📖 Subtopics

### 1. Errors vs exceptions
An error is a broad concept. A Python exception is an object representing an abnormal condition that can be raised and handled.

### 2. Syntax errors
These occur when Python cannot parse the source code, such as a missing colon or unmatched parenthesis.

### 3. Runtime errors
These occur while valid Python code executes, for example `ZeroDivisionError` or `FileNotFoundError`.

### 4. Logical errors
The program runs but produces the wrong result. Python usually cannot detect these automatically.

### 5. Exception hierarchy
Most application exceptions derive from `Exception`; specific subclasses such as `ValueError`, `TypeError`, and `OSError` provide more precise meaning. `BaseException` is higher in the hierarchy and includes system-level exceptions such as `KeyboardInterrupt`.

### 6. `try`
A `try` block contains code whose exceptions you intend to handle.

### 7. `except`
An `except` block handles matching exceptions. Prefer specific exception types.

### 8. `else`
The `else` block runs only when the `try` block completes without an exception.

### 9. `finally`
`finally` runs whether an exception occurs or not, making it useful for cleanup. Context managers are often better for resources.

### 10. Raising exceptions
Raise an exception when a function cannot fulfill its contract or receives invalid input.

### 11. `raise`
`raise ValueError("...")` creates an exception. A bare `raise` inside an exception handler re-raises the current exception.

### 12. Custom exceptions
Define a class inheriting from `Exception` when your application needs a meaningful domain-specific failure type.

### 13. Exception propagation
If an exception is not handled in the current function, it moves up the call stack until a matching handler is found or the program terminates.

### 14. Specific vs broad exceptions
Catch the narrowest expected exception. `except Exception:` can be appropriate at a system boundary for logging or conversion, but should not hide programming bugs.

### 15. Designing reliable error handling
Validate inputs, preserve useful context, clean up resources, log actionable information, and avoid silently swallowing failures.

## 🧠 Core Concepts

- `try/except` is for handling failures, not hiding bugs.
- Exception type communicates what went wrong.
- `else` means success path; `finally` means cleanup path.
- Exceptions propagate through the call stack until handled.
- Resource cleanup is usually better expressed with context managers.

## ⚠️ Common Mistakes

- Using bare `except:`.
- Catching `Exception` around huge sections of code.
- Printing an exception and continuing when the program is actually invalid.
- Losing the original cause when translating exceptions.
- Using exceptions for ordinary control flow when a normal condition is clearer.

## 🗂️ Files

- `exercise.py` — runnable examples of exception handling.
- `fundamentals.py` — 10 practice problems on diagnosis and reliable handling.

## 🎯 Expected Outcome

You should be able to distinguish failure types, catch appropriate exceptions, raise meaningful errors, design custom exceptions, and build failure paths that remain understandable and reliable.