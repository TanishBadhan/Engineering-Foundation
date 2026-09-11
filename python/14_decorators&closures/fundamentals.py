"""10-question practice set for Decorators & Closures."""

# Q1 — Nested function
# Write outer() containing inner(). Make inner() return a value and call it
# from outer().

# Q2 — Closure
# Write make_power(exponent) that returns a function using exponent later.
# Demonstrate the retained value.

# Q3 — Free variable
# Identify which variable in your closure is local to the inner function and
# which is a free variable from the enclosing function.

# Q4 — Basic decorator
# Write a decorator that prints "before" and "after" a function call.

# Q5 — @ syntax
# Apply your decorator both with @decorator and by explicit function rebinding.
# Explain why the two forms are equivalent.

# Q6 — wraps
# Remove functools.wraps from your decorator, inspect __name__/__doc__, then add
# wraps back and compare the result.

# Q7 — Arbitrary arguments
# Modify the decorator so it can wrap functions accepting arbitrary positional
# and keyword arguments.

# Q8 — Parameterized decorator
# Create a decorator factory that accepts a prefix string and prints that prefix
# before each function call.

# Q9 — Practical pattern
# Design a decorator for simple execution logging. Decide what information is
# useful without exposing sensitive arguments.

# Q10 — Reasoning
# Explain why decorators are useful for cross-cutting behavior and why putting
# unrelated business logic into a decorator can make a codebase harder to follow.
