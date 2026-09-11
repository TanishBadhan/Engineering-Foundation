# 17. Testing & Code Quality

Testing checks whether software behaves as intended. Code quality makes that software understandable, maintainable, debuggable, and safer to change. Tests are not a replacement for reasoning; they are executable evidence of expected behavior.

## 📖 Subtopics

### 1. Assertions
Assertions state conditions that should be true at a particular point in code or tests.

### 2. `assert`
`assert condition` raises `AssertionError` when the condition is false. Do not use assertions as a substitute for user-input validation because assertions can be disabled with optimization.

### 3. Testing fundamentals
A useful test has a clear setup, action, and expected result. Tests should be deterministic and focused.

### 4. Unit testing concepts
Unit tests isolate a small unit of behavior. Integration tests instead verify interactions between components.

### 5. `unittest`
Python's standard-library testing framework provides test cases, assertions, fixtures, and a test runner.

### 6. `pytest` fundamentals
`pytest` offers simple test functions, rich assertions, fixtures, parametrization, and a large plugin ecosystem.

### 7. Test organization
Keep tests discoverable and group them logically, commonly in a `tests/` directory with names such as `test_*.py`.

### 8. Edge cases
Test boundaries, empty inputs, invalid inputs, unusual values, and conditions likely to expose hidden assumptions.

### 9. Defensive programming
Validate important assumptions and fail clearly at system boundaries. Avoid defensive code that obscures normal logic without reducing real risk.

### 10. Debugging
Reproduce the failure, isolate the cause, inspect state, form a hypothesis, change the smallest necessary thing, and verify the fix.

### 11. Logging fundamentals
Logging records useful runtime information with levels such as DEBUG, INFO, WARNING, ERROR, and CRITICAL. It is preferable to scattered print statements in production software.

### 12. Readability
Code should communicate intent clearly through structure, names, and reasonable abstraction.

### 13. Naming
Use descriptive, consistent names. Follow Python conventions such as `snake_case` for functions and variables and `PascalCase` for classes.

### 14. Code organization
Separate responsibilities into functions/modules/classes with clear boundaries and minimize unnecessary coupling.

### 15. PEP 8
PEP 8 provides widely used Python style guidance for formatting and naming. Automated formatters and linters can enforce much of it.

### 16. Documentation
Document public behavior, assumptions, usage, and non-obvious decisions. Good code should still be understandable without excessive comments.

## 🧠 Core Concepts

- Tests specify behavior; they are part of the development process, not decoration.
- Test edge cases and failure paths, not only the happy path.
- Logging and debugging solve different problems: logs record runtime behavior; debugging investigates causes.
- Quality includes correctness, readability, maintainability, and predictable behavior.

## ⚠️ Common Mistakes

- Testing implementation details instead of observable behavior.
- Writing tests that depend on timing, global state, or external services unnecessarily.
- Using `assert` for input validation.
- Catching bugs by deleting or weakening the test that exposes them.
- Treating formatting as the entire definition of code quality.

## 🗂️ Files

- `exercise.py` — runnable examples for assertions, unittest, pytest-style tests, and logging.
- `fundamentals.py` — 10 testing and code-quality exercises.

## 🎯 Expected Outcome

You should be able to write focused tests, reason about edge cases, debug systematically, and organize Python code with professional readability and documentation.