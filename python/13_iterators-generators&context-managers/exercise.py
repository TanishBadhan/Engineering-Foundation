"""Runnable examples for Iterators, Generators & Context Managers."""

# 1–3. Iterator protocol
class CountUp:
    def __init__(self, stop):
        self.current = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

iterator = CountUp(3)
print("iterator:", next(iterator), next(iterator), next(iterator))
try:
    next(iterator)
except StopIteration:
    print("iterator exhausted")

# 4. Custom iterators can implement any desired sequence behavior.

# 5–7. Generator function, yield, and preserved state
def count_up(stop):
    current = 1
    while current <= stop:
        yield current
        current += 1

generator = count_up(3)
print("generator object:", generator)
print("generator values:", list(generator))

# 8. Generator expression
squares = (x * x for x in range(4))
print("generator expression:", list(squares))

# 9. Lazy evaluation
lazy = (x * x for x in range(1_000_000))
print("lazy first value:", next(lazy))

# 10–13. Context manager protocol
class ManagedMessage:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")
        return False  # do not suppress exceptions

with ManagedMessage() as resource:
    print("inside with:", resource)

# 14. Resource lifecycle: acquire -> use -> release.
