# INSERT, UPDATE, DELETE

These commands change the rows stored in PostgreSQL tables. They are fundamental DML operations and should be used with deliberate filtering and transaction awareness.

## 1. INSERT

Basic form:

```sql
INSERT INTO customers (c_name, c_mail)
VALUES ('Tanish', 'tanish@example.com');
```

Explicitly naming columns is preferable because it makes the intended mapping clear and protects the statement from changes in column order.

### Multiple Rows

```sql
INSERT INTO products (p_name, price)
VALUES
    ('Mouse', 500),
    ('Keyboard', 800),
    ('Cable', 250);
```

### RETURNING

PostgreSQL can return inserted rows:

```sql
INSERT INTO customers (c_name, c_mail)
VALUES ('Tanish', 'tanish@example.com')
RETURNING c_id;
```

This is especially useful when an application needs the generated identifier immediately.

## 2. UPDATE

Basic form:

```sql
UPDATE products
SET price = 850
WHERE p_id = 3;
```

The `WHERE` clause determines which rows are modified.

Without it:

```sql
UPDATE products
SET price = 850;
```

every row is updated.

That is sometimes intentional, but it should never happen accidentally.

### Updating Multiple Columns

```sql
UPDATE customers
SET
    c_name = 'Tanish Badhan',
    c_mail = 'new@example.com'
WHERE c_id = 1;
```

### RETURNING

```sql
UPDATE products
SET price = price * 1.10
WHERE p_id = 3
RETURNING p_id, price;
```

This lets PostgreSQL return the resulting rows.

## 3. DELETE

Basic form:

```sql
DELETE FROM customers
WHERE c_id = 10;
```

Again, `WHERE` controls the target rows.

Without it:

```sql
DELETE FROM customers;
```

all rows are deleted while the table itself remains.

### RETURNING

```sql
DELETE FROM customers
WHERE c_id = 10
RETURNING *;
```

This can be useful when an application needs information about the deleted record.

## 4. NULL and UPDATE

To set a value to NULL:

```sql
UPDATE customers
SET c_mail = NULL
WHERE c_id = 1;
```

The column must permit null values.

To find null values later:

```sql
SELECT *
FROM customers
WHERE c_mail IS NULL;
```

## 5. UPDATE from Other Data

PostgreSQL supports powerful update patterns using joins and subqueries.

For example, a product price could be updated from another table or derived dataset. This is useful in data-processing jobs but should be tested carefully because a single statement can modify many rows.

## 6. INSERT ... SELECT

Rows can be inserted from a query:

```sql
INSERT INTO archived_orders (o_id, c_id, o_date)
SELECT o_id, c_id, o_date
FROM orders
WHERE o_date < DATE '2025-01-01';
```

This is useful for data movement and transformations.

## 7. UPSERT

PostgreSQL supports conflict handling with `ON CONFLICT`.

Example:

```sql
INSERT INTO customers (c_name, c_mail)
VALUES ('Tanish', 'tanish@example.com')
ON CONFLICT (c_mail)
DO UPDATE
SET c_name = EXCLUDED.c_name;
```

`EXCLUDED` refers to the row that PostgreSQL attempted to insert.

This pattern is commonly called an **upsert**: insert when absent, update when a conflict occurs.

## 8. Transactions

A group of writes can be made atomic:

```sql
BEGIN;

UPDATE products
SET stock = stock - 1
WHERE p_id = 1;

INSERT INTO orders (...);

COMMIT;
```

If the operation fails:

```sql
ROLLBACK;
```

The exact transaction design depends on the application's consistency requirements.

## 9. Safe Update Mental Model

Before modifying data:

```text
1. Identify target rows
2. SELECT them
3. Write the UPDATE/DELETE
4. Verify the WHERE condition
5. Use a transaction for risky multi-step changes
6. Inspect RETURNING output where useful
```

For example, first:

```sql
SELECT *
FROM products
WHERE price < 500;
```

Then, if that is the intended target:

```sql
UPDATE products
SET price = price * 1.10
WHERE price < 500;
```

## Common Mistakes

- Running `UPDATE` or `DELETE` without checking the `WHERE` clause.
- Assuming `DEFAULT` is applied when explicitly inserting `NULL`.
- Forgetting that updates can affect multiple rows.
- Ignoring constraints when writing DML.
- Performing dependent writes without considering transaction boundaries.

## Engineering Takeaways

You should be able to insert individual and multiple rows, update targeted data, delete safely, use `RETURNING`, perform upserts, and reason about writes as part of transactions.

## Practice

The exercises are in `practice.sql`.

## Next Topic

**SELECT and Filtering** — reading exactly the rows and columns needed by an application.