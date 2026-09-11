"""Runnable examples for Python Internals & Execution Model."""

import dis
import copy

# 1–3. Source execution and bytecode fundamentals
def add(a, b):
    return a + b

print("bytecode:")
dis.dis(add)
print("interpreter note: this file is running under a Python implementation")

# 4–5. Namespaces and LEGB
x = "global"

def scope_demo():
    x = "local"
    def inner():
        return x  # enclosing scope
    return inner()

print("LEGB example:", scope_demo())

# 6–7. Object model and references
items = [1, 2]
alias = items
print("same identity:", items is alias)
alias.append(3)
print("shared object:", items)

# 8–10. Memory / garbage collection / reference counting
# CPython implementation details can be inspected with sys.getrefcount(),
# but the exact count is implementation-dependent.
import sys
value = []
print("reference-count example:", sys.getrefcount(value))

# 11–13. Shallow vs deep copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0].append(99)
print("original:", original)
print("shallow shares nested list:", shallow)
print("deep copy isolated:", deep)

# 14. Mutability and object sharing
number = 10
other_number = number
# Integers are immutable; rebinding one name does not mutate the object.
other_number += 1
print("immutable values:", number, other_number)
