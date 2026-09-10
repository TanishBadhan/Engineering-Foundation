"""04_conditionals /fundamentals.py — fill in each TODO, no answers given."""

# 1-3. if/elif/else: classify `temp` into "freezing" (<32), "cold" (<60),
# "mild" (<80), or "hot" (else). Print the result.
temp = 45

# my sol:

if temp < 32:
     print("freezing")
elif temp < 60:
    print("cold")
elif temp < 80:
    print("mild")
else:
    print("Hot")
    
# 4. Nested conditions: print "admin dashboard" only if `logged_in` AND
# `is_admin` are both True, "user dashboard" if logged in but not admin,
# and "please log in" otherwise. Use nested ifs.
logged_in = True
is_admin = False

# my sol:
if logged_in == True and is_admin == True:
    print("admin_dashboard")
elif logged_in == True and is_admin == False:
    print("user dashboard")
else:
    print("Please Login")
    
# 5. Multiple conditions: a discount applies if is_member OR cart_total
# is over 100. Write the combined boolean expression.
is_member = False
cart_total = 120
if is_member == True or cart_total > 100:
    print("eligible for discount")
else: 
    print("sorry no discount for you")


# 6-7. Boolean expressions & truthiness: rewrite this explicit check
# using truthiness instead of len():
cart = []
# if len(cart) == 0:
#     print("cart is empty")
# TODO: rewrite using truthiness directly
 # my sol :
 
if cart:
    print("cart is not empty")
else:
    print("the cart is empty")

# 8. Conditional expression: assign "even" or "odd" to `parity` for the
# number below in a single line, using a ternary.
number = 17
# parity = ...

# my sol :

parity = "even" if number % 2 == 0 else "odd"
print(parity)

# 9. Chained comparisons: check if `pin` is a valid 4-digit range
# (1000-9999) using a single chained comparison.
pin = 4521

# my sol :
is_valid = "correct PIN" if 1000<= pin <= 9999 else "wrong PIN"
print(is_valid)

# 10. Short-circuit: `config` might be None. Safely check if
# config["debug"] is True without risking a crash on None.
config = None
# TODO

if config is not None and config["Debug"]:
    print("Debugging is ON")
else:
    print("Debugging is OFF")
    

# 11. Combining logical operators: entry is allowed if (age >= 18 AND
# has_ticket) OR is_staff. Use parentheses to make the grouping explicit.
age = 20
has_ticket = False
is_staff = True
entry_allowed = "Entry Allowed" if (age >= 18 and has_ticket) or is_staff else "No Entry"
print(entry_allowed)

# 12. Readable decision logic: rewrite this nested version using guard
# clauses inside a function instead.
def is_eligible_nested(has_license, age, has_insurance):
    if not has_license:
        return False
   
    if age < 18:
        return False
    
    if not has_insurance:
        return False
    
    return True # every check passed so now no nesting is required.