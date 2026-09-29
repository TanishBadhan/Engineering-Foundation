# Window Functions

Window functions calculate values across a related set of rows while preserving the individual rows in the result.

This makes them fundamentally different from ordinary aggregates.

## 1. Aggregate vs Window

Aggregate:

```text
10 rows
  ↓
SUM
  ↓
1 row
```

Window:

```text
10 rows
  ↓
SUM() OVER (...)
  ↓
10 rows + calculated value
```

This distinction is the foundation of window functions.

## 2. Basic Syntax

```sql
function(...) OVER (
    PARTITION BY ...
    ORDER BY ...
)
```

The `OVER` clause defines the window.

## 3. PARTITION BY

`PARTITION BY` divides rows into independent groups for the window calculation.

Example:

```sql
SELECT
    fname,
    dept,
    salary,
    AVG(salary) OVER (
        PARTITION BY dept
    ) AS department_avg
FROM employees;
```

Every employee remains visible, but each row receives the average salary of its department.

## 4. ORDER BY in a Window

```sql
ROW_NUMBER() OVER (
    PARTITION BY dept
    ORDER BY salary DESC
)
```

This numbers employees within each department from highest salary downward.

## 5. ROW_NUMBER

```sql
SELECT
    fname,
    dept,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY dept
        ORDER BY salary DESC
    ) AS rank_in_dept
FROM employees;
```

`ROW_NUMBER` always gives distinct sequential positions within the window ordering.

## 6. RANK and DENSE_RANK

`RANK` gives tied rows the same rank and leaves gaps after ties.

`DENSE_RANK` gives tied rows the same rank without gaps.

Example conceptually:

```text
salary
100 -> rank 1, dense_rank 1
100 -> rank 1, dense_rank 1
90  -> rank 3, dense_rank 2
```

Choose based on the meaning required by the application.

## 7. LAG

`LAG` accesses a previous row according to the window ordering.

```sql
SELECT
    o_date,
    total,
    LAG(total) OVER (
        ORDER BY o_date
    ) AS previous_total
FROM daily_sales;
```

This enables row-to-row comparisons.

## 8. LEAD

`LEAD` accesses a following row:

```sql
LEAD(total) OVER (
    ORDER BY o_date
)
```

A useful mental model:

```text
LAG  -> look backward
LEAD -> look forward
```

Neither requires `SUM`. They operate on row positions.

## 9. Running Totals

A running total can be calculated with:

```sql
SUM(amount) OVER (
    ORDER BY transaction_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

Unlike `SUM(amount)` with no window, this does not collapse the rows.

## 10. PARTITION + ORDER

These two clauses answer different questions.

```text
PARTITION BY -> Which independent group?
ORDER BY     -> In what sequence?
```

For example:

```sql
ROW_NUMBER() OVER (
    PARTITION BY dept
    ORDER BY salary DESC
)
```

means:

> Restart numbering for each department, ordering employees by descending salary.

## 11. Window Frames

Some window functions use a frame that determines which rows around the current row participate.

Example:

```sql
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
```

This can represent a rolling three-row calculation.

Frames matter especially for running totals, moving averages, and ordered aggregates.

## 12. Common Engineering Use Cases

Window functions are useful for:

- Top-N per group
- Running totals
- Moving averages
- Previous/next record comparison
- Deduplication
- Ranking
- Percentile-style analysis
- Time-series calculations

## 13. Window Functions vs GROUP BY

Use GROUP BY when the desired result grain is one row per group.

Use a window function when you need group-level information while retaining individual rows.

Mental model:

```text
GROUP BY
many rows -> fewer rows

WINDOW
many rows -> same rows + context
```

## Common Mistakes

- Using GROUP BY when individual rows must remain.
- Forgetting the window's ORDER BY when row order matters.
- Assuming RANK and DENSE_RANK behave identically.
- Misunderstanding the window frame.
- Comparing rows without defining a deterministic ordering.

## Engineering Takeaways

Window functions are not merely "advanced aggregates." They are a mechanism for adding context from related rows without losing the original row-level result.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**User-Defined Functions** — encapsulating reusable database-side computations.