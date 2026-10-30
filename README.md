# Engineering Foundations

[![Python application](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/python-app.yml)
[![Engineering Foundation Checks](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/TanishBadhan/Engineering-Foundation/actions/workflows/validate.yml)

A hands-on repository for building software engineering foundations through structured notes, small examples, and deliberate debugging practice.

## Learning modules

| Module | Focus | Entry point |
|---|---|---|
| Python | Language fundamentals through modern Python and concurrency foundations | [Browse Python](./python/) |
| SQL & PostgreSQL | SQL, relational design, querying, transactions, and database-side programming | [Roadmap](./postgresql/README.md) |
| Linux & Bash | Shell usage, files, processes, permissions, system tools, networking, SSH, and scripting | [Roadmap](./linux/README.md) |
| Computer networking | Addressing, protocols, ports, network models, TCP/UDP, and Python sockets | [Roadmap](./computer_network/README.md) |
| Testing & debugging | Practice drills, edge cases, bug analysis, and recurring-mistake tracking | [Guide](./testing_drills/README.md) |

## Repository architecture

The top-level layout separates learning domains. The topic names below match the current repository.

```text
Engineering-Foundation/
├── .github/workflows/
│   ├── python-app.yml
│   └── validate.yml
├── python/
├── postgresql/
│   ├── 00_setup/
│   │   ├── README.md
│   │   ├── schema.sql
│   │   └── seed.sql
│   └── README.md
├── linux/
│   └── README.md
├── computer_network/
│   ├── 01-ip-addressing-and-subnetting/
│   ├── 02-protocols-ports-and-network-models/
│   ├── TCP-UDP/
│   │   ├── 01-TCP/
│   │   ├── 02-UDP/
│   │   ├── 03-Python-Sockets/
│   │   └── README.md
│   └── README.md
├── testing_drills/
│   ├── README.md
│   └── practice_set_01/
│       ├── README.md
│       ├── tester_drills.md
│       └── errors_made.md
└── README.md
```

### Python curriculum — 19 topic directories

| | | |
|---|---|---|
| [01 — Variables & object model](./python/01_variables%26objectmodel/) | [02 — Data types & data structures](./python/02_DataTypes_And_DataStructures/) | [03 — Operators & expressions](./python/03_operators%26expressions/) |
| [04 — Conditional logic](./python/04_Conditional_logics/) | [05 — Iterations & loops](./python/05_Iterations_And_Loops/) | [06 — Strings](./python/06_strings/) |
| [07 — Functions](./python/07_functions/) | [08 — Comprehensions & functional patterns](./python/08_comprehensions%26functionalpatterns/) | [09 — Modules & packages](./python/09_modules%26packages/) |
| [10 — Object-oriented programming](./python/10_object-oriented-programming/) | [11 — Error handling & exceptions](./python/11_error-handling%26exceptions/) | [12 — File I/O](./python/12_file-io/) |
| [13 — Iterators, generators & context managers](./python/13_iterators-generators%26context-managers/) | [14 — Decorators & closures](./python/14_decorators%26closures/) | [15 — Python internals & execution model](./python/15_python-internals%26execution-model/) |
| [16 — Standard library foundations](./python/16_standard-library-foundations/) | [17 — Testing & code quality](./python/17_testing%26code-quality/) | [18 — Type system & modern Python](./python/18_type-system%26modern-python/) |
| [19 — Concurrency foundations](./python/19_concurrency-foundations/) | | |

### Python projects

- [Project 1 — Engineering Foundation Calculator](./python/projects/project_1/README.md)

### PostgreSQL curriculum — 22 topic directories

| Topic range | Includes |
|---|---|
| 00 | [Setup: schema and seed data](./postgresql/00_setup/) |
| 01–08 | Database fundamentals, SQL command categories, PostgreSQL CLI, database/table creation, data types, constraints, insert/update/delete, select/filtering |
| 09–15 | Aggregate functions, GROUP BY/HAVING, string functions, ALTER TABLE, relationships/foreign keys, joins, CASE/COALESCE |
| 16–19 | Transactions/TCL, views, CTEs, window functions |
| 20–22 | User-defined functions, stored procedures, triggers |

### Linux curriculum — 16 topic directories

| Topic range | Includes |
|---|---|
| 01–04 | Linux and shell fundamentals, filesystem/navigation, files/directories, reading/inspecting files |
| 05–08 | Search/text processing, pipes/redirection/shell control, processes/job control, disk/system resources |
| 09–12 | Users/ownership/permissions, environment variables/PATH, archives/compression, shell editing/productivity |
| 13–16 | Services/system logs, Linux networking, SSH/remote computing, basic Bash scripting |

### Where to start

- **Python:** open any numbered topic folder; the topic README and examples live inside the folder.
- **PostgreSQL:** start with the [roadmap](./postgresql/README.md) and use [00_setup](./postgresql/00_setup/) for the shared practice schema and seed data.
- **Linux:** start with the [roadmap](./linux/README.md); numbered folders group related lessons.
- **Networking:** use the [roadmap](./computer_network/README.md), then explore [TCP/UDP and Python sockets](./computer_network/TCP-UDP/README.md).
- **Testing:** follow the [practice-set guide](./testing_drills/practice_set_01/README.md), work through [tester_drills.md](./testing_drills/practice_set_01/tester_drills.md), and maintain [errors_made.md](./testing_drills/practice_set_01/errors_made.md).

## Continuous integration

| Workflow | Checks | Limitation |
|---|---|---|
| [Python application](./.github/workflows/python-app.yml) | Critical Flake8 errors fail the job; other lint findings are informational. | Pytest runs only when `test_*.py` or `*_test.py` files exist. |
| [Engineering Foundation Checks](./.github/workflows/validate.yml) | Python syntax checks in `python/` and `testing_drills/`; Bash syntax checks in `linux/` using `bash -n`. | Syntax checks do not prove runtime correctness; Bash scripts are parsed, not executed. |

The badges at the top show the latest applicable workflow status for `main`. A green status means the configured checks passed; it does not imply a pytest suite ran if no matching tests exist.

## Working principles

1. Understand the concept and why it exists.
2. Inspect examples and trace their behavior.
3. Practice with small changes and edge cases.
4. Verify with appropriate checks and tests.
5. Document assumptions, mistakes, and lessons.

This is an evolving learning repository. It aims to show progress and verification without overstating mastery or production readiness.

## Maintainer

**Tanish Badhan** · [GitHub profile](https://github.com/TanishBadhan)
