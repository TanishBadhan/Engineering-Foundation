# SELECT and Filtering

`SELECT` is the core PostgreSQL query statement. Strong SQL begins with understanding how to control the result set: which columns are returned, which rows qualify, and how expressions are evaluated.

## 1. Basic SELECT

```sql
SELECT *
FROM customers;
```

`*` means all selected columns.

In application code, prefer explicitly naming required columns when practical:

```sql
SELECT c_id, c_name, c_mail
FROM customers;
```

This makes the query's contract clearer and avoids returning unnecessary data.

## 2. Column Aliases

```sql
SELECT
    c_name AS customer_name,
    c_mail AS email
FROM customers;
```

Aliases make result sets easier for application code and humans to interpret.

## 3. Expressions

SQL can calculate values:

```sql
SELECT
    p_name,
    price,
    price * 1.18 AS price_with_tax
FROM products;
```

The database is not limited to returning stored columns; it can compute expressions as part of the query.

## 4. WHERE

`WHERE` filters rows before the final result is produced.

```sql
SELECT *
FROM products
WHERE price > 1000;
```

Multiple conditions:

```sql
SELECT *
FROM products
WHERE price > 1000
  AND p_name <> 'Laptop';
```

Use parentheses when logic could be ambiguous:

```sql
WHERE (price > 1000 AND price < 10000)
   OR p_name = 'Laptop';
```

## 5. Comparison Operators

Common operators:

```text
=       equal
<>      not equal
>       greater than
<       less than
>=      greater than or equal
<=      less than or equal
```

Example:

```sql
SELECT *
FROM products
WHERE price >= 1000;
```

## 6. BETWEEN

```sql
SELECT *
FROM products
WHERE price BETWEEN 500 AND 5000;
```

`BETWEEN` is inclusive at both ends.

Think of it as approximately:

```text
price >= 500 AND price <= 5000
```

## 7. IN

Use `IN` when matching against a set of values:

```sql
SELECT *
FROM employees
WHERE dept IN ('engineering', 'finance');
```

This is often cleaner than a long chain of `OR` conditions.

## 8. LIKE and ILIKE

Pattern matching:

```sql
SELECT *
FROM customers
WHERE c_name LIKE 'T%';
```

`%` matches zero or more characters.

`_` matches one character.

PostgreSQL also supports case-insensitive matching with `ILIKE`:

```sql
SELECT *
FROM customers
WHERE c_name ILIKE 't%';
```

## 9. NULL Filtering

Use:

```sql
WHERE c_mail IS NULL
```

or:

```sql
WHERE c_mail IS NOT NULL
```

Do not use:

```sql
WHERE c_mail = NULL
```

because null represents an unknown/missing state and participates in SQL's three-valued logic.

## 10. DISTINCT

`DISTINCT` removes duplicate result rows.

```sql
SELECT DISTINCT dept
FROM employees;
```

It applies to the complete selected combination:

```sql
SELECT DISTINCT dept, salary
FROM employees;
```

This returns unique pairs, not independently unique values from each column.

## 11. ORDER BY

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

Multiple sort keys:

```sql
ORDER BY price DESC, p_name ASC;
```

The second key breaks ties from the first.

## 12. LIMIT and OFFSET

```sql
SELECT *
FROM products
ORDER BY p_id
LIMIT 10;
```

`OFFSET` skips rows:

```sql
LIMIT 10 OFFSET 20;
```

Offset pagination is simple but can become inefficient or unstable for large, changing datasets. Cursor/keyset pagination is often preferable in production APIs.

## 13. Query Processing Mental Model

A simplified conceptual order is:

```text
FROM
  ↓
WHERE
  ↓
GROUP BY
  ↓
HAVING
  ↓
SELECT
  ↓
DISTINCT
  ↓
ORDER BY
  ↓
LIMIT/OFFSET
```

This is a conceptual processing model, not a literal description of PostgreSQL's physical execution plan.

Understanding it explains why a SELECT alias cannot normally be referenced in the WHERE clause of the same query.

## 14. Backend Connection

An API endpoint might require:

```text
GET /products?min_price=1000&limit=20
```

The backend can translate the request into a parameterized query that filters and limits products.

The important production rule is to use parameters rather than constructing SQL through unsafe string concatenation.

## Common Mistakes

- Selecting `*` everywhere.
- Forgetting parentheses around mixed `AND` / `OR` conditions.
- Comparing directly with `NULL`.
- Assuming `BETWEEN` excludes endpoints.
- Using `OFFSET` pagination blindly for large datasets.
- Building SQL by concatenating untrusted input.

## Engineering Takeaways

You should be able to construct precise result sets using projection, filtering, pattern matching, distinctness, sorting, and limits, while understanding how these operations connect to backend API queries.

## Practice

The exercises are in `practice.sql`.

## Next Topic

**Aggregate Functions** — reducing many rows into meaningful numerical or statistical summaries.