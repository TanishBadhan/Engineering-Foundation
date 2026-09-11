# 10. Object-Oriented Programming

Object-oriented programming organizes state and behavior around objects. Python's object model is flexible: classes can use inheritance, composition, protocols, properties, special methods, and dataclasses. The goal is to model responsibilities clearly, not to force every problem into a class.

## 📖 Subtopics

### 1. Classes
A class defines a type and describes the attributes and behavior its instances can have.

### 2. Objects
An object is an instance of a class. Every Python object has identity, type, and value/state.

### 3. Attributes
Attributes are names associated with an object or class, accessed with dot notation.

### 4. Methods
A method is a function defined in a class and normally accessed through an instance or class.

### 5. Constructors
In everyday Python terminology, object initialization is often called construction. `__new__` creates an instance and `__init__` initializes an already-created instance.

### 6. `__init__`
`__init__` receives the newly created instance as `self` and initializes its state. It does not itself create the object.

### 7. Instance attributes
These belong to a particular object, commonly assigned through `self.attribute`.

### 8. Class attributes
These belong to the class and are shared unless an instance shadows the same name.

### 9. Instance methods
Their first conventional parameter is `self`, giving access to instance state.

### 10. Class methods
`@classmethod` receives the class as `cls` and is useful for alternative constructors or class-level behavior.

### 11. Static methods
`@staticmethod` does not receive an automatic instance or class argument. It is a function grouped inside the class namespace.

### 12. `self`
`self` is the conventional name for the current instance. It is passed automatically when an instance method is called through an instance.

### 13. Encapsulation
Encapsulation keeps related state and behavior together and controls how state is accessed. Python uses conventions such as `_name` and name mangling for `__name`, rather than strict private fields.

### 14. Abstraction
Abstraction exposes the important interface while hiding unnecessary implementation details.

### 15. Inheritance
A class can derive from another class and reuse or specialize its behavior.

### 16. Method overriding
A subclass can provide its own implementation of an inherited method.

### 17. Polymorphism
Different objects can support the same operation or interface while implementing it differently.

### 18. Composition
A class contains or uses other objects to build larger behavior. Composition often reduces tight coupling compared with deep inheritance.

### 19. Aggregation
Aggregation is a weaker whole-part relationship where contained objects can exist independently of the container.

### 20. Association
Association simply means objects know about or interact with one another without implying ownership.

### 21. Multiple inheritance
A class can inherit from multiple base classes. It is powerful but should be designed carefully because method lookup becomes more complex.

### 22. Method Resolution Order (MRO)
MRO defines the order Python searches classes for attributes and methods. `Class.mro()` or `Class.__mro__` exposes it.

### 23. `super()`
`super()` delegates to the next class in the MRO and is central to cooperative inheritance.

### 24. Special / dunder methods
Methods such as `__str__`, `__repr__`, `__len__`, and `__eq__` integrate custom objects with Python syntax and built-ins.

### 25. Operator overloading
Special methods such as `__add__` and `__lt__` can define how operators work with custom objects.

### 26. Properties
`@property` exposes method-backed behavior through attribute syntax and can control access to computed or validated state.

### 27. Getters and setters
In Python, properties are generally preferred to Java-style explicit getter/setter methods when controlled attribute access is needed.

### 28. Dataclasses
`@dataclass` generates common methods such as `__init__` and `__repr__` for data-focused classes, reducing boilerplate.

### 29. Abstract base classes
`abc.ABC` and `@abstractmethod` define required methods for subclasses and can prevent incomplete classes from being instantiated.

### 30. Interfaces through protocols / duck typing
Duck typing focuses on supported behavior rather than exact type. `typing.Protocol` lets that structural interface be described for static type checking.

## 🧠 Core Concepts

- Prefer composition when an object simply uses another object.
- Inheritance should represent a meaningful “is-a” relationship.
- Encapsulation in Python is based heavily on conventions and interfaces.
- Polymorphism often works without a common base class because of duck typing.
- `super()` follows MRO; it does not simply mean “call my parent.”

## ⚠️ Common Mistakes

- Forgetting `self` in instance methods.
- Treating `__init__` as the object allocator.
- Accidentally sharing mutable state through class attributes.
- Using inheritance where composition is clearer.
- Calling `super()` without understanding cooperative multiple inheritance.
- Writing getters/setters that add no useful behavior.

## 🗂️ Files

- `exercise.py` — runnable examples of core OOP patterns.
- `fundamentals.py` — 10 problems covering object design and Python's object model.

## 🎯 Expected Outcome

You should be able to design small class hierarchies, choose composition or inheritance appropriately, use Python's special methods and properties, and understand MRO, ABCs, dataclasses, and protocols.