"""
02_data_types / practice.py

Practice exercises for Data Types & Data Structures.
Each exercise has a short prompt and a `# TODO`. Write your
solution in place of the TODO, then run the file to check
your own output against the expected behavior described.

No solutions are given — the goal is deliberate practice.
"""

# ---------------------------------------------------------------
# 1-2. Integers & Floats
# ---------------------------------------------------------------
# TODO: Given price = 49.99 and quantity = 3, compute the total
# cost and round it to 2 decimal places.
price = 49.99
quantity = 3
# total = ...

# sol:
total = round(price * quantity, 2)
print(total)  # Expected output: 149.97


# ---------------------------------------------------------------
# 4. Booleans
# ---------------------------------------------------------------
# TODO: Without using `if x == True`, write a boolean expression
# that checks whether age (below) is old enough to vote (18+).
age = 20
# can_vote = ...

# sol:
can_vote = age >= 18
print(can_vote)  # Expected output: True

# ---------------------------------------------------------------
# 6. None
# ---------------------------------------------------------------
# TODO: `user_email` below represents "no email provided."
# Write a check using `is` (not `==`) that prints "No email on file"
# if it's missing, otherwise prints the email.

# sol:
user_email = None

if user_email is None:
    print("No email on file")
else:
    print(user_email)

# ---------------------------------------------------------------
# 7. Type conversion
# ---------------------------------------------------------------
# TODO: `raw_input` is a string from a form field. Convert it to
# a float safely — handle the case where conversion might fail.
raw_input = "12.5"

# sol:

try :
    converted_input = float(raw_input)
    print(converted_input)  # Expected output: 12.5
except ValueError:
    print("Invalid input, cannot convert to float.")
    converted_input = 0 # for the fallback 
    
# ---------------------------------------------------------------
# 8-9. Lists vs Tuples
# ---------------------------------------------------------------
# TODO: Store a to-do list (should change often) in the right
# container, and a (latitude, longitude) coordinate pair (should
# never change) in the right container. Explain your choice in
# a comment.
# todo_list = ...
# coordinate = ...

# sol:
todo_list = ["Buy groceries", "Call mom", "Finish project"]  # List is mutable, suitable for a to-do list that changes often.
coordinate = (12.34, 56.78)  # Tuple is immutable, suitable for a coordinate pair that should not change.

# ---------------------------------------------------------------
# 10. Sets
# ---------------------------------------------------------------
# TODO: Given the list below, produce a collection of the unique
# tags with no duplicates.
tags = ["python", "coding", "python", "beginner", "coding"]
# unique_tags = ...

# sol:
unique_tags = set(tags)
print(unique_tags)  # Expected output: {'python', 'coding', 'beginner'} # sets ignore the repeating elements.

# ---------------------------------------------------------------
# 11. Dictionaries
# ---------------------------------------------------------------
# TODO: Build a dictionary representing a book with keys: title,
# author, year. Then update the year to a new value.
# book = ...

# sol:
book = {"title": "Python Programming", "author": "John Doe", "year": 2020}
book["year"] = 2021
print(book)  # Expected output: {'title': 'Python Programming', 'author': 'John Doe', 'year': 2021}

# ---------------------------------------------------------------
# 12. Nested data structures
# ---------------------------------------------------------------
# TODO: Given the nested structure below, print the city of the
# second person WITHOUT hardcoding the value directly (index/key
# your way to it).
people = [
    {"name": "Ana", "address": {"city": "Delhi"}},
    {"name": "Ben", "address": {"city": "Mumbai"}},
]

print(people[1]["address"]["city"])  # Accessing the city of the second person

# ---------------------------------------------------------------
# 13. Mutability
# ---------------------------------------------------------------
# TODO: Predict, then verify: after running the two lines below,
# does `original` also contain 4? Why or why not? Write your
# answer as a comment.
original = [1, 2, 3]
copy_ref = original
copy_ref.append(4)

#sol:
# yes the original list will also contain 4 because `copy_ref` is a reference to the same list object as `original`. Therefore, modifying `copy_ref` modifies the same underlying list.


# ---------------------------------------------------------------
# 14. Hashability
# ---------------------------------------------------------------
# TODO: You want to use a pair of coordinates as a dictionary key
# to store "visited" status. Which type (list or tuple) must you
# use, and why? Write your answer as a comment, then build a
# small dict demonstrating it.

#sol:
# i will choose tuple because tuples are immutable and hashable perfect for the dictonary keys. 
# Whereas Lists are mubtable and this makes them unhashable and unsuitable for use as dictionary keys.

# hash([1,2]) # This will raise a TypeError because lists are unhashable.
hash((1,2)) # This will work because tuples are hashable.

# ---------------------------------------------------------------
# 15-16. Indexing & Slicing
# ---------------------------------------------------------------
# TODO: Given the string below, extract just the word "Python"
# using slicing (not a library function).
sentence = "I am learning Python properly"

# sol:
my_word = (sentence[14:20])  # Extract "Python" using slicing
print(my_word)

# ---------------------------------------------------------------
# 17. Membership
# ---------------------------------------------------------------
# TODO: Check whether "banana" is in the fruits list below, and
# print a friendly message either way.
fruits = ["apple", "orange", "grape"]

# sol:

if "banana" in fruits:
    print("Banana is in the list of fruits.")
else:
    print("Banana is not in the list of fruits.")

# ---------------------------------------------------------------
# 18. Built-in operations
# ---------------------------------------------------------------
# TODO: Given the scores list, print the number of scores, the
# total, the average (2 decimal places), and the sorted list in
# descending order — using built-in functions only.
scores = [88, 92, 79, 95, 67]

# sol:
no_of_scores = len(scores)
total_scores = sum(scores)
average_score = round(total_scores / no_of_scores, 2)
sorted_scores_desc = sorted(scores, reverse=True)

print(f"{no_of_scores} scores, total: {total_scores}, average: {average_score}, sorted descending: {sorted_scores_desc}")