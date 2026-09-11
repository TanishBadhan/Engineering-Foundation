# 15. Python Internals & Execution Model

Python hides many runtime details behind simple syntax. Understanding the execution model helps explain names, references, mutability, copying, memory behavior, and why seemingly similar operations can behave differently.

## 📖 Subtopics

### 1. Source code to execution
Python source is parsed and compiled to bytecode, which a Python implementation executes through its runtime machinery. Exact internals vary by implementation and version.

### 2. Bytecode fundamentals
Bytecode is an intermediate instruction representation. The `dis` module can inspect CPython bytecode for learning and debugging.

### 3. Python interpreter
The interpreter executes Python code according to the language implementation. CPython is the reference implementation most commonly encountered.

### 4. Namespaces
A namespace maps names to objects. Common namespaces include local, enclosing, global, and built-in namespaces.

### 5. Scope and LEGB
Name lookup generally follows Local → Enclosing → Global → Built-in for lexical scopes.

### 6. Object model
Variables are names bound to objects. Objects have identity, type, and value/state.

### 7. References
Assignment usually binds another name to an existing object rather than copying the object.

### 8. Memory concepts
Objects live in memory managed by the Python runtime. The language does not require you to manually allocate and free ordinary objects.

### 9. Garbage collection fundamentals
Python implementations reclaim objects that are no longer reachable. CPython combines reference counting with cyclic garbage collection.

### 10. Reference counting
In CPython, an object's reference count tracks references to it. When the count reaches zero, deallocation can happen immediately, although cyclic structures require additional handling.

### 11. Shallow vs deep copying
A shallow copy creates a new outer object but keeps references to nested objects. A deep copy recursively copies nested structures where possible.

### 12. `copy`
The `copy` module provides `copy.copy()` for shallow copying and `copy.deepcopy()` for deep copying.

### 13. `deepcopy`
`deepcopy()` recursively copies reachable objects while maintaining a memo to handle shared references and cycles.

### 14. Mutability and object sharing
Mutable objects can change in place; immutable objects cannot. Multiple names may refer to the same mutable object, so changes can be visible through all aliases.

## 🧠 Core Concepts

- Assignment is binding, not automatic copying.
- Identity (`is`) and equality (`==`) answer different questions.
- Mutability explains many aliasing surprises.
- Shallow copies share nested objects; deep copies attempt to duplicate them.
- CPython implementation details should not be confused with guarantees of the Python language itself.

## ⚠️ Common Mistakes

- Saying “variables contain values” without considering object references.
- Using `is` for ordinary value equality.
- Assuming `list.copy()` deep-copies nested lists.
- Relying on reference-count timing as portable Python behavior.
- Treating implementation details as universal language guarantees.

## 🗂️ Files

- `exercise.py` — runnable examples using `dis`, identity, copying, and references.
- `fundamentals.py` — 10 reasoning problems.

## 🎯 Expected Outcome

You should be able to reason about names, objects, references, scope, mutability, copying, and basic CPython execution without needing to become an interpreter developer.