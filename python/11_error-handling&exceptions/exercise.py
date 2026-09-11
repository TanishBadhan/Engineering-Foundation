"""Runnable examples for Error Handling & Exceptions."""

# 1–4. Exception categories
# Syntax errors stop parsing before execution and therefore are not demonstrated here.
# Runtime exception:
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("runtime exception:", error)

# Logical error: the code runs but the intended formula is wrong.
print("logical-error example:", 2 + 2)  # change the intended requirement to see the distinction

# 5. Exception hierarchy
print("ZeroDivisionError subclass of Exception:", issubclass(ZeroDivisionError, Exception))

# 6–9. try / except / else / finally
try:
    value = int("42")
except ValueError:
    print("invalid integer")
else:
    print("converted:", value)
finally:
    print("cleanup/finally executed")

# 10–11. Raising exceptions with raise
def set_percentage(value):
    if not 0 <= value <= 100:
        raise ValueError("percentage must be between 0 and 100")
    return value

print("valid percentage:", set_percentage(80))

# 12. Custom exception
class InsufficientStockError(Exception):
    pass

# 13. Exception propagation

def inner():
    raise InsufficientStockError("stock unavailable")

def outer():
    inner()

try:
    outer()
except InsufficientStockError as error:
    print("propagated exception:", error)

# 14. Specific exception handling
try:
    number = int("abc")
except ValueError as error:
    print("specific handler:", error)

# 15. Reliable handling: catch expected failures and preserve context.
def parse_port(value):
    try:
        port = int(value)
    except ValueError as error:
        raise ValueError("port must be an integer") from error
    if not 1 <= port <= 65535:
        raise ValueError("port out of range")
    return port

print("port:", parse_port("8080"))
