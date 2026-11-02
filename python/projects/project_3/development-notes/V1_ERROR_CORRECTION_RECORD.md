Industrial Log Intelligence CLI
V1.0 — Error and Correction Record
This document records the development and debugging issues encountered while building V1. It is kept separately from the main development journal so the project overview stays readable while the debugging history remains available as a focused learning record.

The issues below are based on the problems encountered during development. They are not claims that the program contains these errors in its final V1 state.
1. Empty input displayed report headings
Observed behaviour
The program displayed report headings even when the CSV contained no data records.

Cause
The program began displaying or generating reports before checking whether any records had been read.

Correction made
The CSV reader was converted into a list, and the program checked whether the list contained records before entering the record-processing and reporting path.
rows = list(reader)

if len(rows) == 0:
    print("No records found")
else:
    # Process and report the records here.
What was learned
Check whether required input exists before running code that depends on it. This introduced practical use of list(), len(), and conditional statements.
2. The original CSV reader was used after it had been consumed
Observed behaviour
After converting the reader into a list, an earlier version still attempted to process records by looping over the original reader. That loop had no records left to return.

Cause
list(reader) consumes the iterator to retrieve its records. The original reader is therefore exhausted after the conversion.

Correction made
The later processing loop was changed to iterate over rows, the list containing the records.
rows = list(reader)

for row in rows:
    # Process each stored record.
What was learned
An iterator is not the same as a reusable list. Once an iterator has been consumed, use the stored list when the records need to be processed again.
3. The ALL LOGS heading appeared in the wrong place
Observed behaviour
The heading and record output did not appear in the intended order in an earlier version.

Cause
The heading was placed outside the branch that checked whether records existed, or after the record-display loop, rather than immediately before the loop.

Correction made
The heading was moved inside the non-empty-record branch and placed before the loop that prints each record.

What was learned
Indentation controls which statements belong to a conditional block. The position of a statement also determines the order of terminal output.
4. The program checked for dictionary entries instead of non-zero error counts
Observed behaviour
A check that the machine error-count dictionary contained entries was not enough to establish that an error had actually occurred. Machines with zero errors could still be present in the dictionary.

Cause
A dictionary can contain keys even when every associated value is zero. Checking the dictionary itself tests whether it has entries, not whether any count is non-zero.

Correction made
The program uses any() on the dictionary's values before identifying the most error-prone machine.
if any(Error_Count_By_Machine.values()):
    Most_Error_Machine = max(
        Error_Count_By_Machine,
        key=Error_Count_By_Machine.get
    )
else:
    print("No errors recorded across any machine.")
What was learned
Understand what a condition actually checks. any(values) checks whether at least one value is truthy; it is different from checking whether a dictionary contains keys.
5. A blank first line prevented the CSV header from being read correctly
Observed error
KeyError: 'machine_id'
A temporary diagnostic print showed:
CSV Headers: []
Cause
The no_error.csv file contained a blank line before the actual header. csv.DictReader treated that first line as the header row. As a result, the dictionaries produced for subsequent records did not have the expected machine_id key.

Investigation performed
The file was inspected with:
ls -l data/no_error.csv
cat -A data/no_error.csv
The cat -A output exposed the empty first line before timestamp,machine_id,severity,message.

Correction made
The leading blank line was removed so the first line of the file was the actual CSV header:
timestamp,machine_id,severity,message
What was learned
A file can contain many records and still have a malformed header. Inspect the actual input file when the parser's output contradicts expectations.
6. Explanatory text was accidentally included as a CSV record
Observed error
After the header was corrected, the program raised a KeyError while updating the severity counter:
Severity_count[Severity] += 1
The unexpected value shown in the traceback was not one of the supported severity labels.

Cause
An explanatory note had been appended to the bottom of no_error.csv. A normal CSV reader does not automatically ignore arbitrary comment text. Since the note contained commas, the reader split it into fields and treated it as another row. Part of the note was consequently read as the severity value.

Correction made
The explanatory note was removed from the CSV file. The file was left with only its header and valid data records.

What was learned
Keep documentation outside the data file. CSV files should contain records that follow the declared column structure; arbitrary prose is not automatically treated as a comment.
Summary
No.	Issue	Correction
1	Empty input displayed report headings.	Check the stored record list before processing.
2	The original reader was reused after being consumed.	Iterate over the stored rows list.
3	The ALL LOGS heading appeared in the wrong position.	Place it before the record loop inside the non-empty branch.
4	Dictionary presence was mistaken for the presence of errors.	Check the stored counts with any().
5	A leading blank line was read as the CSV header.	Remove the blank line and use the correct header as the first line.
6	Explanatory prose was parsed as a CSV record.	Remove the prose from the data file.