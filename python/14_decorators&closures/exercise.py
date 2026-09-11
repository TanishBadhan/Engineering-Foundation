"""Runnable examples for Decorators & Closures."""

from functools import wraps

# 1–3. Nested function, closure, and free variable
def make_multiplier(factor):
    def multiply(value):
        return value * factor  # factor is a free variable
    return multiply

times_three = make_multiplier(3)
print("closure:", times_three(5))

# 4–5. Function decorator and @ syntax
def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("calling:", function.__name__)
        result = function(*args, **kwargs)
        print("result:", result)
        return result
    return wrapper

@log_call
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

add(2, 3)

# 6. functools.wraps preserves metadata
print("name preserved:", add.__name__)
print("doc preserved:", add.__doc__)

# 7. Decorator with arguments / factory
def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(2)
def announce(message):
    print(message)

announce("hello")

# 8. Practical pattern: simple timing/logging could be implemented by the same
# wrapper structure, while authentication and caching would add domain-specific logic.
