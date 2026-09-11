"""Runnable examples for Object-Oriented Programming."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

# 1–4. Class, object, attributes, methods
class Robot:
    category = "industrial"  # 8. class attribute

    def __init__(self, name, speed):  # 5–6. initialization
        self.name = name  # 7. instance attribute
        self.speed = speed

    def move(self):  # 9. instance method
        return f"{self.name} moves at {self.speed} m/s"

    @classmethod  # 10. class method
    def from_slow_robot(cls, name):
        return cls(name, 1)

    @staticmethod  # 11. static method
    def valid_speed(speed):
        return speed >= 0

robot = Robot("AGV-1", 2)
print("object:", robot.move())
print("class attribute:", robot.category)
print("self speed valid:", Robot.valid_speed(robot.speed))

# 12. self is the instance passed to instance methods.

# 13. Encapsulation
class Account:
    def __init__(self, balance):
        self._balance = balance  # convention: internal/protected-like

    # 26–27. property as controlled access
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        self._balance = value

account = Account(100)
account.balance = 150
print("property balance:", account.balance)

# 14–17. Abstraction, inheritance, overriding, polymorphism
class Vehicle:
    def move(self):
        return "vehicle moves"

class Car(Vehicle):
    def move(self):
        return "car drives"

class Drone(Vehicle):
    def move(self):
        return "drone flies"

for vehicle in [Car(), Drone()]:
    print("polymorphism:", vehicle.move())

# 18–20. Composition, aggregation, association
class Engine:
    def start(self):
        return "engine started"

class Machine:
    def __init__(self, engine):
        self.engine = engine  # composition/has-a usage

    def start(self):
        return self.engine.start()

engine = Engine()
machine = Machine(engine)
print("composition:", machine.start())
# Aggregation: the engine could exist independently of Machine.
# Association: two independent objects can simply collaborate.

# 21–23. Multiple inheritance, MRO, super()
class LoggerMixin:
    def action(self):
        return "logged"

class BaseController:
    def action(self):
        return "controller"

class Controller(LoggerMixin, BaseController):
    def action(self):
        return super().action() + " + controller"

print("MRO:", [cls.__name__ for cls in Controller.mro()])
print("super:", Controller().action())

# 24–25. Dunder methods / operator overloading
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v = Vector(1, 2) + Vector(3, 4)
print("operator overload:", v)

# 28. Dataclass
@dataclass
class Sensor:
    name: str
    value: float

print("dataclass:", Sensor("temperature", 25.5))

# 29. Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print("ABC:", Square(4).area())

# 30. Protocol / duck typing
class Startable(Protocol):
    def start(self) -> str: ...

class Motor:
    def start(self):
        return "motor started"

# Motor does not inherit Startable, but supports the required behavior.
def run_device(device: Startable):
    return device.start()

print("protocol-style duck typing:", run_device(Motor()))
