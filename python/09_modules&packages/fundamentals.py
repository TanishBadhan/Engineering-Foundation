"""10-question practice set for Modules & Packages."""

# Q1 — import
# Import math and calculate the square root and factorial of two values.

# Q2 — import styles
# Rewrite an example using both `import module` and `from module import name`.
# Explain the namespace difference.

# Q3 — Aliases
# Import datetime using an alias and use the alias to construct today's date.

# Q4 — Module namespace
# Import a standard-library module and use dir() or hasattr() to inspect names.
# Explain why module.name is useful.

# Q5 — Custom module
# Create helpers.py with add() and multiply(). Import it from another script
# and call both functions.

# Q6 — Package structure
# Design a package called sensors containing temperature.py and pressure.py.
# Write the import statements you would use from app.py.

# Q7 — Absolute vs relative imports
# Show one absolute import and one relative import for the same package.
# Explain where each form is normally written.

# Q8 — __name__ guard
# Write a function main() and call it only under:
# if __name__ == "__main__":
# Explain what changes when the file is imported.

# Q9 — Import mechanism
# Use sys.modules to check whether math is cached after importing it. Explain
# why Python caches loaded modules.

# Q10 — Design/debugging
# Suppose app.py imports helpers.py, but helpers.py imports app.py. Explain
# why this can create a circular import and propose a cleaner dependency
# structure.
