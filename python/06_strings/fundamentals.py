"""06_strings / practice.py — fill in each TODO, no answers given."""

# 1. Creation: create a multi-line string containing three lines of
# your choice using triple quotes.

# MY SOL :
a = """ My name is tanish badhan 
        I am a proficient AI engineer 
        I will be succeeding ahead in whatever i will be doing in life."""

print(a)
# 2. Indexing/slicing: get the last 3 characters of `word` below.
word = "engineering"
# my sol :
print(word[-3:])

# 3. Immutability: `name` should become uppercase. Fix the bug below.
name = "tanish"
name.upper()
print(name)   # currently prints "tanish" — why? fix it.

# fix :
print(name.upper())

# 4. String methods: check if `email` both starts with "admin" and
# ends with "@company.com".
email = "admin@company.com"
# my sol:
print((email.startswith("admin")) and email.endswith("@company.com"))

# 5. Search/replace: replace all dashes with spaces in `code`.
code = "AB-12-CD-34"
# my sol:
print(code.replace("-"," "))


# 6. Split/join: turn the sentence below into a list of words, then
# join them back together with underscores instead of spaces.
sentence = "learning python step by step"

# my sol :
words = sentence.split()
result = "_".join(words)
print(result)

# 7. Whitespace: clean up `raw` so it has no leading/trailing spaces
# and no internal extra newline.
raw = "   important data   \n"

# my sol:
clean = raw.strip()
print(clean)

# 8-9. Formatting: build a message "Order #1042: $59.99" using an
# f-string, given the variables below (format price to 2 decimals).
order_id = 1042
amount = 59.989
print(f"Order:{order_id}: ${amount:.2f}")

# 10. Escape sequences: print a string that displays as:
#   Name:	Tanish
#   Quote:	"Keep going"
# (use \t and \" appropriately)
print("Name :\tTanish Badhan\nQuote:\t\"Its Not Over Until I win\"")

# 11. Raw strings: store the Windows path C:\Users\Tanish\Desktop
# correctly using a raw string.
path = r"C:\Users\Tanish\Desktop"
print(path)

# 12. Comparison: predict then verify — is "Banana" < "apple" True
# or False? Print it and explain why as a comment.
result = "Banana" < "apple"
print(result) # beacause the string are also just unicodes formed together representing words and python compares left to write so B is a lesser number as a UNICODE than A .


# 13. Iteration: count how many vowels are in `phrase` below using a
# for loop over its characters.
phrase = "the quick brown fox"

count = 0
for w in phrase:
    if w in "aeiou":
        count += 1
        
print(count)

# 14. Practical pattern: given the messy CSV line below, extract a
# clean list of [name, age, city] with whitespace stripped from each.
csv_line = " Ana , 28 , Delhi "

data = [i.strip() for i in csv_line.split(",")]
print(data)