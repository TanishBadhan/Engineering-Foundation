"""10-question practice set for Python Functions.

Attempt these without opening exercise.py first.
"""

# Q1 — Parameters / arguments
# Write a function greet_user(name, greeting="Hello") that returns:
# "<greeting>, <name>!"
# Test it with both positional and keyword arguments.

# Q2 — *args
# Write sum_all(*args) that returns the sum of every supplied number.
# Test: sum_all(2, 4, 6, 8) -> 20

# Q3 — **kwargs
# Write describe_person(**kwargs) that prints each key and value.
# Test with name, age, and role.

# Q4 — Return values
# Write min_max(numbers) that returns BOTH the smallest and largest value.
# Unpack the result into two variables.

# Q5 — Scope
# Predict the output before running:
# x = 10
# def test():
#     x = 20
#     return x
# print(test())
# print(x)
# Then explain why the two values differ.

# Q6 — Higher-order functions
# Write apply_twice(function, value) so that function is applied two times.
# Example: apply_twice(lambda x: x * 2, 3) -> 12

# Q7 — Lambda + sorting
# Given:
# students = [("A", 72), ("B", 91), ("C", 65)]
# Sort the list by the marks using a lambda as the key.

# Q8 — Recursion
# Write recursive countdown(n) that prints n down to 1 and then prints "Done".
# Make sure there is a base case.

# Q9 — Type hints + docstring
# Write calculate_power(base, exponent) with type hints and a useful docstring.
# Return base raised to exponent.

# Q10 — Pure vs impure
# Create one pure function that calculates a value from its inputs.
# Create one impure function that also modifies an external list or dictionary.
# Explain in comments what makes each function pure or impure.
