# 01 — Variables

Variables are one of the most fundamental concepts in programming. In Python, a variable is a **name that refers to an object stored in memory**.

Understanding variables properly is important because concepts such as data types, functions, objects, mutability, memory management, scope, and data structures all build on this foundation.

---

## 1. Learning Objectives

* Understand what a variable represents in Python
* Create and assign variables
* Explain Python's name-binding model
* Understand objects and references
* Identify variable names and values
* Understand Python's dynamic typing
* Reassign variables safely
* Follow Python naming conventions
* Understand multiple assignment
* Understand chained assignment
* Swap variables
* Understand constant conventions
* Understand object identity at a basic level
* Understand how variables behave with mutable and immutable objects
* Understand local and global variables at a foundational level
* Identify common variable-related mistakes

---

# 2. What Is a Variable?

A variable is a **name used to refer to an object**.

Example:

```python
age = 19
```

Conceptually:

```text
age ───────► 19
             object
```

Python does not require us to declare the variable's type separately.

```python
age = 19
name = "Tanish"
height = 5.9
```

Python determines the type from the object assigned to the name.

---

# 3. Variable Assignment

The `=` operator is used for assignment.

```python
x = 10
```

This means:

> Bind the name `x` to the object `10`.

It does **not** mean mathematical equality.

```python
x = x + 1
```

This is valid because Python first evaluates:

```python
x + 1
```

and then assigns the resulting object back to `x`.

---

# 4. Variables Are Names, Not Boxes

A common beginner mental model is:

```text
x = [10, 20, 30]
```

thinking that `x` itself contains the list.

A better Python mental model is:

```text
x ─────────► [10, 20, 30]
              object
```

The variable is a **name/reference** associated with an object.

This distinction becomes extremely important when learning:

* Mutable objects
* Immutable objects
* Function arguments
* Shallow copies
* Deep copies
* Object identity
* Memory management

---

# 5. Dynamic Typing

Python is dynamically typed.

The type belongs to the **object**, not permanently to the variable name.

```python
x = 10
```

Here:

x → int

Later:

```python
x = "hello"
```

Now:

x → str

The same name can refer to objects of different types at different times.

```python
x = 10
x = 3.14
x = "Python"
x = True
```

This is valid Python.

---

# 6. Type Checking

Use `type()` to inspect an object's type.

```python
x = 10

print(type(x))
```

Output:

```text
<class 'int'>
```

Examples:

```python
name = "Tanish"
age = 19
height = 5.9
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

---

# 7. Variable Naming Rules

Python variable names must follow specific rules.

### Valid

```python
age = 19
student_name = "Tanish"
marks2 = 85
_private = 10
```

### Invalid

```python
2marks = 90
student-name = "Tanish"
student name = "Tanish"
```

Variable names:

* Can contain letters
* Can contain digits
* Can contain `_`
* Cannot begin with a digit
* Cannot contain spaces
* Cannot contain `-`
* Are case-sensitive
* Cannot be Python keywords

---

# 8. Case Sensitivity

Python variable names are case-sensitive.

```python
age = 19
Age = 20
AGE = 21
```

These are three different names.

```python
print(age)
print(Age)
print(AGE)
```

---

# 9. Naming Conventions

Python generally follows **snake_case** for variable names.

Recommended:

```python
student_name = "Tanish"
total_marks = 450
average_score = 90.0
```

Avoid:

```python
studentName = "Tanish"
TotalMarks = 450
```

CamelCase is generally used for classes:

```python
class StudentProfile:
    pass
```

---

# 10. Meaningful Variable Names

Prefer names that communicate intent.

Bad:

```python
x = 19
y = 450
z = 90
```

Better:

```python
age = 19
total_marks = 450
average_marks = 90
```

Good naming becomes increasingly important in large software systems.

---

# 11. Multiple Assignment

Python allows multiple variables to be assigned in one statement.

```python
x, y, z = 10, 20, 30
```

Equivalent conceptually to:

```python
x = 10
y = 20
z = 30
```

---

# 12. Assigning the Same Value to Multiple Variables

```python
x = y = z = 100
```

All three names refer to the assigned object.

For immutable objects such as integers, this is generally straightforward.

For mutable objects, however, shared references can produce surprising behavior:

```python
a = b = []
```

Now:

```text
a ─────► []
          ▲
b ────────┘
```

Both names refer to the **same list object**.

---

# 13. Variable Swapping

Python supports direct variable swapping.

```python
a = 10
b = 20

a, b = b, a
```

Now:

```python
a == 20
b == 10
```

No temporary variable is required.

---

# 14. Reassignment

A variable can be reassigned.

```python
score = 50
score = 75
score = 90
```

The name `score` is rebound to a new object.

This is different from modifying an existing mutable object.

---

# 15. Assignment vs Modification

Consider:

```python
x = 10
x = 20
```

The name is rebound.

Compare that with:

```python
numbers = [1, 2, 3]
numbers.append(4)
```

The existing list object is modified.

This distinction is fundamental when learning Python's object model.

---

# 16. Mutable vs Immutable Objects

Some objects can be modified after creation.

Examples of commonly mutable objects:

```text
list
dict
set
```

Examples of commonly immutable objects:

```text
int
float
bool
str
tuple
```

Example:

```python
x = 10
```

Integers are immutable.

When we do:

```python
x = x + 1
```

Python does not modify the integer `10`.

A new integer object is produced and `x` is rebound to it.

---

# 17. Object Identity

Python provides `id()` to inspect an object's identity.

```python
x = 10

print(id(x))
```

The exact value is implementation-dependent and should not normally be treated as a meaningful memory address.

The `is` operator checks whether two names refer to the same object.

```python
a = []
b = a

print(a is b)
```

Output:

```text
True
```

`==` and `is` are **not interchangeable**.

```python
a == b
```

checks value equality.

```python
a is b
```

checks object identity.

---

# 18. Variables and References

Example:

```python
a = [1, 2, 3]
b = a
```

Conceptually:

```text
a ───────┐
         ▼
       [1, 2, 3]
         ▲
         │
b ───────┘
```

Therefore:

```python
b.append(4)

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

Why?

Because `a` and `b` refer to the same list object.

---

# 19. Variables and Memory

Python manages memory automatically.

As a programmer, you normally do not manually allocate and free memory for ordinary Python objects.

The Python runtime manages object lifetime using mechanisms including:

* Reference counting
* Garbage collection

At this stage, understand the conceptual model:

```text
Variable name
      ↓
Reference
      ↓
Python object
      ↓
Memory managed by Python
```

Detailed memory management will be studied separately.

---

# 20. Constants

Python does not enforce true constants at the language level.

By convention, names intended to behave as constants are written in uppercase.

```python
PI = 3.14159
MAX_CONNECTIONS = 100
DATABASE_TIMEOUT = 30
```

The convention communicates:

> Do not reassign this value.

Python technically still allows:

```python
PI = 4
```

---

# 21. Variable Scope — Foundation

A variable's scope determines where its name can be accessed.

Example:

```python
x = 10

def display():
    print(x)
```

Here `x` is defined outside the function.

A variable created inside a function normally has local scope:

```python
def display():
    y = 20
```

`y` cannot normally be accessed outside the function.

Detailed scope rules will be covered with functions and namespaces.

---

# 22. Global Variables

A variable defined at module level can be accessed from functions in many situations.

```python
count = 10

def display():
    print(count)
```

However, excessive use of global mutable state is generally discouraged in production software because it makes programs harder to reason about and test.

---

# 23. Unpacking

Python supports unpacking.

```python
numbers = [10, 20, 30]

a, b, c = numbers
```

Now:

```python
a = 10
b = 20
c = 30
```

Extended unpacking is also possible:

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
```

Result:

first  → 1
middle → [2, 3, 4]
last   → 5

---

# 24. Variable Lifetime

A variable name exists within a particular namespace and scope.

For example, local variables created during a function call generally exist only within that function's execution context.

Understanding lifetime becomes important when studying:

* Functions
* Closures
* Classes
* Modules
* Generators
* Memory management

---

# 25. Keywords Cannot Be Variable Names

Python reserves certain words for the language itself.

Examples:

if
else
for
while
class
def
return
import
try
except
True
False
None


Therefore:

```python
class = 10
```

is invalid.

You can inspect Python's keywords using:

```python
import keyword

print(keyword.kwlist)
```

---

# 26. Common Mistakes

### Mistake 1 — Starting with a number

```python
1name = "Tanish"
```

Invalid.

Correct:

```python
name1 = "Tanish"
```

---

### Mistake 2 — Using spaces

```python
student name = "Tanish"
```

Invalid.

Correct:

```python
student_name = "Tanish"
```

---

### Mistake 3 — Confusing `=` and `==`

```python
x = 10
```

Assignment.

```python
x == 10
```

Comparison.

---

### Mistake 4 — Confusing `==` and `is`

```python
a == b
```

Checks equality.

```python
a is b
```

Checks identity.

---

### Mistake 5 — Accidentally sharing a mutable object

```python
a = []
b = a
```

Changing `b` also affects the object seen through `a`.

---

### Mistake 6 — Using meaningless names

Avoid:

```python
a = 500
b = 20
c = a / b
```

Prefer:

```python
total_distance = 500
time_taken = 20
average_speed = total_distance / time_taken
```

---

# 27. Conceptual Model

The most important mental model from this topic is:

                Python Program
                       │
                       ▼
                 Variable Name
                       │
                       ▼
                  Reference
                       │
                       ▼
                  Python Object
                 ┌─────┴─────┐
                 │           │
              Value         Type
                 │           │
                 └─────┬─────┘
                       ▼
               Memory managed
                 by Python


Do not reduce variables to:

> "A variable is a container that stores a value."

A stronger understanding is:

> **A Python variable is a name bound to an object.**

---

# 28. Practical Examples

The accompanying `fundamental.py` file should contain examples covering:

* Basic assignment
* Different data types
* Reassignment
* Multiple assignment
* Chained assignment
* Variable swapping
* `type()`
* `id()`
* Equality vs identity
* Shared references
* Mutable vs immutable behavior
* Unpacking
* Naming conventions

---

# 29. Practice Requirements

The accompanying `exercise.py` file should contain exercises that test:

### Level 1 — Fundamentals

* Create variables
* Assign values
* Print variables
* Reassign variables
* Check types

### Level 2 — Application

* Calculate values using variables
* Swap variables
* Use multiple assignment
* Perform unpacking
* Build small calculations using meaningful names

### Level 3 — Conceptual

Predict the output of programs involving:

* Reassignment
* References
* `==`
* `is`
* `id()`
* Mutable objects
* Chained assignment

### Level 4 — Interview

Explain in your own words:

> Why is `a = b = []` different from `a = []; b = []`?

And:

> Why does `x = x + 1` behave differently from modifying a list with `append()`?

---

# 30. Key Takeaways

1. Variables are names.
2. Names refer to objects.
3. Objects have types and values.
4. Python is dynamically typed.
5. Assignment binds/rebinds names.
6. Multiple names can refer to one object.
7. == checks equality.
8. is checks identity.
9. Mutable objects can be changed.
10. Immutable objects cannot be changed in place.
11. Python manages memory automatically.
12. Good variable names improve code quality.

---