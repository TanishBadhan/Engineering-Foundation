# 9. Modules & Packages

Modules let Python code be split into reusable files. Packages organize related modules into directories. Understanding namespaces and imports is essential for building maintainable applications and avoiding circular-import or path mistakes.

## 📖 Subtopics

### 1. Importing modules
Importing makes names defined in another module available through that module's namespace.

### 2. `import`
`import math` binds the module name; use `math.sqrt(25)` to access its members.

### 3. `from ... import`
`from math import sqrt` binds `sqrt` directly. It is convenient but can make the origin of a name less obvious.

### 4. Aliases
`import numpy as np` or `from pathlib import Path` can shorten commonly used names and avoid collisions.

### 5. Module namespaces
A module has its own namespace. `module.name` explicitly accesses a name stored there.

### 6. Creating custom modules
Any `.py` file can be imported as a module when Python can find it on its import path.

### 7. Packages
A package is a directory used to organize modules and subpackages. Modern Python can support namespace packages without `__init__.py`, but regular packages commonly include it.

### 8. `__init__.py`
It marks and initializes a regular package and can expose selected package-level names. It runs when the package is initialized.

### 9. Absolute imports
An absolute import starts from the top-level package/module available on the import path, such as `from project.utils import helper`.

### 10. Relative imports
Relative imports use dots to refer to the current package, such as `from .utils import helper`. They are mainly used inside packages.

### 11. `__name__`
Every module has `__name__`. An imported module normally has its module name; a directly executed script has `__name__ == "__main__"`.

### 12. `if __name__ == "__main__"`
This guard keeps script-only behavior from running automatically when the file is imported.

### 13. Python's import mechanism
Python searches import locations, finds the requested module/package, creates and initializes a module object, and caches it in `sys.modules`.

### 14. Standard library fundamentals
Python ships with modules such as `math`, `pathlib`, `json`, `os`, `datetime`, and `collections`. Learn their purpose and documentation rather than memorizing every function.

## 🧠 Core Concepts

- Importing is primarily namespace management and module loading.
- `import x` and `from x import y` create different local bindings.
- Relative imports depend on package context.
- Imports are normally cached in `sys.modules`, so repeated imports do not simply re-execute the module each time.

## ⚠️ Common Mistakes

- Naming a file `math.py`, `json.py`, or another standard-library name.
- Confusing a module's namespace with the caller's namespace.
- Using relative imports from a script executed in a way that removes package context.
- Putting expensive side effects at module import time.
- Creating circular imports through poorly designed dependencies.

## 🗂️ Files

- `exercise.py` — runnable import and package examples.
- `fundamentals.py` — 10 problems covering modules, namespaces, packages, and imports.

## 🎯 Expected Outcome

You should be able to create reusable modules, organize packages, choose appropriate import styles, and understand why Python loads and caches modules.