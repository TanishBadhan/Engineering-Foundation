# 3. Operators & Expressions

Operators combine values into expressions, and a small set of evaluation rules (precedence, associativity, short-circuiting) determines exactly what any expression produces. This module treats operators not as syntax to memorize, but as a formal system: each operator has a defined arity, a return type, and a place in a total evaluation order.

---

## 📖 Subtopics

### 1. Arithmetic Operators — `+ - * / // % **`
Standard numeric operations. Two are non-obvious: `/` is **true division** and always returns a `float`, even `6 / 2 → 3.0`; `//` is **floor division**, rounding toward negative infinity (`-7 // 2 == -4`, not `-3`). `%` returns the remainder with the *same sign as the divisor*, which is why Python's modulo differs from C's for negative operands.
> **Analogy:** `/` is exact division on paper; `//` is division where you only keep whole steps and discard the rest.

### 2. Comparison Operators — `== != > < >= <=`
Compare two values and always yield a `bool`. Python supports **chained comparisons**: `1 < x < 10` is a single expression equivalent to `1 < x and x < 10`, not `(1 < x) < 10`. Comparing objects of unrelated types (`3 < "3"`) raises `TypeError` — Python refuses to guess an ordering across types.

### 3. Assignment Operators — `= += -= *= //= **=` etc.
`=` binds a name to an object; `+=` and friends are shorthand for "compute then rebind." For immutable operands (`int`, `str`), `x += 1` always creates a new object. For mutable operands (`list`), `x += [1]` may mutate in place via `__iadd__` — a subtlety that matters once two names reference the same list.

### 4. Logical Operators — `and or not`
Operate on truthiness, not strictly on booleans — `and`/`or` return one of their **actual operands**, not necessarily `True`/`False` (`"" or "default"` returns `"default"`, the string itself).
> **Analogy:** `and` is a series circuit — both switches must close for current to flow; `or` is a parallel circuit — either switch suffices; `not` simply flips a switch's state.

### 5. Identity Operators — `is` / `is not`
Test whether two names reference the **exact same object in memory** (compare via `id()`), not whether their contents are equal. `[1,2] == [1,2]` is `True`; `[1,2] is [1,2]` is `False` — two distinct list objects with matching contents. Reserve `is` for identity-sensitive checks, chiefly `is None`, `is True`, `is False`.

### 6. Membership Operators — `in` / `not in`
Test containment. Semantically simple, but performance is *not* uniform across types: `in` on a `list`/`tuple` is O(n) (linear scan); `in` on a `set`/`dict` is O(1) on average (hash lookup). Choosing the right container is often the difference between a script and a bottleneck.

### 7. Bitwise Operators — `& | ^ ~ << >>`
Operate on the binary representation of integers: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT / two's-complement negation), `<<`/`>>` (shift left/right, equivalent to multiplying/dividing by a power of 2). `~x` evaluates to `-x - 1`, a common surprise rooted in two's-complement representation.
> **Analogy:** think of each integer as a row of light switches; bitwise operators flip or combine those switches position by position, independent of the number's "value" as a whole.

### 8. Operator Precedence
The fixed ranking that decides which operator binds first in an expression with no parentheses — e.g. `**` binds tighter than unary `-`, which binds tighter than `*`/`/`, which binds tighter than `+`/`-`, which binds tighter than comparisons, which bind tighter than `not`, then `and`, then `or`. When in doubt, add parentheses — precedence rules exist so code *can* omit them, not so it *should*.

### 9. Associativity
For operators sharing the same precedence level, associativity decides the grouping direction. Almost everything is **left-to-right** (`10 - 3 - 2` groups as `(10-3)-2 = 5`). The one common exception is `**`, which is **right-to-left** (`2 ** 3 ** 2` groups as `2 ** (3 ** 2) = 512`, not `(2**3)**2 = 64`).

### 10. Expressions vs. Statements
An **expression** evaluates to a value and can appear anywhere a value is expected (`3 + 4`, `f(x)`, `a if cond else b`). A **statement** performs an action and has no value of its own (`x = 5`, `import os`, `if cond:`). The distinction matters because it defines what can legally be nested inside what — you can pass an expression as a function argument; you cannot pass a statement.

### 11. Truth Values & Truthiness
Every Python object has an implicit boolean interpretation used by `if`, `while`, and the logical operators. An object is **falsy** if it is "empty or zero-like": `0`, `0.0`, `None`, `False`, `""`, `[]`, `{}`, `set()`. Everything else is **truthy** — including a list containing only `False`, since the list itself is non-empty. Custom classes can override this via `__bool__` or `__len__`.

### 12. Short-Circuit Evaluation
`and`/`or` stop evaluating as soon as the outcome is guaranteed: `and` short-circuits on the first falsy operand (later operands never run); `or` short-circuits on the first truthy operand. This isn't just an optimization — it's routinely relied upon for safety, e.g. `obj is not None and obj.value > 0` avoids ever calling `.value` on `None`.

---

## 🗂️ Files
```text
03_operators&expressions/
├── examples.py    # Annotated, runnable demonstrations of every subtopic
├── practice.py    # Practice exercises (no answers given away)
└── README.md      # This file
```