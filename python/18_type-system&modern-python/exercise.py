"""Runnable examples for Type System & Modern Python."""

from typing import Any, Callable, Optional, Union, Protocol

# 1. Type annotations
def add(a: int, b: int) -> int:
    return a + b

print("annotations:", add(2, 3), add.__annotations__)

# 2. Built-in generic types
scores: list[int] = [10, 20, 30]
lookup: dict[str, float] = {"temperature": 25.5}
print("generics:", scores, lookup)

# 3. Optional
name: Optional[str] = None
print("optional:", name)

# 4. Union / modern union syntax
value: Union[int, str] = "42"
modern_value: int | str = 42
print("union:", value, modern_value)

# 5. Any
anything: Any = {"can": "be any type"}
print("Any:", anything)

# 6. Type alias
SensorReading = float
reading: SensorReading = 25.4
print("alias:", reading)

# 7. Callable
Operation = Callable[[int, int], int]
def multiply(a: int, b: int) -> int:
    return a * b

def run_operation(operation: Operation, a: int, b: int) -> int:
    return operation(a, b)

print("Callable:", run_operation(multiply, 3, 4))

# 8. Generics fundamentals
from typing import TypeVar
T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

print("generic function:", first(["Python", "SQL"]))

# 9. Static type checking
# Tools such as mypy/pyright can inspect the annotations without executing the program.

# 10. typing module
print("typing helpers:", Optional, Union)

# 11. Structural typing with Protocol
class Startable(Protocol):
    def start(self) -> str: ...

class Motor:
    def start(self) -> str:
        return "started"

def start_device(device: Startable) -> str:
    return device.start()

print("structural typing:", start_device(Motor()))
