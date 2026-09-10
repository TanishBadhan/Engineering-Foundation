"""05_loops / practice.py — fill in each TODO, no answers given."""

# 1. Iteration fundamentals: manually call iter()/next() on the list
# below to print its first two elements without a for loop.
colors = ["red", "green", "blue"]

# my sol :
it = iter(colors)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("DONE")

else:
    print("not possible")

# 2. Dictionaries: print each key AND value from `scores` using .items().
scores = {"Ana": 90, "Ben": 75}

for name, score in scores.items():
    print(name,score)
else:
    ("No Data Available")
    

# 3. range(): print all even numbers from 0 to 10 (inclusive) using range()
# with a step argument.
for i in range (11):
    if i%2==0:
        print(i)


# 4. Nested loops: print every (row, col) pair for a 3x3 grid.
for row in range(3):
    for col in range(3):
        print(row,col)

# 5. break/continue: loop through 1-20, skip multiples of 3 (continue),
# and stop entirely once you reach a number greater than 15 (break).

for i in range (1,20):
    if i > 15:
        break
    if i % 3==0:
        continue
    print(i)

# 6. for...else: search for 7 in the list below; if not found, print
# "not found" using a for...else construct.
values = [1, 3, 5, 9]

for i in values:
    if i==7:
        break
else:
    print("Not Found") 

# 7. enumerate() + zip(): given names and ages below, print
# "0: Ana is 30" style lines combining index, name, and age.
names = ["Ana", "Ben"]
ages = [30, 25]

for i, (name,age) in enumerate(zip(names,ages)):
    print(f"{i}:{name} is {age} yrs old.")
    
# 8. Reverse iteration: print `values` (above) from last to first.

for v in reversed(values):
    print(v)
    

# 9. while loop: sum numbers from 1 to 10 using a while loop and a
# counter + accumulator (no sum() or for loop allowed).
total = 0 
count = 1 
while count<=10:
    total += count
    count += 1 
print(total)

# 10. Sentinel loop: process items from `queue` below one at a time
# using a while loop, stopping when you hit "STOP" (don't process it).
queue = ["task1", "task2", "STOP", "task3"]

i=0

while queue[i] != "STOP":
    print("processing items:",queue[i])
    i += 1 

# 11. Generators: write a generator function `even_numbers(limit)` that
# yields even numbers from 0 up to (not including) limit.

def even_numbers(limit):
    n = 0
    while n < limit:
        yield n
        n += 2

for x in even_numbers(10):
    print(x)   # 0 2 4 6 8

# 12. Memory-efficient iteration: compute the sum of squares from 1 to
# 100 using a generator expression (not a list).
import sys
total = sum(x ** 2 for x in range(1, 101))
print(total)
print(sys.getsizeof(total))