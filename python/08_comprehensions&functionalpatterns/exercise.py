"""Runnable examples for Python comprehensions and functional patterns."""

# List, set, and dictionary comprehensions
numbers = [1, 2, 3, 4, 5]
print([n * 2 for n in numbers])
print({n % 3 for n in numbers})
print({n: n * n for n in numbers})

# Conditional and nested comprehensions
print([n for n in numbers if n % 2 == 0])
matrix = [[1, 2], [3, 4]]
print([value for row in matrix for value in row])

# Generator expression: values are produced lazily
squares = (n * n for n in numbers)
print(next(squares))
print(list(squares))

# map() and filter()
print(list(map(lambda n: n + 1, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))

# reduce()
from functools import reduce
print(reduce(lambda a, b: a + b, numbers))

# sorted() and key=
students = [("A", 72), ("B", 91), ("C", 65)]
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[1], reverse=True))

# Prefer a normal loop when the expression becomes difficult to read.
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n * n)
print(result)
