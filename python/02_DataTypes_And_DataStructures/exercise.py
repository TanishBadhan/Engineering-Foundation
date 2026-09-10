"""
02_data_types / examples.py

Annotated, runnable demonstrations of Python's core data types
and data structures. Each section is self-contained — run the
whole file, or copy a section into a REPL to explore it.
"""

# ---------------------------------------------------------------
# 1. Integers (int)
# ---------------------------------------------------------------
a = 10
b = 3
print("1. Integers")
print("a + b =", a + b)
print("a // b (floor division) =", a // b)   # 3, drops the remainder
print("a / b (true division)  =", a / b)     # 3.333..., always a float
print("a % b (modulo)         =", a % b)     # 1, the remainder
print("a ** b (power)         =", a ** b)    # 1000
big = 2 ** 100                                # no overflow, Python grows automatically
print("2**100 =", big)
print()

# ---------------------------------------------------------------
# 2. Floating-point numbers (float)
# ---------------------------------------------------------------
print("2. Floats")
x = 0.1 + 0.2
print("0.1 + 0.2 =", x)                       # 0.30000000000000004, not exactly 0.3
print("rounded:", round(x, 2))                # 0.3, fixed with rounding
print()

# ---------------------------------------------------------------
# 3. Complex numbers (complex)
# ---------------------------------------------------------------
print("3. Complex numbers")
c = 3 + 4j
print("c =", c, "| real:", c.real, "| imag:", c.imag)
print()

# ---------------------------------------------------------------
# 4. Booleans (bool)
# ---------------------------------------------------------------
print("4. Booleans")
print("True + True =", True + True)           # 2, because bool is a subtype of int
print("isinstance(True, int) =", isinstance(True, int))
is_valid = 5 > 3
print("is_valid =", is_valid)
print()

# ---------------------------------------------------------------
# 5. Strings (str) — brief intro (full depth in Module 6)
# ---------------------------------------------------------------
print("5. Strings")
name = "Tanish"
print("name =", name, "| type:", type(name))
print()

# ---------------------------------------------------------------
# 6. None
# ---------------------------------------------------------------
print("6. None")
result = None
print("result is None ->", result is None)    # correct way to check
print()

# ---------------------------------------------------------------
# 7. Type conversion and coercion
# ---------------------------------------------------------------
print("7. Type conversion")
print(int("42"))          # explicit: str -> int
print(float("3.14"))      # explicit: str -> float
print(str(99))            # explicit: int -> str
print(1 + 2.0)             # implicit coercion: int + float -> float
try:
    int("3.5")             # fails: must go through float first
except ValueError as e:
    print("int('3.5') failed:", e)
print(int(float("3.5")))  # correct two-step conversion
print()

# ---------------------------------------------------------------
# 8. Lists — ordered, mutable
# ---------------------------------------------------------------
print("8. Lists")
groceries = ["milk", "eggs", "bread"]
groceries.append("butter")
groceries[0] = "oat milk"
print("groceries:", groceries)
print()

# ---------------------------------------------------------------
# 9. Tuples — ordered, immutable
# ---------------------------------------------------------------
print("9. Tuples")
point = (4, 7)
print("point:", point)
try:
    point[0] = 10          # fails: tuples can't be modified
except TypeError as e:
    print("modifying tuple failed:", e)
print()

# ---------------------------------------------------------------
# 10. Sets — unordered, unique elements
# ---------------------------------------------------------------
print("10. Sets")
stamps = {"blue", "red", "blue", "green"}
print("stamps (duplicates removed):", stamps)
stamps.add("gold")
print("blue in stamps ->", "blue" in stamps)
print()

# ---------------------------------------------------------------
# 11. Dictionaries — key -> value pairs
# ---------------------------------------------------------------
print("11. Dictionaries")
person = {"name": "Tanish", "role": "learner"}
print("person['name'] =", person["name"])
person["topic"] = "data types"
print("person:", person)
print()

# ---------------------------------------------------------------
# 12. Nested data structures
# ---------------------------------------------------------------
print("12. Nested structures")
students = [
    {"name": "Ana", "scores": [90, 85]},
    {"name": "Ben", "scores": [70, 75]},
]
print("Ana's first score:", students[0]["scores"][0])
print()

# ---------------------------------------------------------------
# 13. Mutability and immutability
# ---------------------------------------------------------------
print("13. Mutability")
mutable_list = [1, 2, 3]
immutable_tuple = (1, 2, 3)
mutable_list.append(4)      # allowed, same object modified in place
print("mutable_list:", mutable_list)
new_tuple = immutable_tuple + (4,)   # not modified, a NEW tuple is created
print("original tuple unchanged:", immutable_tuple)
print("new_tuple:", new_tuple)
print()

# ---------------------------------------------------------------
# 14. Hashability
# ---------------------------------------------------------------
print("14. Hashability")
print("hash of an int:", hash(42))
print("hash of a tuple:", hash((1, 2)))
try:
    hash([1, 2])            # fails: lists are mutable, so unhashable
except TypeError as e:
    print("hash(list) failed:", e)
print()

# ---------------------------------------------------------------
# 15. Indexing
# ---------------------------------------------------------------
print("15. Indexing")
letters = ["a", "b", "c", "d"]
print("first:", letters[0])
print("last:", letters[-1])
print()

# ---------------------------------------------------------------
# 16. Slicing
# ---------------------------------------------------------------
print("16. Slicing")
numbers = [0, 1, 2, 3, 4, 5, 6]
print("numbers[1:4] =", numbers[1:4])     # index 4 (stop) is excluded
print("numbers[::2] =", numbers[::2])     # every 2nd item
print("numbers[::-1] =", numbers[::-1])   # reversed
print()

# ---------------------------------------------------------------
# 17. Membership
# ---------------------------------------------------------------
print("17. Membership")
print("3 in numbers ->", 3 in numbers)
print("'z' in letters ->", "z" in letters)
print("'name' in person ->", "name" in person)   # checks dict KEYS
print()

# ---------------------------------------------------------------
# 18. Common built-in operations & functions
# ---------------------------------------------------------------
print("18. Built-in operations")
values = [4, 1, 7, 3]
print("len:", len(values))
print("sum:", sum(values))
print("min/max:", min(values), max(values))
print("sorted:", sorted(values))
print("concatenation:", [1, 2] + [3, 4])
print("repetition:", [0] * 3)