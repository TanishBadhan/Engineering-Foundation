# Industrial Log Intelligence CLI

## V1.0 — Error and Correction Record

This document summarises the main debugging issues encountered while building V1.0. These are historical issues that were corrected during development; they are not a list of known defects in the released version.

| # | Problem encountered | Cause | Correction and lesson |
|---:|---|---|---|
| 1 | Normal CSV processing did not run as expected. | The processing code was placed under `except`, which runs only when the handled exception occurs. | Keep normal processing in the `try` path and reserve `except` for error handling. |
| 2 | An error message did not appear. | A string expression was written without calling `print()`. | Call `print()` to display the message. An expression alone does not print it. |
| 3 | A counter repeatedly returned to zero or was unavailable. | Initialisation was placed inside a loop or an exception branch. | Initialise counters once, before the loop that updates them and within the successful file-processing path. |
| 4 | Reading failed after leaving the file block. | The code attempted to use the file reader after the `with` block had closed the file. | Read and process the records inside the `with` block. |
| 5 | Error statistics included the wrong records or only considered the last record. | The severity condition and counter updates were placed at the wrong level relative to the record loop. | Check each row inside the loop and update machine and message error counts only when severity is exactly `ERROR`. |
| 6 | A new machine ID caused a `KeyError`. | The machine-count dictionary was created with a fixed set of machine IDs. | Start with an empty dictionary and add each machine ID when it is first encountered. |
| 7 | Machines with zero errors were missing from the report. | Machine IDs were added only inside the `ERROR` condition. | Register each machine for every record, then increment its count only for an `ERROR` record. |
| 8 | A machine was reported as most error-prone when all counts were zero. | `max()` can return a key even when every stored count is zero. | Check `any(Error_Count_By_Machine.values())` before calling `max()`. |
| 9 | The record loop produced no output after checking the file. | `list(reader)` consumed the CSV reader, but the code then tried to iterate over the original reader again. | Process the stored list of rows instead of the exhausted reader. |
| 10 | The empty-file message and log heading appeared in the wrong order. | Output statements were placed outside the appropriate empty/non-empty branch or in the wrong position. | Check for records first; place the log heading immediately before the record loop in the non-empty branch. |
| 11 | The no-error CSV did not expose the expected column names. | A blank line appeared before the CSV header, so the reader treated that line as the header. | Remove the leading blank line so the header is the first row. |
| 12 | Explanatory text in the CSV caused an unexpected severity value and a `KeyError`. | Prose had been appended to the CSV and was parsed as a data row. | Keep explanations in documentation, not in the CSV data file. |

## Key Takeaway

Most V1.0 bugs came from code placement, loop conditions, dictionary initialisation, iterator behaviour or malformed input data. The debugging process was to inspect the code and terminal output, identify the actual cause, make one focused correction, and run the affected test again.
