"""10-question practice set for Python Internals & Execution Model."""

# Q1 — Source to execution
# Explain the broad path from .py source to execution in CPython. Distinguish
# parsing, compilation to bytecode, and execution.

# Q2 — Bytecode
# Use dis.dis() on a small function and identify a few instructions.

# Q3 — Namespaces
# Explain local, enclosing, global, and built-in namespaces with a nested
# function example.

# Q4 — References
# Create a list and assign it to two names. Mutate through one name and explain
# why the other name sees the change.

# Q5 — Identity vs equality
# Create two equal but separately constructed lists. Compare == and is and
# explain the difference.

# Q6 — Mutability
# Demonstrate one mutable object and one immutable object and explain what
# assignment versus mutation does in each case.

# Q7 — Shallow copy
# Make a shallow copy of a nested list and demonstrate that the nested object
# is still shared.

# Q8 — Deep copy
# Repeat Q7 using deepcopy() and explain the difference.

# Q9 — Garbage collection
# Explain reference counting in CPython and why cycles require cyclic garbage
# collection. Avoid treating CPython behavior as a universal Python guarantee.

# Q10 — Debugging reasoning
# Given a surprising mutation bug, list the questions you would ask about
# object identity, aliases, mutability, and copies before changing the code.
