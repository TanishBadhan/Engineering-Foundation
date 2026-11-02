# Industrial Log Intelligence CLI

## V1.0 Development Journal

| Project detail | V1.0 |
|---|---|
| Level | Beginner |
| Language | Python 3 |
| Input | Local CSV files |
| Interface | Command-line |
| Dependencies | Python standard library |
| Release | Published as `project-3-v1.0` |

## 1. Overview

Industrial Log Intelligence CLI reads synthetic industrial equipment logs from a CSV file and displays a basic analysis in the terminal. The project is a practical exercise in Python fundamentals and works only with local sample data.

The records are synthetic. The application does not connect to physical equipment or process live telemetry.

## 2. V1.0 Scope

V1.0 can:

- Read CSV records with `csv.DictReader`.
- Display records in aligned terminal columns.
- Count records by severity: INFO, WARNING, ERROR and CRITICAL.
- Count ERROR records by machine ID and message.
- Identify the machine with the highest ERROR count.
- Display the total number of records processed.
- Handle empty files and missing files.

**Counting rule:** Only records whose severity is exactly `ERROR` contribute to machine error counts, recurring error-message counts and the most-error-prone-machine result. `CRITICAL` is included in the severity summary only.

## 3. Processing Flow

1. Open the CSV file using `with open(...)`.
2. Read records as dictionaries with `csv.DictReader`.
3. Store the records in a list and check whether the file contains data.
4. For each record, update the severity, machine and error-message counts.
5. Display the records and summary reports.
6. Display a handled error message if the file cannot be found.

The input file path is set directly in `main.py`; V1.0 does not accept a filename as a command-line argument.

Expected CSV headers:

`timestamp,machine_id,severity,message`

## 4. Concepts Practised

| Concept | Use in the project |
|---|---|
| Variables and counters | Store record values and running totals. |
| Lists and loops | Store and process CSV records. |
| Dictionaries | Track severity, machine and message counts. |
| Conditional statements | Separate ERROR records and handle empty or zero-error data. |
| File handling | Read files with a context manager. |
| Exception handling | Handle `FileNotFoundError`. |
| Built-in functions | Use `list()`, `len()`, `any()` and `max()`. |
| F-strings | Format terminal output. |

## 5. Manual Testing

V1.0 was tested manually with the following cases. It does not include an automated test suite.

| Test file or input | Purpose | Observed behaviour |
|---|---|---|
| `data/machine_log.csv` | Normal dataset | Records and summary reports are displayed. |
| `data/empty_log.csv` | Empty dataset | A no-records message is displayed. |
| `data/no_error.csv` | INFO and WARNING records, with no ERROR records | Severity totals are displayed and zero-error reporting is handled. |
| Non-existent file path | Missing-file handling | A `FileNotFoundError` is caught and a readable message is displayed. |

## 6. Limitations

- Uses synthetic sample data and local CSV files only.
- Does not connect to machines, sensors, controllers or industrial networks.
- Does not include a database, API, GUI, cloud service or machine learning.
- Expects the stated CSV headers and uppercase severity labels; comprehensive input validation is not included.
- Is a learning project, not an industrial monitoring or safety system.

## 7. Next Version

**V2.0 — Functions and code organisation**

Refactor the existing program into a small set of functions. The learning focus is function definitions, parameters, return values and separation of responsibilities. The project will remain beginner-level.

For the development issues and fixes recorded during V1.0, see [V1 Error and Correction Record](../development-notes/V1_ERROR_CORRECTION_RECORD.md).
