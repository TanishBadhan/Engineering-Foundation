# Python Variables - Practice

# 1. Create variables for your name, age, and city.
# Print all three variables.
name = "Tanish Badhan"
age = 19
city = "Chandigarh"

print(name)
print(age)
print(city)

# 2. Create two variables containing numbers.
# Print their sum.
a = 10
b = 20
print(a + b)

# 3. Create a variable called "score".
# Assign it 50, print it, then reassign it to 80 and print it again.
score = 50 
print(score)
score = 80
print(score)

# 4. Create three variables x, y, and z using multiple assignment.
# Assign them the values 10, 20, and 30.
x , y, z = 10, 20, 30
print(x)
print(y)
print(z)

# 5. Create three variables a, b, and c.
# Assign the same value to all three variables using one statement.
a = b = c = 100
print(a)
print(b)
print(c)

# 6. Create a variable containing a number.
# Use type() to check its data type.
num = 76
print(type(num))

# 7. Create a variable containing a string.
# Use type() to check its data type.
me = "Tanish"
print(type(me))

# 8. Create two variables with the same name but different capitalization.
# Example: age and Age.
# Give them different values and print both.
age = 19
Age = 20
print(age)
print(Age)

# 9. Create variables for:
# name, age, percentage, and is_student.
# Give each an appropriate value and print their types.
name = "Tanish Badhan"
age = 19
percentage = 69.8
is_student = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))

# 10. Identify which of the following are valid Python variable names:
# student_name
# 2students
# student2
# student-age
# _marks
# class

student_name = "tanish"
print(student_name)

#2students = "tanish and neha" # Invalid variable name, cannot start with a number
# print(2students)

student2 = "tanish"
print(student2)

#student-age = "tanish" # Invalid variable name, cannot contain hyphens
# print(student-age)

_marks = 85
print(_marks)

#class = "10th Grade" # Invalid variable name, 'class' is a reserved keyword
#print(class)