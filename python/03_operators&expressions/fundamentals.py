"""03_operators / practice.py — fill in each TODO, no answers given."""

# 1. Arithmetic: compute how many full weeks and leftover days in 17 days.
days = 17
# weeks = ...

# my sol:
weeks = (days // 7)
leftover = (days % 7)

print("weeks:", weeks)      # Expected output: 2
print("leftover:", leftover)  # Expected output: 3

# 2. Comparison: check if score (below) is a passing grade (>= 60).
score = 72

# my sol:

if score >= 60:
    passed = True
else:
    passed = False

print("passed:", passed)

# 3. Assignment: double `balance` using a compound assignment operator.
balance = 250

# my sol 

balance *= 2
print(f"balance: {balance}")

# 4. Logical: user can checkout only if logged_in AND has_items.
logged_in = True
has_items = False

# my sol:
can_checkout = logged_in and has_items

if can_checkout is True:
    print("User can checkout.")
else:
    print("User cannot checkout.")

# 5. Identity: predict then verify — does `a is b` print True or False?
a = [1, 2, 3]
b = [1, 2, 3]

# my sol:
print(a is b)

# 6. Membership: check if "admin" is one of the allowed_roles.
allowed_roles = ["user", "editor"]

# my sol:
if "admin" in allowed_roles:
    print("Admin role is allowed.") 
else:
    print("Admin role is not allowed.")


# 7. Bitwise: use `&` to check if a number `n` is odd (hint: n & 1).
n = 6
is_odd = n & 1

if is_odd==1:
    print("Is odd")
else:
    print("Is even")

# 8-9. Precedence & associativity: without running it, predict the result
# of `2 + 3 * 2 ** 2`, then check your answer by printing it.
a = 2 + 3 * 2 ** 2

print(a) # 1** 2.* 3.+

# 10. Expressions vs statements: which of these two lines is an
# expression and which is a statement? Write your answer as a comment.
#   x = 5 : statement 
#   x + 5 : expression

# 11. Truthiness: write a condition that skips empty strings in this list.
words = ["hello", "", "world", ""]

# my sol:
for w in words:
    if w:
        print("truthy")
    else:
        print("false")

# 12. Short-circuit: write a single `and` expression that avoids calling
# risky_divide(10, denom) when denom is 0.
def risky_divide(a, d):
    return a / d

denom = 0

# my sol:

result = denom != 0 and risky_divide(10, denom)
print(result) 