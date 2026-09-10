# 4. Conditional Logic

Conditionals are how a program makes decisions — routing execution down one path or another based on a boolean expression. This module covers Python's branching syntax and, just as importantly, how to *design* decision logic that stays readable as it grows.

---

## 📖 Subtopics

### 1. `if`
The basic branch: a block runs only when its condition evaluates truthy. The condition can be any expression — Python evaluates its truthiness, not just literal `True`/`False`.
```python
if balance < 0:
    print("overdrawn")
```

### 2. `elif`
Short for "else if" — checks an additional condition **only if** every prior `if`/`elif` in the chain was falsy. Conditions are evaluated top to bottom, and Python stops at the **first** one that's true — later branches are never even checked.

### 3. `else`
The catch-all: runs when none of the preceding `if`/`elif` conditions were true. Not mandatory — a chain can end at `elif` with no fallback branch.

### 4. Nested Conditions
An `if` block containing another `if` inside it, for decisions that depend on more than one independent question answered in sequence.
> **Analogy:** a flowchart with sub-branches — you don't ask the second question until the first one routes you there.
Deep nesting (4+ levels) is a common readability smell — often flattenable with combined conditions or early `return`s.

### 5. Multiple Conditions
Testing several conditions together, either as a chain of `elif`s (mutually exclusive branches) or combined into one boolean expression with `and`/`or` (a single branch with a compound test).

### 6. Boolean Expressions
Any expression that reduces to `True`/`False` (or something truthy/falsy) — comparisons, logical combinations, or even a plain variable. Conditionals don't require a literal `bool`; they require *anything Python can evaluate for truthiness*.

### 7. Truthiness
Every object has an implicit boolean value: empty/zero-like values (`0`, `""`, `[]`, `None`) are falsy, everything else is truthy. This lets you write `if items:` instead of `if len(items) > 0:` — more idiomatic, and it works uniformly across types.

### 8. Conditional Expressions (Ternary)
A compact `if/else` that produces a **value** rather than choosing a block to run: `x if condition else y`. Best for short, simple value selection — nesting ternaries reduces readability fast and should generally be avoided.
```python
status = "adult" if age >= 18 else "minor"
```

### 9. Chained Comparisons
Python allows `a < b < c` as a single readable expression, equivalent to `a < b and b < c` but evaluating the shared middle term only once.

### 10. Short-Circuit Logic
`and`/`or` stop evaluating as soon as the result is determined, which lets you write conditions where an earlier check guards a later, riskier one on the same line — `obj is not None and obj.value > 0`.

### 11. Combining Logical Operators
Mixing `and`, `or`, and `not` in one expression requires understanding precedence (`not` binds tightest, then `and`, then `or`) — when combining more than two conditions, use parentheses to make the intended grouping explicit rather than relying on memorized precedence.

### 12. Designing Readable Decision Logic
As branching logic grows, raw nested `if`s become hard to follow. Techniques that help: **guard clauses** (handle edge cases early and return, instead of wrapping the "main" logic in a deep `else`), naming complex conditions as a variable (`is_eligible = age >= 18 and has_id`), and keeping each branch doing one clear thing.
> **Analogy:** a well-designed decision tree reads like a series of short questions asked once each — not a maze you have to retrace to follow.

---

## 🗂️ Files
```text
04_conditionals/
├── examples.py    # Annotated, runnable demonstrations of every subtopic
├── practice.py    # Practice exercises (no answers given away)
└── README.md      # This file
```