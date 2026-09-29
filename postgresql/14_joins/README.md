# JOINs

JOINs combine rows from related tables. They are one of the most important SQL skills for backend engineering because normalized databases intentionally spread related information across tables.

## 1. Why JOINs Exist

Suppose:

```text
customers
c_id | c_name

orders
o_id | c_id | o_date
```

An order stores the customer's ID rather than duplicating the customer's entire record.

A JOIN reconstructs the information needed by a query.

## 2. INNER JOIN

Returns rows where the join condition matches.

```sql
SELECT
    c.c_name,
    o.o_id,
    o.o_date
FROM customers c
JOIN orders o
    ON o.c_id = c.c_id;
```

If a customer has no orders, that customer is not returned.

## 3. LEFT JOIN

Returns every row from the left table and matching rows from the right table.

```sql
SELECT
    c.c_name,
    o.o_id
FROM customers c
LEFT JOIN orders o
    ON o.c_id = c.c_id;
```

Customers with no orders still appear, with null values for order columns.

This is useful for questions such as:

> Show every customer, including customers who have never ordered.

## 4. RIGHT JOIN

A right join preserves rows from the right table.

```sql
SELECT ...
FROM customers c
RIGHT JOIN orders o
    ON o.c_id = c.c_id;
```

It is logically valid, but many engineers rewrite the query as a LEFT JOIN by swapping table order because LEFT JOIN often makes intent easier to read.

## 5. FULL OUTER JOIN

Returns matched rows plus unmatched rows from both sides.

```sql
SELECT ...
FROM customers c
FULL OUTER JOIN orders o
    ON o.c_id = c.c_id;
```

This is useful when comparing two datasets and retaining unmatched records from either side.

## 6. CROSS JOIN

Produces the Cartesian product.

```sql
SELECT *
FROM sizes
CROSS JOIN colors;
```

If there are 3 sizes and 4 colors, the result has 12 combinations.

This is useful for intentionally generating combinations but dangerous when produced accidentally.

## 7. SELF JOIN

A table can be joined to itself.

Example employee hierarchy:

```sql
SELECT
    e.fname AS employee,
    m.fname AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.emp_id;
```

The table is logically playing two roles.

## 8. JOIN Conditions

The `ON` condition determines how rows correspond.

Typical:

```sql
ON orders.c_id = customers.c_id
```

A missing or incorrect condition can create huge numbers of rows.

## 9. JOIN Multiplication

Suppose one customer has 3 orders and each order has 4 items.

Joining customer -> orders -> order_items produces:

```text
1 customer
× 3 orders
× 4 items
=
12 joined rows
```

This is not necessarily wrong. It is the actual result grain.

But aggregations can become incorrect if you forget how many rows the joins create.

This is one of the most important SQL debugging skills.

## 10. JOIN + GROUP BY

Example customer spending:

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

The final grain is one row per customer.

## 11. LEFT JOIN and WHERE Trap

Consider:

```sql
SELECT c.c_name, o.o_id
FROM customers c
LEFT JOIN orders o
    ON o.c_id = c.c_id
WHERE o.o_date >= DATE '2026-01-01';
```

The WHERE condition rejects rows where `o.o_date` is null, effectively removing customers without matching orders.

If the intention is to preserve all customers while restricting matched orders, the condition may belong in the JOIN:

```sql
LEFT JOIN orders o
    ON o.c_id = c.c_id
   AND o.o_date >= DATE '2026-01-01'
```

This distinction is critical.

## 12. JOIN Mental Model

Before writing a JOIN, answer:

```text
What is the left-side grain?
What is the right-side grain?
What key connects them?
Can one row match many rows?
What should happen to unmatched rows?
What will the resulting grain be?
```

If you cannot answer those questions, the query is not yet well-defined.

## Common Mistakes

- Joining on the wrong columns.
- Accidentally creating a Cartesian product.
- Losing unmatched rows with an unintended INNER JOIN.
- Turning a LEFT JOIN into an effective INNER JOIN through WHERE.
- Double-counting after one-to-many joins.
- Not understanding result grain.

## Engineering Takeaways

JOIN mastery means more than memorizing INNER/LEFT/RIGHT/FULL syntax. You should be able to predict which rows survive, how row counts change, and how joins affect downstream aggregation.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**CASE and COALESCE** — expressing conditional logic and controlled fallback values inside SQL.