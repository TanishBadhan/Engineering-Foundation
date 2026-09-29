# CASE and COALESCE

`CASE` provides conditional logic inside SQL expressions. `COALESCE` provides the first non-null value from a list of expressions.

Together they are useful for classification, formatting, fallback values, and business rules.

## 1. CASE

Basic form:

```sql
SELECT
    p_name,
    price,
    CASE
        WHEN price >= 50000 THEN 'premium'
        WHEN price >= 10000 THEN 'mid-range'
        ELSE 'budget'
    END AS price_category
FROM products;
```

Each row is classified independently.

## 2. Simple CASE

You can compare one expression against multiple values:

```sql
CASE dept
    WHEN 'engineering' THEN 'technical'
    WHEN 'sales' THEN 'business'
    ELSE 'other'
END
```

This is useful when matching discrete values.

## 3. Searched CASE

The more general form uses Boolean conditions:

```sql
CASE
    WHEN salary >= 100000 THEN 'high'
    WHEN salary >= 50000 THEN 'medium'
    ELSE 'low'
END
```

Conditions are evaluated in order, so ordering matters when ranges overlap.

## 4. CASE in Aggregation

Conditional aggregation is extremely useful:

```sql
SELECT
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE salary >= 50000) AS above_50k
FROM employees;
```

PostgreSQL's `FILTER` syntax is often clearer than a `CASE` expression for conditional aggregates.

A CASE-based equivalent can also be built:

```sql
SUM(
    CASE WHEN salary >= 50000 THEN 1 ELSE 0 END
)
```

The important concept is that a condition can determine which rows contribute to a metric.

## 5. COALESCE

```sql
SELECT
    c_name,
    COALESCE(c_mail, 'No email')
FROM customers;
```

If `c_mail` is null, the fallback is returned.

With multiple arguments:

```sql
COALESCE(primary_phone, secondary_phone, 'No phone')
```

PostgreSQL returns the first non-null expression.

## 6. NULLIF

`NULLIF(a, b)` returns NULL when `a = b`; otherwise it returns `a`.

Example:

```sql
NULLIF(quantity, 0)
```

This is useful when a zero value should be treated as absent for a particular calculation.

A common pattern for avoiding division by zero is:

```sql
revenue / NULLIF(order_count, 0)
```

## 7. CASE + COALESCE

These can be combined:

```sql
CASE
    WHEN COALESCE(salary, 0) >= 100000 THEN 'high'
    ELSE 'standard'
END
```

But be careful: treating missing salary as zero is a business decision, not merely a technical convenience.

## 8. Business Classification

SQL can encode deterministic classification rules:

```text
raw value
   ↓
CASE
   ↓
business category
   ↓
GROUP BY / reporting
```

For example, products can be classified by price, employees by salary band, or orders by status.

## Common Mistakes

- Ordering overlapping CASE conditions incorrectly.
- Forgetting ELSE and unintentionally returning NULL.
- Treating missing values as zero without considering meaning.
- Using COALESCE to hide data-quality problems.
- Building complicated business logic in SQL that becomes difficult to test.

## Engineering Takeaways

You should be able to express conditional classification, fallback behavior, null-safe calculations, and conditional metrics while distinguishing data cleaning from business rules.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**Transactions and TCL** — making multiple database operations behave as a controlled unit.