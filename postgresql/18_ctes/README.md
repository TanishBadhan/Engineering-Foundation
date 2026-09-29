# Common Table Expressions (CTEs)

A Common Table Expression, or CTE, gives a temporary name to a query result within a single SQL statement. CTEs are primarily a tool for structuring complex queries.

## 1. Basic CTE

```sql
WITH expensive_products AS (
    SELECT *
    FROM products
    WHERE price > 10000
)
SELECT *
FROM expensive_products;
```

The CTE exists only for this statement.

It does not create a permanent table or view.

## 2. Why CTEs Help

A long query can become difficult to reason about when every operation is nested inside another subquery.

CTEs allow a pipeline:

```text
raw data
   ↓
CTE 1
   ↓
CTE 2
   ↓
final query
```

Each stage can represent a meaningful transformation.

## 3. Multiple CTEs

```sql
WITH customer_totals AS (
    SELECT
        c_id,
        SUM(total) AS spent
    FROM orders
    GROUP BY c_id
),
high_value AS (
    SELECT *
    FROM customer_totals
    WHERE spent > 50000
)
SELECT *
FROM high_value;
```

The second CTE can reference the first.

## 4. CTE Scope

A CTE is available only to the statement immediately following its `WITH`.

```text
WITH ...
SELECT ...;
```

It cannot be queried later like a permanent table.

If reusable across separate statements, consider a view or table depending on the requirement.

## 5. CTEs vs Subqueries

A subquery:

```sql
SELECT *
FROM (
    SELECT *
    FROM products
) p;
```

can often be rewritten as:

```sql
WITH p AS (
    SELECT *
    FROM products
)
SELECT *
FROM p;
```

The advantage of the CTE is usually readability and the ability to give meaningful names to stages of the query.

It is not automatically faster.

## 6. Recursive CTEs

PostgreSQL supports recursive CTEs.

They are useful for hierarchical data such as:

```text
CEO
 ├── Engineering Manager
 │     ├── Developer
 │     └── Developer
 └── Sales Manager
       └── Salesperson
```

A recursive CTE has an anchor query and a recursive query connected with `UNION ALL`.

Conceptually:

```text
anchor rows
   ↓
recursive expansion
   ↓
more rows
   ↓
repeat until no new rows
```

## 7. Data-Modifying CTEs

PostgreSQL also allows data-modifying statements in CTEs in appropriate forms.

This can be useful when a statement needs to coordinate multiple related operations.

Because this can become complex quickly, transaction semantics and the statement's exact behavior should be understood rather than treating CTEs as a general-purpose scripting language.

## 8. CTE Performance

A common misconception is:

> CTEs are always slower.

That is not a reliable rule.

Modern PostgreSQL can inline some CTEs when appropriate, while materialization can also occur under certain conditions or be requested explicitly.

The correct approach is:

```text
Write clear SQL
   ↓
Measure
   ↓
EXPLAIN / EXPLAIN ANALYZE
   ↓
Optimize if needed
```

Do not optimize based on folklore.

## 9. Engineering Use Cases

CTEs are especially useful for:

- Multi-stage analytics
- Data transformations
- Complex reporting
- Hierarchical queries
- Breaking large queries into named logical steps

## Common Mistakes

- Thinking a CTE is a permanent object.
- Assuming CTEs are automatically faster.
- Creating unnecessarily many layers that obscure the query.
- Forgetting the query's final result grain.
- Using recursive CTEs without a clear termination condition.

## Engineering Mental Model

Treat a CTE as a named intermediate result in a query pipeline:

```text
WITH stage_1 AS (...)
   ↓
stage_1
   ↓
WITH stage_2 AS (...)
   ↓
stage_2
   ↓
final SELECT
```

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**Window Functions** — performing calculations across related rows without collapsing them into one row per group.