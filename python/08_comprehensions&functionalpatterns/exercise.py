# Runnable examples for Module 8.
numbers = [1, 2, 3, 4, 5]
print([n * 2 for n in numbers])
print({n % 3 for n in numbers})
print({n: n * n for n in numbers})
print([n for n in numbers if n % 2 == 0])
print([x for row in [[1, 2], [3, 4]] for x in row])
g = (n * n for n in numbers)
print(next(g), list(g))
print(list(map(lambda n: n + 1, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))
from functools import reduce
print(reduce(lambda a, b: a + b, numbers))
students = [("A", 72), ("B", 91), ("C", 65)]
print(sorted(students, key=lambda s: s[1], reverse=True))
