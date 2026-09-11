"""Python Functions — runnable examples for every subtopic."""

# 1. Defining functions

def greet():
    """A function with no parameters."""
    print("Hello")


# 2. Calling functions
greet()


# 3–6. Parameters, positional, keyword, default arguments

def introduce(name, age=20):
    print(f"{name} is {age} years old")


introduce("Tanish", 20)                 # positional
introduce(age=20, name="Tanish")       # keyword
introduce("Tanish")                     # default


# 7–9. Variable-length arguments, *args, **kwargs

def show_args(*args):
    print("args:", args)


def show_kwargs(**kwargs):
    print("kwargs:", kwargs)


def show_everything(required, *args, **kwargs):
    print(required, args, kwargs)


show_args(1, 2, 3)
show_kwargs(name="Tanish", role="Engineer")
show_everything("A", 10, 20, language="Python")


# 10. Return values

def square(number):
    return number * number


result = square(5)
print("square:", result)


# 11. Multiple return values

def divide(a, b):
    return a // b, a % b


quotient, remainder = divide(17, 5)
print(quotient, remainder)


# 12–15. Scope, local/global, global, nonlocal
count = 0


def local_example():
    message = "local"
    print(message)


def increment_global():
    global count
    count += 1


local_example()
increment_global()
print("global count:", count)


def outer():
    value = 10

    def inner():
        nonlocal value
        value += 1
        return value

    return inner


counter = outer()
print("nonlocal value:", counter())
print("nonlocal value:", counter())


# 16. Function composition

def double(x):
    return x * 2


def add_one(x):
    return x + 1


def compose(f, g, value):
    return f(g(value))


print("composition:", compose(double, add_one, 4))


# 17–18. First-class functions / functions as objects

def say_hi():
    return "Hi"


alias = say_hi
print("function object:", alias())
print("callable:", callable(alias))


# 19. Higher-order functions

def apply(function, value):
    return function(value)


print("higher-order:", apply(square, 6))


# 20. Lambda functions
add = lambda a, b: a + b
print("lambda:", add(2, 3))


# 21. Recursion

def factorial(n):
    if n <= 1:                 # base case
        return 1
    return n * factorial(n - 1) # recursive case


print("factorial:", factorial(5))


# 22. Documentation and docstrings

def area_of_rectangle(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width


print(area_of_rectangle(4, 3))
print(area_of_rectangle.__doc__)


# 23. Type hints

def repeat_text(text: str, times: int) -> str:
    return text * times


print(repeat_text("Py", 3))


# 24. Pure vs impure functions

def pure_add(a: int, b: int) -> int:
    """Same inputs always produce the same result and no external state changes."""
    return a + b


log = []


def impure_add(a: int, b: int) -> int:
    """Produces a result while also changing external mutable state."""
    result = a + b
    log.append(result)
    return result


print("pure:", pure_add(2, 3))
print("impure:", impure_add(2, 3), "log:", log)
