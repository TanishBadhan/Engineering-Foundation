# Testing & Debugging Drills

A standalone practice module for building practical debugging, test-writing, and bug-investigation skills. It supports Python practice now and prepares for future open-source contributions.

This folder lives at the **repository root**, alongside `python/`, `linux/`, and `postgresql/`. It is deliberately separate from the Python curriculum: testing and debugging are transferable engineering skills, not just a Python topic.

## Start here

- [Practice Set 1 — overview and progress](practice_set_01/README.md)
- [Practice Set 1 — questions, attempts, feedback, and solutions](practice_set_01/tester_drills.md)
- [Errors made — correction and improvement log](practice_set_01/errors_made.md)

## Workflow for every drill

1. Read the requirement and state expected behaviour.
2. Identify or reproduce the bug with a small input.
3. Explain the cause before changing code.
4. Make the smallest correct fix.
5. Test normal cases, edge cases, and relevant invalid inputs.
6. Explain what each test proves.
7. Record mistakes and verify learning with a new problem.

## Scoring standard

Each question is evaluated on bug identification and reasoning, implementation, test quality, and explanation. A solution completed after hints is recorded as guided practice, not independent mastery.

## Folder architecture

```text
testing_drills/
├── README.md
└── practice_set_01/
    ├── README.md
    ├── tester_drills.md
    └── errors_made.md
```

## Completion standard

The goal is not just to finish questions. The target is to reproduce a bug, implement a minimal fix, write meaningful regression tests, and explain the change without being given the solution first. Later sets will progress from small functions to bug reports and beginner-friendly open-source issue simulations.
