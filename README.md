# Engineering Foundations

A structured repository for developing strong foundations in programming, software, and engineering through **conceptual understanding, deliberate practice, and implementation**.

The repository is organized progressively. Each topic is studied from its fundamental concepts to the level required to understand how the underlying programming framework works and apply it independently.

---

## 📚 Current Learning

### Python

Python is being studied systematically, from core language fundamentals through the major concepts required for writing, understanding, and reasoning about Python programs.

📁 `python/`

### 1. Variables & Object Model

* Variables and assignment
* Naming conventions and identifiers
* Dynamic typing
* Strong typing
* Reassignment
* Multiple assignment
* Unpacking
* Object references
* Identity vs equality
* `id()`
* `is` vs `==`
* Mutable vs immutable objects
* Namespaces and scope fundamentals

### 2. Data Types & Data Structures

* Integers
* Floating-point numbers
* Complex numbers
* Booleans
* Strings
* `None`
* Type conversion and coercion
* Lists
* Tuples
* Sets
* Dictionaries
* Nested data structures
* Mutability and immutability
* Hashability
* Indexing
* Slicing
* Membership
* Common built-in operations
* Built-in functions

### 3. Operators & Expressions

* Arithmetic operators
* Comparison operators
* Assignment operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators
* Operator precedence
* Associativity
* Expressions vs statements
* Truth values and truthiness
* Short-circuit evaluation

### 4. Conditional Logic

* `if`
* `elif`
* `else`
* Nested conditions
* Multiple conditions
* Boolean expressions
* Truthiness
* Conditional expressions
* Chained comparisons
* Short-circuit logic
* Combining logical operators
* Designing readable decision logic

### 5. Iteration & Loops

#### `for` Loops

* Iteration fundamentals
* Iterables
* Iterators
* `iter()`
* `next()`
* Iteration protocol
* Iterating over sequences
* Iterating over dictionaries
* `range()`
* Nested `for` loops
* Loop variables
* `break`
* `continue`
* `pass`
* `for...else`
* Enumerating with `enumerate()`
* Parallel iteration with `zip()`
* Reverse iteration
* Iteration patterns
* Common iteration mistakes

#### `while` Loops

* Loop conditions
* State-controlled iteration
* Infinite loops
* Loop termination
* `break`
* `continue`
* `while...else`
* Nested `while` loops
* Counters and accumulators
* Sentinel-controlled loops
* Designing safe loop conditions

#### Iteration Concepts

* Iterable vs iterator
* Lazy iteration
* Iterator exhaustion
* Generators
* Generator expressions
* Memory-efficient iteration

### 6. Strings

* String creation
* Indexing and slicing
* Immutability
* String methods
* Searching and replacing
* Splitting and joining
* Whitespace handling
* Formatting
* f-strings
* Escape sequences
* Raw strings
* String comparison
* Iterating over strings
* Practical string-processing patterns

### 7. Functions

* Defining functions
* Calling functions
* Parameters and arguments
* Positional arguments
* Keyword arguments
* Default arguments
* Variable-length arguments
* `*args`
* `**kwargs`
* Return values
* Multiple return values
* Scope
* Local and global variables
* `global`
* `nonlocal`
* Function composition
* First-class functions
* Functions as objects
* Higher-order functions
* Lambda functions
* Recursion
* Documentation and docstrings
* Type hints
* Pure vs impure functions

### 8. Comprehensions & Functional Patterns

* List comprehensions
* Set comprehensions
* Dictionary comprehensions
* Conditional comprehensions
* Nested comprehensions
* Generator expressions
* `map()`
* `filter()`
* `reduce()`
* `sorted()`
* `key=`
* When comprehensions improve code
* When comprehensions become harmful to readability

### 9. Modules & Packages

* Importing modules
* `import`
* `from ... import`
* Aliases
* Module namespaces
* Creating custom modules
* Packages
* `__init__.py`
* Absolute imports
* Relative imports
* `__name__`
* `if __name__ == "__main__"`
* Python's import mechanism
* Standard library fundamentals

### 10. Object-Oriented Programming

* Classes
* Objects
* Attributes
* Methods
* Constructors
* `__init__`
* Instance attributes
* Class attributes
* Instance methods
* Class methods
* Static methods
* `self`
* Encapsulation
* Abstraction
* Inheritance
* Method overriding
* Polymorphism
* Composition
* Aggregation
* Association
* Multiple inheritance
* Method Resolution Order (MRO)
* `super()`
* Special / dunder methods
* Operator overloading
* Properties
* Getters and setters
* Dataclasses
* Abstract base classes
* Interfaces through protocols / duck typing

### 11. Error Handling & Exceptions

* Errors vs exceptions
* Syntax errors
* Runtime errors
* Logical errors
* Exception hierarchy
* `try`
* `except`
* `else`
* `finally`
* Raising exceptions
* `raise`
* Custom exceptions
* Exception propagation
* Handling specific vs broad exceptions
* Designing reliable error handling

### 12. File I/O

* Files and file paths
* Opening files
* Reading files
* Writing files
* Appending files
* File modes
* Text vs binary files
* `with` statement
* Context managers
* `read()`
* `readline()`
* `readlines()`
* Iterating over files
* Writing structured data
* CSV fundamentals
* JSON fundamentals
* File handling errors
* Resource management

### 13. Iterators, Generators & Context Managers

* Iterator protocol
* `__iter__`
* `__next__`
* Custom iterators
* Generator functions
* `yield`
* Generator state
* Generator expressions
* Lazy evaluation
* Context managers
* `__enter__`
* `__exit__`
* `with`
* Resource lifecycle

### 14. Decorators & Closures

* Nested functions
* Closures
* Free variables
* Function decorators
* Decorator syntax
* Preserving metadata with `functools.wraps`
* Decorators with arguments
* Practical decorator patterns

### 15. Python Internals & Execution Model

* Source code to execution
* Bytecode fundamentals
* Python interpreter
* Namespaces
* Scope and LEGB
* Object model
* References
* Memory concepts
* Garbage collection fundamentals
* Reference counting
* Shallow vs deep copying
* `copy`
* `deepcopy`
* Mutability and object sharing

### 16. Standard Library Foundations

* `math`
* `random`
* `datetime`
* `os`
* `pathlib`
* `sys`
* `collections`
* `itertools`
* `functools`
* `re`
* `json`
* `csv`
* `statistics`

The goal is not to memorize the entire standard library, but to understand the major tools available and know how to use documentation effectively.

### 17. Testing & Code Quality

* Assertions
* `assert`
* Testing fundamentals
* Unit testing concepts
* `unittest`
* `pytest` fundamentals
* Test organization
* Edge cases
* Defensive programming
* Debugging
* Logging fundamentals
* Readability
* Naming
* Code organization
* PEP 8
* Documentation

### 18. Type System & Modern Python

* Type annotations
* Built-in generic types
* `Optional`
* `Union`
* `Any`
* Type aliases
* `Callable`
* Generics fundamentals
* Static type checking concepts
* `typing`
* Structural typing fundamentals

### 19. Concurrency Foundations

* Processes vs threads
* Threading fundamentals
* Multiprocessing fundamentals
* Concurrency vs parallelism
* Synchronization concepts
* Async programming fundamentals
* `async`
* `await`
* Event loops
* `asyncio`
* When concurrency is useful

---

## 🧠 Learning Standard

The objective is not to memorize Python syntax.

For each major concept, the focus is on understanding:

**What it is → Why it exists → How it works → When to use it → Common mistakes → Practical application**

The depth increases progressively without introducing unnecessary complexity or obscure language details.

---

## 🗂️ Repository Structure

```text
Engineering-Foundations/
│
├── python/
│   ├── 01_variables/
│   ├── 02_data_types/
│   ├── 03_operators/
│   ├── 04_conditionals/
│   ├── 05_loops/
│   ├── 06_strings/
│   ├── 07_functions/
│   ├── 08_comprehensions/
│   ├── 09_modules_packages/
│   ├── 10_oop/
│   ├── 11_exceptions/
│   ├── 12_file_io/
│   ├── 13_iterators_generators/
│   ├── 14_decorators_closures/
│   ├── 15_python_internals/
│   ├── 16_standard_library/
│   ├── 17_testing/
│   ├── 18_type_system/
│   └── 19_concurrency/
│
└── README.md
```

Each topic may contain:

```text
topic/
├── examples.py
├── practice.py
└── README.md
```

---

## 📈 Progress

| Area                | Status         |
| ------------------- | -------------- |
| Python Fundamentals | 🟢 In Progress |

Progress will be updated as topics are completed.

---

## 🔄 Version Control

Git and GitHub are used to track the repository and document meaningful learning milestones.

Commits are organized around substantive progress rather than arbitrary file changes.

---

## 👤 Author

**Tanish Badhan**

GitHub: [TanishBadhan](https://github.com/TanishBadhan)

---

> Engineering Foundations is built progressively: understand the fundamentals deeply, practice them deliberately, and use them to build increasingly capable systems.
