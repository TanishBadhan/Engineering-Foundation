# 6. Strings

Strings are immutable sequences of Unicode text — one of the most used types in any program. This module goes past the basics covered in Module 2 into how strings are actually manipulated: creation, methods, formatting, and common processing patterns.

---

## 📖 Subtopics

### 1. String Creation
Created with single, double, or triple quotes (`'`, `"`, `'''`/`"""`) — triple quotes allow multi-line strings. Single vs. double is purely stylistic (pick one, stay consistent); triple quotes matter when the text itself spans lines or contains both quote types.

### 2. Indexing and Slicing
Strings support the same `[i]` and `[start:stop:step]` syntax as lists (Module 2), since a string is a sequence of characters — but slicing a string always returns a **new string**, never modifies the original.

### 3. Immutability
Once created, a string's characters can never change in place. `.upper()`, `.replace()`, concatenation — all of these build and return a **new** string, leaving the original untouched. This is why `s.upper()` alone does nothing visible; you must capture it: `s = s.upper()`.

### 4. String Methods
Strings ship with dozens of built-in methods (`.upper()`, `.lower()`, `.strip()`, `.startswith()`, `.endswith()`, `.isdigit()`, etc.) — all return new strings or booleans, never mutate. Worth browsing `dir(str)` once to know what's available before reaching for a manual loop.

### 5. Searching and Replacing
`.find()`/`.index()` locate a substring's position (`.find()` returns `-1` if missing, `.index()` raises `ValueError`); `.replace(old, new)` returns a new string with every occurrence swapped; `in` checks existence without needing a position.

### 6. Splitting and Joining
`.split(sep)` breaks a string into a list (default: split on any whitespace); `sep.join(list)` does the reverse, stitching a list of strings into one using `sep` as glue. These are inverses of each other and among the most-used string operations in real code.

### 7. Whitespace Handling
`.strip()` removes leading/trailing whitespace, `.lstrip()`/`.rstrip()` do one side only. Essential when processing user input or file lines, which routinely carry stray spaces or trailing newlines.

### 8. Formatting
Building strings with embedded values — the older `%`-style and `.format()` methods still appear in existing code, but f-strings (below) are the modern default.

### 9. f-strings
`f"Hello {name}, you are {age} years old"` — embeds expressions directly inside `{}`, evaluated at runtime. Supports inline formatting specs (`f"{price:.2f}"` for 2 decimal places) and even inline expressions (`f"{a + b}"`). The clearest and fastest string-building tool in modern Python.

### 10. Escape Sequences
Special characters written with a backslash: `\n` (newline), `\t` (tab), `\\` (literal backslash), `\"` (literal quote inside a double-quoted string). Necessary whenever a string needs to contain a character that would otherwise break its syntax.

### 11. Raw Strings
`r"C:\new\path"` — prefixing with `r` disables escape-sequence processing, so backslashes are treated literally. Essential for file paths (Windows) and regular expressions, where backslashes are meaningful on their own and shouldn't be reinterpreted.

### 12. String Comparison
`==` compares character-by-character; `<`/`>` compare **lexicographically** (dictionary order, based on Unicode code points) — which means all uppercase letters sort before all lowercase ones (`"Z" < "a"` is `True`), a common surprise when sorting mixed-case text.

### 13. Iterating Over Strings
A `for` loop over a string yields one character at a time, since a string is just a sequence — the exact same iteration protocol covered in Module 5 applies here.

### 14. Practical String-Processing Patterns
Common real-world combinations: `.strip().split(",")` to clean and parse a CSV-style line, `" ".join(word.capitalize() for word in text.split())` to title-case a sentence, `.lower()` before comparison to make matching case-insensitive.

---

## 🗂️ Files
```text
06_strings/
├── exercise.py    # Annotated, runnable demonstrations of every subtopic
├── fundamentals.py    # Practice exercises (no answers given away)
└── README.md      # This file
```