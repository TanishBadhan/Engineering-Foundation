# 12. File I/O

File I/O lets programs persist and exchange data. Python's `open()` and `pathlib` provide the core tools for text and binary files, while CSV and JSON handle common structured formats. Correct resource management is essential so files are closed even when failures occur.

## 📖 Subtopics

### 1. Files and file paths
A file path identifies a file in the filesystem. Prefer `pathlib.Path` for portable path manipulation.

### 2. Opening files
`open(path, mode, encoding=...)` returns a file object. Text files should usually specify an encoding such as UTF-8.

### 3. Reading files
`read()` retrieves content; reading large files all at once may use substantial memory.

### 4. Writing files
`write()` writes text to an opened file. Writing usually replaces existing content when using `w` mode.

### 5. Appending files
`a` mode adds new content to the end without replacing existing content.

### 6. File modes
Common modes include `r` read, `w` write, `a` append, `x` exclusive creation, and combinations such as `rb` or `wb` for binary data.

### 7. Text vs binary files
Text mode decodes bytes into strings using an encoding. Binary mode works directly with bytes and is required for many images, archives, and other non-text data.

### 8. `with` statement
`with open(...) as file:` ensures the file is closed when the block exits, including through exceptions.

### 9. Context managers
A context manager defines setup and cleanup behavior through the context-management protocol and is used by `with`.

### 10. `read()`
Reads all remaining content unless a size is supplied.

### 11. `readline()`
Reads one line at a time, useful when processing a file incrementally.

### 12. `readlines()`
Returns remaining lines as a list. It can consume significant memory for large files.

### 13. Iterating over files
`for line in file` streams lines efficiently and is usually preferable for large text files.

### 14. Writing structured data
Structured data should use a defined format such as CSV or JSON rather than ad-hoc string formatting.

### 15. CSV fundamentals
The `csv` module reads and writes tabular data while handling quoting and delimiters correctly.

### 16. JSON fundamentals
The `json` module converts between JSON text and Python objects using `dump`/`load` for files and `dumps`/`loads` for strings.

### 17. File handling errors
Common failures include `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, and encoding-related errors.

### 18. Resource management
Open resources should have deterministic cleanup. Context managers are the standard pattern for this.

## 🧠 Core Concepts

- File paths and file contents are different concerns.
- `w` replaces; `a` appends; `x` requires a new path.
- Text mode works with `str`; binary mode works with `bytes`.
- Use `with` for files and other resources requiring cleanup.
- Stream large files instead of loading them completely when possible.

## ⚠️ Common Mistakes

- Forgetting to close a file.
- Using the wrong encoding.
- Using `w` when append behavior was intended.
- Reading huge files with `readlines()` unnecessarily.
- Treating JSON or CSV as arbitrary plain text.

## 🗂️ Files

- `exercise.py` — runnable file, CSV, and JSON examples.
- `fundamentals.py` — 10 file-I/O practice problems.

## 🎯 Expected Outcome

You should be able to safely read and write text and binary files, work with paths, process large files, and use CSV/JSON with correct resource management.