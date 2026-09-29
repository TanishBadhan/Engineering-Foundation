# Views

A view is a named query that behaves like a virtual table. Views are useful for reusing query logic, simplifying access to complex joins, and exposing a controlled database interface.

## 1. Creating a View

Example:

```sql
CREATE VIEW customer_order_summary AS
SELECT
    c.c_id,
    c.c_name,
    COUNT(o.o_id) AS order_count
FROM customers c
LEFT JOIN orders o
    ON o.c_id = c.c_id
GROUP BY c.c_id, c.c_name;
```

Now:

```sql
SELECT *
FROM customer_order_summary;
```

The view provides a reusable name for the query.

## 2. View vs Table

A normal view stores the query definition, not an independent copy of the query result.

Conceptually:

```text
View
 ↓
query definition
 ↓
underlying tables
 ↓
current result
```

A table stores its own rows.

Therefore, a view is usually not a replacement for a table.

## 3. Why Use Views?

Views can provide:

- Reusable query logic
- Simpler application queries
- Abstraction over complex joins
- Controlled exposure of columns
- A stable logical interface over underlying tables

For example, an application may query:

```sql
SELECT *
FROM customer_order_summary;
```

instead of repeatedly embedding the same multi-table aggregation.

## 4. Views as an Interface

A useful engineering perspective is:

```text
Base tables
     ↓
Complex SQL
     ↓
View
     ↓
Application / reporting query
```

This can reduce duplication and hide implementation details.

However, the view definition itself becomes part of the database contract.

## 5. CREATE OR REPLACE VIEW

PostgreSQL supports:

```sql
CREATE OR REPLACE VIEW customer_order_summary AS
SELECT ...;
```

This is useful for evolving a view while preserving its identity, subject to PostgreSQL's rules about compatible column structure.

## 6. Dropping a View

```sql
DROP VIEW customer_order_summary;
```

Dependencies should be considered before dropping a view.

## 7. Views and Security

Views can expose only selected columns:

```sql
CREATE VIEW public_customer_data AS
SELECT c_id, c_name
FROM customers;
```

This can help create a narrower interface than granting direct access to every base-table column.

A view alone is not a complete security architecture; permissions and underlying access rules still matter.

## 8. Materialized Views

A materialized view stores the query result physically.

```sql
CREATE MATERIALIZED VIEW daily_sales AS
SELECT ...
```

Unlike an ordinary view, its result does not automatically reflect later changes to the underlying data.

It can be refreshed:

```sql
REFRESH MATERIALIZED VIEW daily_sales;
```

Materialized views are useful when an expensive query is read frequently and slightly stale results are acceptable.

## 9. View vs CTE vs Materialized View

### View

Reusable named query definition.

### CTE

Query-scoped named subquery used within one statement.

### Materialized View

Persisted query result that must be refreshed.

Mental model:

```text
CTE              -> temporary within one statement
View              -> reusable query definition
Materialized view -> stored query result
Table             -> stored data
```

## Common Mistakes

- Assuming an ordinary view stores a cached result.
- Treating a view as automatically faster.
- Forgetting that changing a view can affect application queries.
- Using materialized views without a refresh strategy.
- Assuming a view alone provides complete security.

## Engineering Takeaways

You should understand views as reusable database interfaces and be able to distinguish them from tables, CTEs, and materialized views.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**CTEs** — structuring complex queries using named subqueries.