"""04_conditionals / excerise.py — runnable demos, one section per subtopic."""

# 1. if
balance = -50
if balance < 0:
    print("1. overdrawn")

# 2. elif — stops at the first true branch
grade = 82
if grade >= 90:
    print("2. A")
elif grade >= 80:
    print("2. B")     # this one runs; lower branches never checked
elif grade >= 70:
    print("2. C")

# 3. else
age = 15
if age >= 18:
    print("3. adult")
else:
    print("3. minor")

# 4. Nested conditions
logged_in = True
is_admin = True
if logged_in:
    if is_admin:
        print("4. admin dashboard")
    else:
        print("4. user dashboard")

# 5. Multiple conditions (elif chain vs combined expression)
temp = 72
if temp < 32:
    print("5. freezing")
elif temp < 60:
    print("5. cold")
elif temp < 80:
    print("5. mild")
else:
    print("5. hot")

can_drive = age >= 16 and logged_in   # combined into one branch
print("5b. can_drive:", can_drive)

# 6. Boolean expressions
items = ["apple"]
if len(items) > 0:
    print("6. has items (explicit)")

# 7. Truthiness — idiomatic version of the same check
if items:
    print("7. has items (idiomatic)")

# 8. Conditional expressions (ternary)
status = "adult" if age >= 18 else "minor"
print("8.", status)

# 9. Chained comparisons
score = 75
if 60 <= score < 90:
    print("9. passing but not honors")

# 10. Short-circuit logic
user = None
if user is not None and user == "admin":   # user == "admin" never evaluated
    print("10. welcome admin")
else:
    print("10. no user")

# 11. Combining logical operators (parentheses make intent explicit)
has_id = True
is_member = False
if (age >= 18 and has_id) or is_member:
    print("11. entry allowed")
else:
    print("11. entry denied")

# 12. Designing readable decision logic — guard clauses vs nested ifs
def can_checkout_nested(logged_in, cart_items):
    if logged_in:
        if cart_items:
            return True
        else:
            return False
    else:
        return False

def can_checkout_guarded(logged_in, cart_items):
    if not logged_in:
        return False
    if not cart_items:
        return False
    return True

print("12.", can_checkout_nested(True, ["book"]), can_checkout_guarded(True, ["book"]))