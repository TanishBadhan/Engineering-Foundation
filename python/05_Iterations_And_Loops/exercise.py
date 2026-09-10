"""05_loops / examples.py — runnable demos, one section per subtopic."""

# --- FOR LOOPS ---

# Iteration fundamentals: what `for` does under the hood
nums = [10, 20, 30]
it = iter(nums)
print("1.", next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("1. iterator exhausted")

# Iterating sequences vs dictionaries
person = {"name": "Ana", "role": "dev"}
for key in person:                     # keys by default
    print("2. key:", key)
for key, value in person.items():      # key-value pairs
    print("2.", key, "->", value)

# range()
for i in range(3):
    print("3. i =", i)

# Nested for loops
for row in range(2):
    for col in range(2):
        print(f"4. ({row},{col})")

# Loop variables, break, continue, pass
for n in range(10):
    if n == 5:
        break              # stop entirely
    if n % 2 == 0:
        continue           # skip to next iteration
    print("5. odd:", n)

# for...else — runs only if no break occurred
target = 99
for n in [1, 2, 3]:
    if n == target:
        break
else:
    print("6. target not found")

# enumerate() and zip()
fruits = ["apple", "banana"]
for idx, fruit in enumerate(fruits):
    print("7.", idx, fruit)

prices = [1.5, 0.5]
for fruit, price in zip(fruits, prices):
    print("7b.", fruit, price)

# Reverse iteration
for fruit in reversed(fruits):
    print("8.", fruit)

# Common mistake: mutating a list while iterating (shown safely, via a copy)
original = [1, 2, 3, 4]
for item in list(original):   # iterate over a copy
    if item % 2 == 0:
        original.remove(item)
print("9. safely filtered:", original)

# --- WHILE LOOPS ---

# Loop condition / state-controlled iteration
count = 0
while count < 3:
    print("10. count =", count)
    count += 1

# Infinite loop with break-based termination
n = 0
while True:
    if n >= 3:
        break
    print("11. n =", n)
    n += 1

# while...else
n = 0
while n < 3:
    n += 1
else:
    print("12. while completed normally")

# Counters and accumulators
total = 0
counter = 0
for value in [5, 10, 15]:
    total += value      # accumulator
    counter += 1        # counter
print("13. total:", total, "count:", counter)

# Sentinel-controlled loop
inputs = ["go", "go", "quit", "ignored"]
i = 0
while inputs[i] != "quit":
    print("14. processing:", inputs[i])
    i += 1
print("14. stopped at sentinel")

# --- ITERATION CONCEPTS ---

# Iterable vs iterator — a list can spawn many independent iterators
nums = [1, 2, 3]
it1 = iter(nums)
it2 = iter(nums)
print("15.", next(it1), next(it2))   # both start at the beginning independently

# Generators — lazy, one value at a time
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(3):
    print("16.", val)

# Generator expression
squares = (x ** 2 for x in range(5))
print("17.", list(squares))

# Memory-efficient iteration — sum over a generator, no full list built
total = sum(x for x in range(1000))
print("18. total:", total)