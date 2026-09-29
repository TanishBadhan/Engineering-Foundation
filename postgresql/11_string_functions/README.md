# String Functions

PostgreSQL provides functions and operators for inspecting, transforming, formatting, and comparing text. These are useful for cleaning imported data, formatting API results, normalizing values, and building queries over textual fields.

## 1. Why String Functions Matter

Raw application data is rarely perfectly formatted.

Examples:

```text
"  Tanish Badhan  "
"TANISH@example.com"
"Punjab, India"
```

Database expressions can normalize or transform such values without requiring every transformation to happen in application code.

## 2. LENGTH

```sql
SELECT
    c_name,
    LENGTH(c_name) AS name_length
FROM customers;
```

It returns the number of characters for text.

## 3. UPPER and LOWER

```sql
SELECT
    UPPER(c_name) AS upper_name,
    LOWER(c_mail) AS normalized_email
FROM customers;
```

These are common for display formatting and normalization.

## 4. TRIM

```sql
SELECT TRIM('   Tanish   ');
```

Related functions include:

```sql
LTRIM(...)
RTRIM(...)
BTRIM(...)
```

A common cleanup pattern is:

```sql
LOWER(TRIM(c_mail))
```

## 5. CONCAT

```sql
SELECT CONCAT(fname, ' ', lname)
FROM employees;
```

`CONCAT` handles null arguments more conveniently than manual `||` expressions in many cases.

The concatenation operator is:

```sql
fname || ' ' || lname
```

Choose the form based on the required null behavior and readability.

## 6. SUBSTRING

```sql
SELECT SUBSTRING(c_name FROM 1 FOR 5)
FROM customers;
```

This extracts part of a string.

It is useful for controlled parsing and formatting, but complicated parsing logic may be clearer in application code or a dedicated data-processing step.

## 7. REPLACE

```sql
SELECT REPLACE(c_name, ' ', '_')
FROM customers;
```

This replaces matching text.

## 8. POSITION

```sql
SELECT POSITION('@' IN c_mail)
FROM customers;
```

This can locate a substring.

## 9. SPLIT_PART

PostgreSQL provides `SPLIT_PART` for delimiter-based extraction:

```sql
SELECT SPLIT_PART(c_mail, '@', 1)
FROM customers;
```

For an email address this extracts the part before `@`.

## 10. String Aggregation

`STRING_AGG` combines multiple rows into one string:

```sql
SELECT
    dept,
    STRING_AGG(fname, ', ')
FROM employees
GROUP BY dept;
```

This is an aggregate, not merely a string transformation.

It becomes useful when one result row needs a human-readable list of related values.

## 11. NULL and Strings

String functions can behave differently when arguments are null.

For example, concatenation with `||` can produce null if one operand is null.

If a fallback is appropriate:

```sql
COALESCE(fname, '')
```

can provide an explicit replacement.

Do not replace null blindly; missing information and empty text are different states.

## 12. Practical Normalization

A common pattern for case-insensitive email normalization is:

```sql
LOWER(TRIM(c_mail))
```

If the normalized value must be unique, consider enforcing that property through an appropriate schema design rather than relying only on a query-time transformation.

## Common Mistakes

- Confusing characters with bytes when thinking about text size.
- Ignoring null behavior.
- Performing complicated parsing in SQL without considering maintainability.
- Assuming `LOWER` is a universal substitute for proper case-insensitive identity rules.
- Using string functions where a native data type would be more appropriate.

## Engineering Takeaways

You should be able to clean, format, split, combine, search, and aggregate text while understanding null behavior and when transformation belongs in SQL versus application code.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**ALTER TABLE** — evolving an existing PostgreSQL schema safely.