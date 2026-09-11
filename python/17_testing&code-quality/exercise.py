"""Runnable examples for Testing & Code Quality.

Run this file directly to see the non-pytest examples. The pytest/unittest
snippets are included as commented learning examples where appropriate.
"""

import logging
import unittest

# 1–2. Assertions / assert
value = 5
assert value > 0
print("assert passed")

# 3–4. Testing fundamentals and unit-style function

def add(a, b):
    return a + b


def test_add_logic():
    assert add(2, 3) == 5


test_add_logic()
print("unit-style test passed")

# 5. unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# Uncomment to run unittest from this file:
# unittest.main()

# 6. pytest fundamentals
# A pytest test can simply be:
# def test_add():
#     assert add(2, 3) == 5

# 7–9. Organization and edge cases
# Keep such tests in tests/test_math.py and include cases such as 0, negatives,
# empty collections, and invalid input.

# 10. Debugging mindset
# Reproduce -> isolate -> inspect -> hypothesize -> change -> verify.

# 11. Logging
logging.basicConfig(level=logging.INFO)
logging.info("application started")
logging.warning("example warning")

# 12–16. Readability, naming, organization, PEP 8, documentation
# Good names and small focused functions are easier to test and maintain.
def calculate_total(price: float, quantity: int) -> float:
    """Return the total price for a quantity of items."""
    return price * quantity

print("documented function:", calculate_total(10.0, 3))
