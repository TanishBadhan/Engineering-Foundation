"""10-question practice set for Object-Oriented Programming."""

# Q1 — Classes and objects
# Create a Robot class with name and speed instance attributes and a move()
# method. Instantiate two different robots.

# Q2 — Class vs instance attributes
# Add a class attribute category = "AGV". Show that instances can read it,
# then explain what happens if an instance assigns its own category.

# Q3 — Methods and self
# Write an instance method that changes an object's state. Explain what self
# refers to during the call.

# Q4 — Classmethod and staticmethod
# Add a classmethod alternative constructor and a staticmethod that validates
# an input. Explain why each does or does not need self/cls.

# Q5 — Inheritance and overriding
# Create Vehicle and two subclasses that override move(). Put both objects
# into a list and call move() polymorphically.

# Q6 — Composition vs inheritance
# Model a Car that uses an Engine. Implement it with composition and explain
# why Engine does not need to be a parent of Car.

# Q7 — MRO and super()
# Create a small multiple-inheritance example. Print its MRO and use super()
# to demonstrate cooperative method lookup.

# Q8 — Dunder methods
# Create a Point class implementing __repr__ or __str__, __eq__, and __add__.
# Demonstrate printing, comparison, and addition.

# Q9 — Dataclass + property
# Create a dataclass for a Sensor. Then create another class with a property
# that rejects invalid values.

# Q10 — ABC / Protocol / duck typing
# Define an abstract Shape with area(), then implement Circle or Square.
# Separately write a function that accepts any object with start() and explain
# how duck typing differs from nominal inheritance.
