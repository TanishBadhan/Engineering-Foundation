# GROUP BY and HAVING

`GROUP BY` turns a result set into groups so aggregate functions can calculate a separate result for each group. `HAVING` filters those groups after aggregation.

## 1. GROUP BY

Suppose employees belong to departments:

```text
engineering -> 3 employees
sales       -> 2 employees
finance     -> 4 employees
```

Query:

```sql
SELECT
    dept,
    COUNT(*) AS employee_count
FROM employees
GROUP BY dept;
```

Result conceptually:

```text
engineering | 3
sales       | 2
finance     | 4
```

The database creates one group for each distinct department.

## 2. The Fundamental Rule

When using `GROUP BY`, every selected expression must either:

1. Be included in the grouping keys, or
2. Be aggregated.

Valid:

```sql
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept;
```

Invalid conceptually:

```sql
SELECT dept, fname, AVG(salary)
FROM employees
GROUP BY dept;
```

Why? A department can contain many employees, so PostgreSQL cannot choose one arbitrary `fname` for the department.

The query must define how that value should be represented.

## 3. Multiple Grouping Columns

```sql
SELECT
    dept,
    job_title,
    COUNT(*)
FROM employees
GROUP BY dept, job_title;
```

Now the group is identified by the combination:

```text
(dept, job_title)
```

not by each column independently.

## 4. Aggregates Per Group

```sql
SELECT
    dept,
    COUNT(*) AS employees,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees
GROUP BY dept;
```

This is a common reporting pattern.

## 5. HAVING

`HAVING` filters groups after aggregation.

```sql
SELECT
    dept,
    COUNT(*) AS employee_count
FROM employees
GROUP BY dept
HAVING COUNT(*) >= 3;
```

Conceptually:

```text
Rows
 ↓
GROUP BY
 ↓
Groups
 ↓
Aggregate
 ↓
HAVING
 ↓
Remaining groups
```

## 6. WHERE vs HAVING

This distinction is essential.

`WHERE` filters individual rows before grouping.

```sql
SELECT
    dept,
    AVG(salary)
FROM employees
WHERE salary >= 50000
GROUP BY dept;
```

`HAVING` filters groups after aggregation.

```sql
SELECT
    dept,
    AVG(salary)
FROM employees
GROUP BY dept
HAVING AVG(salary) >= 50000;
```

These queries answer different questions.

### Mental Model

```text
WHERE  -> Which rows participate?
HAVING -> Which groups survive?
```

## 7. Grouping After a JOIN

Many real queries group joined data.

For example, customer spending:

```sql
SELECT
    c.c_id,
    c.c_name,
    SUM(i.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o
    ON o.c_id = c.c_id
JOIN order_items i
    ON i.o_id = o.o_id
JOIN products p
    ON p.p_id = i.p_id
GROUP BY c.c_id, c.c_name;
```

The result contains one row per customer.

## 8. COUNT(DISTINCT ...) in Grouped Queries

Suppose a customer can order the same product many times.

To count different products purchased:

```sql
COUNT(DISTINCT p.p_id)
```

To count orders:

```sql
COUNT(DISTINCT o.o_id)
```

These are different metrics.

This is a common source of incorrect business reports.

## 9. String Aggregation

Sometimes a grouped result needs several values represented in one row.

PostgreSQL provides `STRING_AGG`:

```sql
SELECT
    c_id,
    STRING_AGG(c_name, ', ')
FROM customers
GROUP BY c_id;
```

In practical queries, this can be useful for collecting related names or labels.

The important idea is that a non-grouped attribute cannot simply be selected when multiple rows exist; it needs an explicit aggregation rule.

## 10. GROUP BY Mental Model

Imagine sorting rows into buckets:

```text
Raw rows
   ↓
Choose grouping key
   ↓
Bucket rows
   ↓
Aggregate each bucket
   ↓
Filter buckets with HAVING
   ↓
Return one row per surviving group
```

This model makes grouped queries easier to construct.

## 11. Common Business Queries

GROUP BY is used for:

- Revenue by customer
- Orders by day
- Employees by department
- Products by category
- Average salary by department
- Number of users by country

Example:

```sql
SELECT
    c_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY c_id
HAVING COUNT(*) >= 5;
```

This asks for customers with at least five orders.

## Common Mistakes

- Selecting a non-grouped, non-aggregated column.
- Using HAVING when WHERE would filter rows earlier.
- Forgetting `COUNT(DISTINCT ...)` when duplicates should not count.
- Grouping by the wrong combination of columns.
- Producing misleading metrics after joins because joins can multiply rows.

## Engineering Takeaways

You should be able to determine the intended grain of a result—one row per customer, department, product, day, etc.—then choose grouping keys and aggregates that produce exactly that grain.

That idea of **result grain** is more important than memorizing GROUP BY syntax.

## Practice

The exercises are in `practice.sql`.

## Next Topic

**String Functions** — transforming and inspecting textual data inside PostgreSQL.