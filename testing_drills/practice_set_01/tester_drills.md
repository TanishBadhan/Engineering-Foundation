# Practice Set 1 — Questions, Attempts, Feedback, and Reference Fixes

This record distinguishes the learner's original attempts from reference solutions. Syntax errors, incorrect tests, and revisions are kept because they show which skills need more practice.

## Question 1 — Even number

**Requirement:** Return `True` for an even integer and `False` otherwise.

**Buggy code**

```python
def is_even(number):
    if number % 2 == 1:
        return True
    else:
        return False
```

**Original attempt and outcome**

The learner identified that the condition should be `number % 2 == 0`, rewrote it correctly, tested `2` and `3`, and explained how the original condition failed. Score: 9/10.

**Reference fix**

```python
def is_even(number):
    return number % 2 == 0
```

**Tests**

```python
def test_even_number():
    assert is_even(2) is True

def test_odd_number():
    assert is_even(3) is False
```

**Status:** Passed.

---

## Question 2 — Discount age boundary

**Requirement:** Ages 5 through 17 are eligible, including both endpoints.

**Buggy code**

```python
def qualifies_for_discount(age):
    if age > 5 and age < 17:
        return True
    else:
        return False
```

**Original attempt and outcome**

The learner changed the condition to `age >= 5 and age <= 17`, tested ages 5, 17, and 12, and suggested -5 and 18 as additional tests. They correctly noted that a typical interior value alone would not expose the boundary bug. Score: 9/10.

**Reference fix**

```python
def qualifies_for_discount(age):
    return 5 <= age <= 17
```

**Tests**

```python
def test_lower_boundary():
    assert qualifies_for_discount(5) is True

def test_upper_boundary():
    assert qualifies_for_discount(17) is True

def test_inside_range():
    assert qualifies_for_discount(12) is True

def test_below_range():
    assert qualifies_for_discount(4) is False

def test_above_range():
    assert qualifies_for_discount(18) is False
```

**Status:** Passed.

---

## Question 3 — Whitespace-only username

**Requirement:** A username consisting only of whitespace must not be valid.

**Buggy code**

```python
def is_valid_username(username):
    if len(username) > 0:
        return True
    else:
        return False
```

**Original attempt and outcome**

The learner explained that spaces count as characters, then proposed stripping surrounding whitespace and checking the cleaned string. Their tests covered a normal username, an empty string, and spaces only. Score: 8.5/10.

**Reference fix**

```python
def is_valid_username(username):
    return len(username.strip()) > 0
```

**Tests**

```python
def test_normal_username():
    assert is_valid_username("Alice") is True

def test_empty_username():
    assert is_valid_username("") is False

def test_whitespace_only_username():
    assert is_valid_username("       ") is False
```

**Feedback:** `strip()` returns a new string with leading and trailing whitespace removed; it does not mutate the original string.

**Status:** Passed.

---

## Question 4 — Print versus return

**Requirement:** Return the square of a number.

**Buggy code**

```python
def square(number):
    result = number * number
    print(result)
```

**Original attempt and outcome**

The learner correctly explained that the function prints but does not return its result, so the call evaluates to `None`. They replaced `print(result)` with `return result` and tested 4 and -3. Score: 9/10.

**Reference fix**

```python
def square(number):
    return number * number
```

**Tests**

```python
def test_positive_number():
    assert square(4) == 16

def test_negative_number():
    assert square(-3) == 9
```

**Status:** Passed.

---

## Question 5 — Input validation and exceptions

**Requirement:** Accept a non-negative integer age and return age plus one. Negative and non-integer values must raise `ValueError`.

**Buggy code**

```python
def age_next_year(age):
    if age < 0:
        return False
    return age + 1
```

**Original attempts**

The learner identified that returning `False` did not satisfy the requirement to raise an exception, and noticed that non-integer inputs were not validated. They tried the invalid parameter syntax `def age_next_year(int age)`, then tried testing exceptions by asserting a call equalled `ValueError`. Later attempts included `int(age) == False` and combining it with `age < 0` using `and`.

**What needed correction**

- Python annotation syntax is `age: int`, not `int age`.
- Type annotations do not enforce runtime types by themselves.
- Comparing a normal function result to `ValueError` does not test whether an exception is raised.
- `int(age)` attempts a conversion; it is not a safe validity check.
- When either the type is invalid or the age is negative, the input should be rejected. Requiring both conditions with `and` misses cases.
- In Python, `bool` is a subclass of `int`. A strict integer-only rule that excludes booleans can use `type(age) is not int`.

**Reference implementation**

```python
def age_next_year(age):
    if type(age) is not int or age < 0:
        raise ValueError("age must be a non-negative integer")
    return age + 1
```

**Example pytest tests**

```python
import pytest

def test_valid_age():
    assert age_next_year(12) == 13

def test_negative_age_raises():
    with pytest.raises(ValueError):
        age_next_year(-2)

def test_non_integer_raises():
    with pytest.raises(ValueError):
        age_next_year("12")

def test_boolean_is_rejected():
    with pytest.raises(ValueError):
        age_next_year(True)
```

**Status:** Partial — 6/10. Revisit exception testing and Boolean operators with a new problem.

---

## Question 6 — First item of a list

**Requirement:** Return the first item; return `None` for an empty list.

**Buggy code**

```python
def first_item(items):
    return items[0]
```

**Original attempts**

The learner correctly observed that an empty list has no index 0. Their first attempted fix ended with `return items[]`, which is invalid syntax. The intended correction was clarified as returning `None` for an empty list.

Their first tests were:

```python
def test_non_empt():
    assert first_item(3,2,4) == first_item(items[0])

def test_empty():
    assert first_item() == first_item(index[])
```

A later attempt was:

```python
def test_non_empty():
    assert first_item(1,2,3) == [1]

def test_empty():
    assert first_item() == None
```

On retry, the learner supplied a list but expected `[1]` instead of the integer `1`, and still omitted the empty-list argument.

**Reference fix**

```python
def first_item(items):
    if items:
        return items[0]
    return None
```

**Correct tests**

```python
def test_non_empty():
    assert first_item([1, 2, 3]) == 1

def test_empty():
    assert first_item([]) is None
```

**Learning points**

- The function accepts one argument: a list.
- `[1, 2, 3]` is a list; `1` is an integer; `[1]` is a list containing one integer.
- Pass `[]` explicitly to test an empty list.
- `is None` is the idiomatic check for `None`.
- The output list's indexes are not preserved when elements are removed; reason about values and output structure.

**Status:** Passed after retries — 7/10. Test-call structure and expected return types need more practice.

---

## Question 7 — Remove duplicates

**Requirement:** Remove duplicate values while preserving the order of first occurrence.

**Buggy code**

```python
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(items)
    return result
```

**Original explanation and fix**

The learner correctly identified the bug: the function appended the entire `items` list instead of the current `item`.

**Learner's corrected function**

```python
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
```

**Learner's tests**

```python
def test_duplicates():
    assert remove_duplicates([3,3,3,2,2,1,1]) == [3,2,1]

def test_no_duplicates():
    assert remove_duplicates([1,2,3]) == [1,2,3]
```

Both tests are correct.

**Stronger additional test**

```python
def test_mixed_duplicates_preserve_order():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
```

**Feedback:** The learner initially said that the original indexes are preserved. More precisely, the loop visits values in input order and the output retains the relative order of first occurrences. The output is a new list and does not preserve all original indexes.

**Status:** Passed — 8.5/10.

---

## Question 8 — Counting vowels

**Requirement:** Count vowels regardless of case. For example, `count_vowels("Apple")` should return 2.

**Buggy code**

```python
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
```

**Original attempt and reasoning**

The learner identified that the vowel set contained only lowercase letters and proposed normalizing the input. Their first draft combined `lower_text = text.lower()` on the function-definition line; they then separated the statements and correctly iterated over `lower_text`. They also suggested including both uppercase and lowercase vowels in the set.

**Reference fix**

```python
def count_vowels(text):
    lower_text = text.lower()
    vowels = "aeiou"
    count = 0

    for char in lower_text:
        if char in vowels:
            count += 1

    return count
```

**Learner's final tests**

```python
def test_uppercase():
    assert count_vowels("ElephAnt") == 3

def test_lowercase():
    assert count_vowels("apple") == 2

def test_no_vowels():
    assert count_vowels("hy") == 0
```

All three tests are correct.

**Feedback:** `lower()` returns a new string; it does not change the original string in place. Python code uses quotes for string literals, while a website input field passes typed characters as a string value.

**Status:** Passed — 9/10.

---

## Question 9 — Get a student's score

**Requirement:** Return the score if the key exists; return `None` if the name is missing.

**Buggy code**

```python
def get_score(scores, name):
    return scores[name]
```

**Original attempts**

The learner tried:

```python
def get_score(scores, name=None):
    return scores[name]
```

They reasoned that a default parameter might handle the missing-key case. They later proposed:

```python
def get_score(name: scores):
    return scores[name]
```

**What needed correction**

- `name=None` supplies a default only when the argument is omitted; it does not handle a supplied key missing from the dictionary.
- In `{"Aman": 85}`, `"Aman"` is the key and `85` is the value.
- `name: scores` is not a way to pass a dictionary into a function. A type annotation does not create a parameter.
- Square-bracket lookup raises `KeyError` when a key is missing.

**Reference fix**

```python
def get_score(scores, name):
    return scores.get(name)
```

**Correct tests**

```python
scores = {"Aman": 85, "Riya": 92}

def test_existing_name():
    assert get_score(scores, "Aman") == 85

def test_missing_name():
    assert get_score(scores, "Kabir") is None
```

`scores.get(name, None)` is also correct, although the explicit `None` is redundant because it is already the default.

**Status:** Guided solution; independent mastery unverified. Re-test on a fresh example without hints.

---

## Question 10 — Get a user's language

**Requirement:** Return a user's language if present; otherwise return `"English"`.

**Buggy code**

```python
def get_language(users, name):
    return users[name]
```

**Test data**

```python
users = {
    "Aman": "Hindi",
    "Riya": "French",
    "Sam": "Spanish"
}
```

**Learner's attempt**

```python
def get_language(users, name):
    return user.get(name)

def test_existing_name():
    assert get_language(name, "Aman") == "Hindi"

def test_missing_name():
    assert get_language(name, "Tanish") == None
```

The learner correctly reasoned that `.get()` looks up a key and returns `None` by default if the key is absent. The attempt had three issues:

1. It used `user` instead of the parameter `users`.
2. `users.get(name)` defaults to `None`, whereas the requirement calls for `"English"`.
3. The tests passed `name` instead of the dictionary as the first argument.

**Reference fix**

```python
def get_language(users, name):
    return users.get(name, "English")
```

**Correct tests**

```python
users = {
    "Aman": "Hindi",
    "Riya": "French",
    "Sam": "Spanish"
}

def test_existing_name():
    assert get_language(users, "Aman") == "Hindi"

def test_missing_name():
    assert get_language(users, "Tanish") == "English"
```

**Status:** Guided solution; independent mastery unverified. Re-test without hints before marking this skill mastered.

---

## Summary

**Strengths observed:** simple logic debugging, boundary-test reasoning, recognizing print/return differences, removing duplicates, and normalizing text.

**Priority improvements:** runtime validation, exception tests, Boolean operators, correct function arguments, expected-value types, and dictionary fallbacks.

Questions 11–15 remain pending. New work should test whether these corrections can be applied independently rather than repeat the exact solved examples.
