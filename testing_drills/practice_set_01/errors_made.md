# Errors Made — Practice Set 1

This file records specific mistakes, their causes, the correction, and how to verify improvement. It should be updated when a new recurring pattern appears.

## 1. Reversing a Boolean condition

**Observed in:** Q1.

**Mistake:** The even-number function returned true when the remainder was 1.

**Correction:** An integer is even when `number % 2 == 0`.

**Improvement:** The learner corrected the condition, tested an even and odd value, and explained the defect.

**Verify next:** Debug a fresh condition without being told which operator to change.

## 2. Missing inclusive boundaries

**Observed in:** Q2.

**Mistake:** `age > 5 and age < 17` excludes 5 and 17.

**Correction:** Use `age >= 5 and age <= 17`, or `5 <= age <= 17`.

**Improvement:** The learner tested both boundaries and understood why one typical interior value was insufficient.

**Verify next:** Test the lower bound, upper bound, one value below, one above, and an ordinary in-range value.

## 3. Treating whitespace as a meaningful username

**Observed in:** Q3.

**Mistake:** `len(username) > 0` accepts spaces-only input.

**Correction:** Check the content after `username.strip()`.

**Improvement:** The learner understood why spaces count toward the original string's length.

**Verify next:** Test an empty string, whitespace-only input, and a normal username.

## 4. Confusing output with return values

**Observed in:** Q4.

**Mistake:** Printing a result when the caller needs the function's return value.

**Correction:** Use `return result`.

**Improvement:** The learner correctly explained that a function with no explicit return produces `None`.

**Verify next:** Write an assertion for a function's result rather than relying on screen output.

## 5. Incorrect function parameter annotation syntax

**Observed in:** Q5.

**Mistake:** Trying `def age_next_year(int age)`.

**Correction:** Python annotation syntax is `def age_next_year(age: int):`.

**Important distinction:** An annotation expresses the intended type for readers and tools; it does not automatically enforce the type at runtime.

**Verify next:** Annotate a function and separately implement runtime validation.

## 6. Testing an exception as though it were a return value

**Observed in:** Q5.

**Mistake:** Comparing a function call to the `ValueError` class.

**Why it is wrong:** A raised exception interrupts normal return; it is not returned as the ordinary result.

**Correction:** With pytest, use an exception assertion:

```python
import pytest

def test_invalid_value_raises():
    with pytest.raises(ValueError):
        age_next_year(-2)
```

**Verify next:** Test one valid input and each specified invalid input, checking the exact expected exception.

## 7. Choosing `and` or `or` without checking every case

**Observed in:** Q5.

**Mistake:** Combining an invalid type and a negative age with `and`.

**Why it is wrong:** If either condition makes the input invalid, requiring both to be true misses some invalid cases.

**Correction:** For the rule “reject if age is not an integer or age is negative,” reason toward `type(age) is not int or age < 0`. This strict type check also rejects booleans, which are a subclass of `int`.

**Verify next:** Build a small truth table and test each invalid input separately.

## 8. Invalid empty-list syntax

**Observed in:** Q6.

**Mistake:** Writing `items[]`.

**Correction:** The empty list literal is `[]`. Accessing `items[0]` is only safe when the list has an element.

**Verify next:** Test one-item, multi-item, and empty lists.

## 9. Passing the wrong number or shape of arguments

**Observed in:** Q6.

**Mistake:** Calling `first_item(1, 2, 3)` when the function accepts one list, or calling `first_item()` without its required argument.

**Correction:** Use `first_item([1, 2, 3])` or `first_item([])`.

**Verify next:** Read the function signature before writing the test call.

## 10. Confusing an item with a list containing that item

**Observed in:** Q6.

**Mistake:** Expecting `[1]` when the function returns `items[0]`.

**Correction:** The first element of `[1, 2, 3]` is the integer `1`; `[1]` is a different value with a different type.

**Verify next:** Before writing the expected value, trace the return expression and identify both its value and type.

## 11. Misspelling or changing the function name

**Observed in:** Q6 and Q9–Q10.

**Mistake:** The test uses a name that does not exactly match the defined function, such as a misspelled function identifier.

**Correction:** Match the exact identifier and case. For pytest, normally start test function names with `test_`.

**Verify next:** Check each function name in every assertion before running tests.

## 12. Appending the whole list instead of the current item

**Observed in:** Q7.

**Mistake:** Using `result.append(items)` inside the loop.

**Correction:** Use `result.append(item)` to append the current element.

**Improvement:** The learner identified and fixed this bug independently.

**Verify next:** Test mixed duplicates such as `[3, 1, 3, 2, 1]`, expected to produce `[3, 1, 2]`.

## 13. Misdescribing what order is preserved

**Observed in:** Q7.

**Mistake:** Saying the original indexes remain unchanged.

**Correction:** The loop processes the input in order, and the resulting list preserves the relative order of the first occurrence of each retained value. The output indexes can differ because duplicates are removed.

**Verify next:** Use interleaved duplicate values and explain the output sequence.

## 14. Case-sensitive string comparison

**Observed in:** Q8.

**Mistake:** Comparing characters only with lowercase vowels.

**Correction:** Normalize the text with `text.lower()`, or include uppercase and lowercase vowels in the set.

**Improvement:** The learner independently chose normalization and correctly tested mixed-case, lowercase, and no-vowel inputs.

**Verify next:** Test a mixed-case string and explain that `lower()` returns a new string.

## 15. Expecting a type annotation to replace string quotes

**Observed in:** Q8 discussion.

**Misunderstanding:** Thinking that `text: str` allows a bare word to be passed as a string literal.

**Correction:** `count_vowels("ElephAnt")` passes a string literal; `count_vowels(ElephAnt)` looks up a variable. Website input fields accept raw text because the form supplies that text as a value to the program.

**Verify next:** Store a literal in `word = "ElephAnt"`, then pass `word` to the function.

## 16. Using a default parameter to handle a missing dictionary key

**Observed in:** Q9.

**Mistake:** Trying `def get_score(scores, name=None): return scores[name]`.

**Why it fails:** The parameter default applies only when the caller omits `name`. It does not handle a supplied key that is absent from the dictionary.

**Correction:** Use `scores.get(name)` or `scores.get(name, default)`.

**Verify next:** Test an existing key and a missing key in a new dictionary.

## 17. Confusing the dictionary, key, and value

**Observed in:** Q9.

**Mistake:** Misidentifying the score as the key in a name-to-score mapping.

**Correction:** In `{"Aman": 85}`, `"Aman"` is the key and `85` is the value.

**Verify next:** For every dictionary lookup, identify the dictionary variable, key, and value separately.

## 18. Confusing a type annotation with a function parameter

**Observed in:** Q9.

**Mistake:** Trying `def get_score(name: scores)` to give the function access to the dictionary.

**Correction:** Declare both values as parameters: `def get_score(scores, name):`. An annotation after a colon does not declare a separate argument.

**Verify next:** Match all names used in the function body to parameters or variables defined in scope.

## 19. Returning the wrong fallback value

**Observed in:** Q10.

**Mistake:** Using `users.get(name)`, which returns `None` when a key is absent, despite the requirement specifying `"English"`.

**Correction:** Use `users.get(name, "English")`.

**Verify next:** Write the exact required output for a missing-key case before choosing the method's fallback.

## 20. Wrong argument order and variable name

**Observed in:** Q10.

**Mistake:** Calling `get_language(name, "Aman")` instead of `get_language(users, "Aman")`, and using `user` when the defined parameter is `users`.

**Correction:** Match positional arguments to the function signature and use the exact variable name in scope.

**Verify next:** Label the intended argument for each parameter before running the test.

---

## Current strengths

- Identifies straightforward logic defects.
- Understands boundary-test value.
- Distinguishes printing from returning.
- Correctly implemented duplicate removal and case normalization.
- Can improve code and tests using targeted feedback.

## Next practice priorities

1. Solve a fresh exception-handling problem independently.
2. Write test calls with correct arguments and expected types on the first attempt.
3. Re-solve a missing-key problem without hints.
4. Use mixed and boundary inputs rather than only typical examples.
5. Progress to reproducing a small issue and adding regression tests.

Mark a topic as mastered only after the learner solves a new, similar problem without the correction being supplied first.
