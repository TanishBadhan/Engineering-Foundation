"""10-question practice set for Error Handling & Exceptions."""

# Q1 — Error classification
# Give one example each of a syntax, runtime, and logical error and explain
# why they belong to those categories.

# Q2 — Exception hierarchy
# Use issubclass() to inspect relationships among ValueError, TypeError,
# OSError, Exception, and BaseException.

# Q3 — try/except
# Safely convert user-like input strings to integers. Handle only the expected
# conversion exception.

# Q4 — else/finally
# Write a try/except/else/finally example and explain exactly when each block
# executes.

# Q5 — raise
# Write validate_age(age) that raises ValueError for values outside a chosen
# valid range.

# Q6 — Custom exception
# Create InvalidSensorReading(Exception) and raise it when a reading violates
# your chosen sensor limits.

# Q7 — Propagation
# Write two nested functions where the inner function raises an exception and
# the outer caller handles it. Explain the call-stack propagation.

# Q8 — Specific vs broad handling
# Rewrite an example that uses `except Exception:` so that it catches only the
# failures that are actually expected.

# Q9 — Exception chaining
# Convert a ValueError into a domain-specific exception using `raise ... from`
# and explain why preserving the original cause matters.

# Q10 — Reliability design
# Review a function that catches every exception and prints "something failed".
# Explain why it is unreliable and redesign its error handling.
