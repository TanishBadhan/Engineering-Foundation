# Practice Set 1 — Python Debugging Fundamentals

## Objective

Build the ability to read a function, understand its contract, identify a bug, implement the smallest reliable fix, and write tests that catch the defect.

This set belongs to the standalone [Testing & Debugging Drills module](../README.md).

## Working rules

- Attempt each problem before looking at a solution.
- State the expected behaviour first.
- Use tests to demonstrate the bug and verify the fix.
- Check edge cases, not only typical inputs.
- Preserve the original attempt and record the corrected solution separately.
- A guided answer is not independent mastery until a similar problem is solved without hints.

## Progress

The question order was adjusted during practice. The status below reflects what was actually attempted.

| Question | Topic | Status | Details |
|---|---|---|---|
| 1 | Even/odd logic and assertions | Passed — 9/10 | [Review Q1](tester_drills.md#question-1--even-number) |
| 2 | Inclusive boundaries | Passed — 9/10 | [Review Q2](tester_drills.md#question-2--discount-age-boundary) |
| 3 | Whitespace-only strings | Passed — 8.5/10 | [Review Q3](tester_drills.md#question-3--whitespace-only-username) |
| 4 | Printing versus returning | Passed — 9/10 | [Review Q4](tester_drills.md#question-4--print-versus-return) |
| 5 | Validation and exceptions | Partial — 6/10; reinforce | [Review Q5](tester_drills.md#question-5--input-validation-and-exceptions) |
| 6 | Empty-list edge case | Passed after retries — 7/10 | [Review Q6](tester_drills.md#question-6--first-item-of-a-list) |
| 7 | Removing duplicates and preserving order | Passed — 8.5/10 | [Review Q7](tester_drills.md#question-7--remove-duplicates) |
| 8 | Case-insensitive vowel counting | Passed — 9/10 | [Review Q8](tester_drills.md#question-8--counting-vowels) |
| 9 | Missing dictionary key | Guided solution; independent mastery unverified | [Review Q9](tester_drills.md#question-9--get-a-students-score) |
| 10 | Dictionary fallback value | Guided solution; independent mastery unverified | [Review Q10](tester_drills.md#question-10--get-a-users-language) |
| 11–15 | Practical tests, regression, and issue simulations | Not attempted | Pending |

## Highest-priority revision targets

1. **Exception testing:** a function that raises an exception is not tested by comparing its return value to an exception class. Use a framework assertion such as pytest's `raises`.
2. **Boolean logic:** if either of two conditions should invalidate an input, reason through both cases before choosing `and` or `or`.
3. **Test arguments and expected values:** match the function signature and compare against the correct return type (for example, an integer versus a list containing that integer).
4. **Dictionary lookup:** distinguish the dictionary from the lookup key, and use the fallback required by the specification.
5. **Independent repetition:** solve a similar problem without hints before marking a guided concept as mastered.

## Completion criteria

A question is independently complete when you can:

- describe the bug in your own words;
- fix it without copying a supplied solution;
- write at least two useful tests, including a relevant edge case;
- explain what the tests prove; and
- run the tests locally once a test environment is set up.

See [tester_drills.md](tester_drills.md) for the question-by-question record and [errors_made.md](errors_made.md) for recurring mistakes and correction strategies.
