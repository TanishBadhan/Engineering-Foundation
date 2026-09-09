# Python Variables
What is a Variable?

A variable is a name that refers to a value.

name = "Tanish"
age = 19
salary = 25000

Here:

name, age, and salary are variable names.
"Tanish", 19, and 25000 are their values.
Variable Assignment

Python uses = to assign a value to a variable.

x = 10

= is called the assignment operator.

# Dynamic Typing

Python is dynamically typed, which means you do not need to declare the data type of a variable explicitly.

x = 10
x = "Python"

A variable can refer to values of different data types at different times.

# Multiple Assignment

Multiple variables can be assigned in a single statement.

x, y, z = 10, 20, 30

The same value can also be assigned to multiple variables.

a = b = c = 100
Variable Naming Rules
Valid Variable Names
name = "Tanish"
student_age = 19
marks2 = 85
Invalid Variable Names
2marks = 85
student-age = 19
Rules
Variable names can contain letters, numbers, and underscores.
Variable names cannot start with a number.
Spaces are not allowed.
Python keywords cannot be used as variable names.
Variable names are case-sensitive.

For example:

age = 19
Age = 20

age and Age are different variables.

# Checking Variable Type

The type() function can be used to check the data type of a value.

x = 10

print(type(x))

Output:

<class 'int'>

# Reassigning Variables

A variable can be assigned a new value.

score = 50
score = 75

After the second assignment, score refers to 75.

# Key Takeaways
1. A variable is a name that refers to a value.
2. = is used for assignment.
3. Python uses dynamic typing.
4. Variables can be reassigned.
5. Multiple variables can be assigned in one statement.
6. Variable names must follow Python's naming rules.
7. Python variable names are case-sensitive.
8. type() can be used to check the type of a value.