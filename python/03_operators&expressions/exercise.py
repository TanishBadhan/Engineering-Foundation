"""03_operators / examples.py — runnable demos, one section per subtopic."""

# 1. Arithmetic
print("1.", 7 + 3, 7 - 3, 7 * 3, 7 / 3, 7 // 3, 7 % 3, 7 ** 2)

# 2. Comparison
print("2.", 5 == 5, 5 != 3, 5 > 3, 5 <= 5)

# 3. Assignment
x = 10
x += 5   # same as x = x + 5
x //= 3
print("3.", x)

# 4. Logical
a, b = True, False
print("4.", a and b, a or b, not a)

# 5. Identity
l1 = [1, 2]
l2 = [1, 2]
l3 = l1
print("5.", l1 == l2, l1 is l2, l1 is l3)   # equal values, different objects, same object

# 6. Membership
print("6.", 3 in [1, 2, 3], "z" not in "abc")

# 7. Bitwise
print("7.", 5 & 3, 5 | 3, 5 ^ 3, ~5, 5 << 1, 5 >> 1)

# 8. Precedence
print("8.", 2 + 3 * 4)        # 14, * before +
print("8.", (2 + 3) * 4)      # 20, parentheses override

# 9. Associativity
print("9.", 2 ** 3 ** 2)      # 512, ** is right-to-left: 2**(3**2)
print("9.", 10 - 3 - 2)       # 5, - is left-to-right: (10-3)-2

# 10. Expressions vs statements
value = (3 + 4)   # (3 + 4) is an expression; the whole line is a statement
# `if x:` is a statement; it has no value itself

# 11. Truthiness
for item in [0, 1, "", "hi", [], [1], None]:
    print("11.", repr(item), "->", bool(item))

# 12. Short-circuit evaluation
def noisy():
    print("   noisy() called")
    return True

print("12. testing and:")
False and noisy()   # noisy() never runs — left side already False
print("12. testing or:")
True or noisy()      # noisy() never runs — left side already True