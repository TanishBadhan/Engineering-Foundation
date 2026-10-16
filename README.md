# Engineering Foundations

[![Python application](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/python-app.yml)
[![Engineering Foundation Checks](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/validate.yml)

A structured, hands-on repository for building software engineering foundations through focused notes, practical examples, and deliberate debugging practice.

The repository is organized by learning domain. Each module maintains its own roadmap and topic-level documentation; planned work is distinguished from material already studied or verified.

## Learning modules

| Module | Scope | Start here |
|---|---|---|
| **Python** | Language fundamentals, data structures, functions, OOP, exceptions, files, modules, code quality, typing, and concurrency foundations | [Python curriculum](./python/) |
| **SQL & PostgreSQL** | Relational databases, schema structure, querying, joins, transactions, advanced SQL, and database-side programming | [PostgreSQL roadmap](./postgresql/README.md) |
| **Linux & Bash** | Shell fundamentals, filesystem, text processing, processes, permissions, system inspection, networking, SSH, and scripting | [Linux roadmap](./linux/README.md) |
| **Computer networking** | Networking fundamentals, addressing, protocols, TCP/UDP, and Python socket labs; additional topics are planned | [Networking roadmap](./computer_network/README.md) |
| **Testing & debugging** | Bug investigation, input validation, edge cases, test reasoning, and a log of recurring mistakes | [Practice guide](./testing_drills/README.md) |

## Repository architecture

The top-level folders separate learning areas; each module contains its own notes and examples.

```text
Engineering-Foundation/
├── .github/
│   └── workflows/
│       ├── python-app.yml   # Linting and conditional pytest
│       └── validate.yml     # Python and Bash syntax checks
├── python/                  # Numbered Python topic modules
├── postgresql/              # SQL and PostgreSQL lessons
│   └── 00_setup/            # Shared schema and seed data
├── linux/                   # Linux notes and Bash examples
├── computer_network/        # Networking notes and socket exercises
├── testing_drills/          # Cross-cutting debugging practice
│   └── practice_set_01/
└── README.md                # Repository entry point
```

### Module conventions

- **Python:** follow the numbered topic folders from language basics through more advanced foundations. Open the topic README before working through its examples.
- **PostgreSQL:** progress through the numbered lessons. The shared practice database setup lives in [schema.sql](./postgresql/00_setup/schema.sql) and [seed.sql](./postgresql/00_setup/seed.sql).
- **Linux:** topic folders pair explanations with shell examples where provided. Scripts are syntax-checked by CI, not automatically executed.
- **Networking:** use the module README for the roadmap and current coverage. Topics marked planned or pending should not be treated as completed.
- **Testing drills:** work through the [practice-set guide](./testing_drills/practice_set_01/README.md), record mistakes in the [error log](./testing_drills/practice_set_01/errors_made.md), and distinguish independently solved exercises from guided practice.

## Continuous integration

The badges at the top link to the repository's GitHub Actions workflows. Their status is dynamic and updates as workflow runs complete.

| Workflow | Checks | Important limitation |
|---|---|---|
| [Python application](./.github/workflows/python-app.yml) | Critical Flake8 errors fail the job; other lint findings are currently reported as warnings. | Pytest runs only when files named `test_*.py` or `*_test.py` are present. |
| [Engineering Foundation Checks](./.github/workflows/validate.yml) | Compiles Python files under `python/` and `testing_drills/`; parses Bash scripts under `linux/` using `bash -n`. | Syntax validation does not prove that examples behave correctly; Bash scripts are not executed. |

A passing badge means that the relevant workflow's configured checks passed for the latest applicable run. If no pytest test files exist, the Python workflow intentionally skips pytest; a green status does not imply a test suite is present.

## Working principles

1. **Understand:** explain what a concept does and why it exists.
2. **Inspect:** read the example and trace its behavior.
3. **Practice:** change or implement a small example and consider edge cases.
4. **Verify:** use suitable checks and tests rather than relying only on visual inspection.
5. **Document:** record assumptions, common mistakes, and useful lessons.

This is an evolving learning repository. Its goal is to make progress and verification visible without overstating mastery or production readiness.

## Maintainer

**Tanish Badhan** · [GitHub profile](https://github.com/TanishBadhan)
