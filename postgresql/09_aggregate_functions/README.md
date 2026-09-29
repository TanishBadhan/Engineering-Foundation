# Aggregate Functions

Aggregate functions summarize multiple rows into a single value. They are essential for analytics, reporting, dashboards, business metrics, and backend queries that need summaries rather than raw records.

## 1. Core Idea

Given:

```text
orders
100
250
400
```

an aggregate can turn those rows into:

```text
SUM -> 750
AVG -> 250
COUNT -> 3
```

Common PostgreSQL aggregates include:

- `COUNT`
- `SUM`
- `AVG`
- `MIN`
- `MAX`

## 2. COUNT

Count rows:

```sql
SELECT COUNT(*)
FROM customers;
```

Count non-null values:

```sql
SELECT COUNT(c_mail)
FROM customers;
```

These are not always equivalent because `COUNT(column)` ignores null values.

`COUNT(DISTINCT column)` counts unique non-null values:

```sql
SELECT COUNT(DISTINCT c_id)
FROM orders;
```

## 3. SUM

```sql
SELECT SUM(price)
FROM products;
```

For order items, a useful pattern is:

```sql
SELECT SUM(quantity * price)
FROM order_items;
```

The expression is evaluated per row and then aggregated.

## 4. AVG

```sql
SELECT AVG(price)
FROM products;
```

Like many aggregates, `AVG` ignores null inputs.

If a calculation needs a particular treatment of missing values, make that behavior explicit.

## 5. MIN and MAX

```sql
SELECT
    MIN(price) AS cheapest,
    MAX(price) AS most_expensive
FROM products;
```

Aggregates are not restricted to numeric columns. PostgreSQL supports aggregation for compatible data types where ordering or other required semantics exist.

## 6. NULL Behavior

A critical rule:

```text
Most aggregates ignore NULL input values.
```

For example, if salaries are:

```text
50000
60000
NULL
```

then:

```sql
AVG(salary)
```

averages the two numeric values rather than treating NULL as zero.

If you intentionally want a different interpretation, use an expression such as:

```sql
AVG(COALESCE(salary, 0))
```

But do not use `COALESCE` automatically. Replacing missing data with zero changes the meaning of the calculation.

## 7. Aggregates with WHERE

```sql
SELECT AVG(price)
FROM products
WHERE price > 1000;
```

The filter is applied before aggregation.

Conceptually:

```text
All rows
  ↓
WHERE
  ↓
Remaining rows
  ↓
AVG
  ↓
One result
```

## 8. DISTINCT Inside Aggregates

```sql
SELECT COUNT(DISTINCT c_id)
FROM orders;
```

This counts distinct customers who placed orders.

Compare:

```sql
COUNT(c_id)
```

with:

```sql
COUNT(DISTINCT c_id)
```

The first counts qualifying non-null values; the second counts unique qualifying values.

## 9. Aggregate Expressions

Aggregates can operate on calculated expressions:

```sql
SELECT SUM(quantity * price)
FROM order_items;
```

This pattern is extremely common in business systems.

For an e-commerce system:

```text
quantity × unit price
        ↓
line-item value
        ↓
SUM
        ↓
revenue
```

## 10. Combining Multiple Aggregates

```sql
SELECT
    COUNT(*) AS total_products,
    AVG(price) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products;
```

This produces one summary row.

## 11. Aggregates vs Window Functions

An aggregate normally reduces rows:

```text
10 rows
   ↓
SUM
   ↓
1 row
```

A window function can calculate a summary while keeping individual rows:

```text
10 rows
   ↓
window calculation
   ↓
10 rows + summary information
```

This distinction becomes important later in the window-functions section.

## 12. Engineering Applications

Aggregates power metrics such as:

- Total revenue
- Average order value
- Number of active users
- Maximum response time
- Total inventory
- Number of orders
- Average salary

For example:

```sql
SELECT
    COUNT(*) AS total_orders,
    SUM(order_total) AS revenue,
    AVG(order_total) AS average_order_value
FROM orders;
```

## Common Mistakes

- Confusing `COUNT(*)` with `COUNT(column)`.
- Forgetting that null inputs are generally ignored.
- Treating NULL as zero without considering the business meaning.
- Aggregating the wrong expression.
- Forgetting `DISTINCT` when uniqueness is required.

## Engineering Takeaways

You should be able to choose the correct aggregate, understand null behavior, combine aggregates with filtering, aggregate expressions, and distinguish reduction from row-preserving analytics.

## Practice

The exercises are in `practice.sql`.

## Next Topic

**GROUP BY and HAVING** — producing separate aggregate summaries for groups rather than one summary for the entire result set.