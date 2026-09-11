"""Runnable examples for Modules & Packages.

Some package examples are shown as source snippets because a single file
cannot create a complete package tree at runtime.
"""

# 1–2. import and module access
import math
print("sqrt:", math.sqrt(25))

# 3. from ... import
from math import factorial
print("factorial:", factorial(5))

# 4. Aliases
import datetime as dt
print("year:", dt.date.today().year)

# 5. Module namespaces
print("math namespace contains sqrt:", hasattr(math, "sqrt"))

# 6. Creating custom modules
# Example file: helpers.py
# def add(a, b):
#     return a + b
# Another file can then use: import helpers; helpers.add(2, 3)

# 7–8. Packages and __init__.py
# Example structure:
# project/
#   app.py
#   tools/
#     __init__.py
#     numbers.py
# A regular package commonly uses __init__.py for initialization or exports.

# 9. Absolute imports
# from project.tools.numbers import add

# 10. Relative imports
# Inside project/tools/report.py:
# from .numbers import add

# 11. __name__
print("current module name:", __name__)

# 12. Main guard
if __name__ == "__main__":
    print("This file is being executed directly.")

# 13. Import mechanism / cache
import sys
print("math cached:", "math" in sys.modules)

# 14. Standard library fundamentals
from pathlib import Path
path = Path("example.txt")
print("filename:", path.name)
