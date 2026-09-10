"""06_strings / examples.py — runnable demos, one section per subtopic."""

# 1. String creation
single = 'hello'
double = "hello"
multi = """line one
line two"""
print("1.", single == double, multi)

# 2. Indexing and slicing
word = "Python"
print("2.", word[0], word[-1], word[0:3], word[::-1])

# 3. Immutability
s = "hello"
s.upper()               # does nothing to s itself
print("3. unchanged:", s)
s = s.upper()            # must reassign to capture the new string
print("3. reassigned:", s)

# 4. String methods
text = "  Hello World  "
print("4.", text.strip(), "|", text.lower(), "|", text.startswith("  He"))

# 5. Searching and replacing
sentence = "the cat sat on the mat"
print("5. find:", sentence.find("cat"), "| find missing:", sentence.find("dog"))
print("5. replace:", sentence.replace("cat", "dog"))
print("5. in:", "sat" in sentence)

# 6. Splitting and joining
csv_line = "apple,banana,cherry"
parts = csv_line.split(",")
print("6. split:", parts)
print("6. joined:", "-".join(parts))

# 7. Whitespace handling
messy = "   padded text\n"
print("7.", repr(messy.strip()))

# 8. Formatting (older styles, shown for recognition)
name, age = "Ana", 30
print("8. percent-style:", "%s is %d" % (name, age))
print("8. format():", "{} is {}".format(name, age))

# 9. f-strings (modern default)
price = 19.5
print(f"9. {name} is {age} years old, price: {price:.2f}")

# 10. Escape sequences
print("10.", "line1\nline2\ttabbed\tend")
print("10.", "She said \"hello\"")

# 11. Raw strings
path = r"C:\new\folder"
print("11.", path)

# 12. String comparison
print("12.", "apple" == "apple", "Zebra" < "apple")   # uppercase sorts before lowercase

# 13. Iterating over strings
for ch in "abc":
    print("13. char:", ch)

# 14. Practical string-processing patterns
raw_line = " Tanish, 25, Engineer "
name2, age2, role = [p.strip() for p in raw_line.split(",")]
print("14.", name2, age2, role)

title = " ".join(word.capitalize() for word in "hello world from python".split())
print("14. title-cased:", title)