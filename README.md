# Engineering Foundations

A structured repository for developing strong foundations in programming, software, and engineering through **conceptual understanding, deliberate practice, and implementation**.

The repository is organized progressively. Each topic is studied from its fundamental concepts to the level required to understand how the underlying programming framework works and apply it independently.

---

## 📚 Current Learning

### 1. Python

Python is being studied systematically, from core language fundamentals through the major concepts required for writing, understanding, and reasoning about Python programs.

📁 `python/`

#### 1. Variables & Object Model

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
  
📁 `python/01_variables`

#### 2. Data Types & Data Structures

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

#### 3. Operators & Expressions

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

#### 4. Conditional Logic

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

#### 5. Iteration & Loops

##### `for` Loops

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

##### `while` Loops

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

##### Iteration Concepts

* Iterable vs iterator
* Lazy iteration
* Iterator exhaustion
* Generators
* Generator expressions
* Memory-efficient iteration

#### 6. Strings

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

#### 7. Functions

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

#### 8. Comprehensions & Functional Patterns

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

#### 9. Modules & Packages

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

#### 10. Object-Oriented Programming

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

#### 11. Error Handling & Exceptions

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

#### 12. File I/O

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

#### 13. Iterators, Generators & Context Managers

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

#### 14. Decorators & Closures

* Nested functions
* Closures
* Free variables
* Function decorators
* Decorator syntax
* Preserving metadata with `functools.wraps`
* Decorators with arguments
* Practical decorator patterns

#### 15. Python Internals & Execution Model

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

#### 16. Standard Library Foundations

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

#### 17. Testing & Code Quality

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

#### 18. Type System & Modern Python

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

#### 19. Concurrency Foundations

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

### 2. SQL & PostgreSQL

SQL and PostgreSQL are studied progressively from relational database fundamentals through querying, schema design, transactions, advanced SQL, and database-side programming.

📁 `postgresql/`

#### Foundations

* Database fundamentals
* Relational databases
* SQL command categories
* PostgreSQL CLI / `psql`

#### Database Structure

* Database creation
* Table creation
* Data types
* Constraints
* Primary keys
* Unique constraints
* NOT NULL
* CHECK constraints
* Default values

#### Data Manipulation & Querying

* INSERT
* UPDATE
* DELETE
* SELECT
* Filtering
* WHERE
* ORDER BY
* LIMIT
* Aggregate functions
* GROUP BY
* HAVING
* String functions

#### Schema & Relational Modeling

* ALTER TABLE
* Relationships
* Foreign keys
* JOINs
* Referential integrity
* CASE
* COALESCE

#### Transactions

* Transactions
* COMMIT
* ROLLBACK
* SAVEPOINT
* Transaction Control Language (TCL)
* ACID fundamentals

#### Advanced SQL

* Views
* Common Table Expressions (CTEs)
* Window functions
* PARTITION BY
* Ranking and analytical queries

#### Database Programming

* User-defined functions
* Stored procedures
* Triggers

#### Practice Environment

The PostgreSQL topics use a shared practice database defined through:

📁 `postgresql/00_setup/schema.sql`  
📁 `postgresql/00_setup/seed.sql`

The PostgreSQL path is designed to build practical SQL ability for **backend engineering, data-intensive applications, production systems, analytics, and technical interviews**.

---

### 3. Linux

Linux is studied as the command-line and operating-system foundation required for **servers, backend systems, cloud infrastructure, containers, CI/CD, networking, databases, and AI infrastructure**.

📁 `linux/`

#### Linux Learning Path

1. Linux & Shell Fundamentals
2. Filesystem & Navigation
3. Files & Directories
4. Reading & Inspecting Files
5. Search & Text Processing
6. Pipes, Redirection & Shell Control
7. Processes & Job Control
8. Disk & System Resources
9. Users, Ownership & Permissions
10. Environment Variables & PATH
11. Archives & Compression
12. Shell Editing & Productivity
13. Services & System Logs
14. Linux Networking
15. SSH & Remote Computing
16. Basic Bash Scripting

The path progresses from **command-line fundamentals → filesystem → text processing → processes → permissions → networking → remote computing → automation**.

The goal is not command memorization. The goal is to understand how Linux is **operated, inspected, troubleshot, and automated** in real engineering environments.

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
│   ├── 01_variables&objectmodel/
│   ├── 02_DataTypes_And_DataStructures/
│   ├── 03_operators&expressions/
│   ├── 04_Conditional_logics/
│   ├── 05_Iterations_And_Loops/
│   ├── 06_strings/
│   ├── 07_functions/
│   ├── 08_comprehensions&functionalpatterns/
│   ├── 09_modules&packages/
│   ├── 10_object-oriented-programming/
│   ├── 11_error-handling&exceptions/
│   ├── 12_file-io/
│   ├── 13_iterators-generators&context-managers/
│   ├── 14_decorators&closures/
│   ├── 15_python-internals&execution-model/
│   ├── 16_standard-library-foundations/
│   ├── 17_testing&code-quality/
│   ├── 18_type-system&modern-python/
│   └── 19_concurrency-foundations/
│
├── postgresql/
│   ├── 00_setup/
│   ├── 01_database_fundamentals/
│   ├── 02_sql_command_categories/
│   ├── 03_postgresql_cli/
│   ├── 04_database_and_table_creation/
│   ├── 05_data_types/
│   ├── 06_constraints/
│   ├── 07_insert_update_delete/
│   ├── 08_select_and_filtering/
│   ├── 09_aggregate_functions/
│   ├── 10_group_by_and_having/
│   ├── 11_string_functions/
│   ├── 12_alter_table/
│   ├── 13_relationships_and_foreign_keys/
│   ├── 14_joins/
│   ├── 15_case_and_coalesce/
│   ├── 16_transactions_and_tcl/
│   ├── 17_views/
│   ├── 18_ctes/
│   ├── 19_window_functions/
│   ├── 20_user_defined_functions/
│   ├── 21_stored_procedures/
│   └── 22_triggers/
│
└── README.md
```

Each topic may contain:

```text
topic/
├── README.md
├── practice.py / practice.sql
└── fundamentals.py / supporting files
```

---

## 📈 Progress

| Area | Status |
|---|---|
| Python Fundamentals | 🟢 In Progress |
| SQL & PostgreSQL | 🟢 In Progress |
| Linux | 🟢 In Progress |

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
