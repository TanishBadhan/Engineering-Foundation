# SQL Command Categories

SQL is easier to reason about when commands are grouped by their purpose. The categories describe what a statement does to the database rather than how complicated its syntax looks.

## 1. DDL — Data Definition Language

DDL changes database structure.

Common statements:

- `CREATE`
- `ALTER`
- `DROP`
- `TRUNCATE`

Example:

```sql
CREATE TABLE products (
    p_id SERIAL PRIMARY KEY,
    p_name VARCHAR(100),
    price NUMERIC(10,2)
);
```

This defines a table. It is not inserting a product; it is defining the structure that products will use.

`ALTER TABLE` changes an existing definition:

```sql
ALTER TABLE products
ADD COLUMN stock INT DEFAULT 0;
```

## 2. DML — Data Manipulation Language

DML changes the rows stored inside tables.

Core commands:

- `INSERT`
- `UPDATE`
- `DELETE`

Example:

```sql
INSERT INTO products (p_name, price)
VALUES ('Keyboard', 800);
```

Update:

```sql
UPDATE products
SET price = 850
WHERE p_id = 3;
```

Delete:

```sql
DELETE FROM products
WHERE p_id = 3;
```

The key distinction is:

```text
DDL -> structure
DML -> stored rows
```

## 3. DQL — Data Query Language

DQL is commonly used to describe querying data with `SELECT`.

```sql
SELECT p_name, price
FROM products
WHERE price > 1000;
```

A `SELECT` normally reads data rather than changing stored rows.

It can become much more powerful through:

- Filtering
- Joins
- Aggregation
- Subqueries
- CTEs
- Window functions
- Ordering
- Grouping

## 4. DCL — Data Control Language

DCL controls permissions.

Common statements include:

```sql
GRANT
REVOKE
```

Example:

```sql
GRANT SELECT ON products TO analyst;
```

This is part of database security rather than ordinary application querying.

## 5. TCL — Transaction Control Language

TCL controls transactions.

Important statements:

- `BEGIN`
- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`

Example:

```sql
BEGIN;

UPDATE products
SET stock = stock - 1
WHERE p_id = 1;

COMMIT;
```

If something goes wrong before the commit:

```sql
ROLLBACK;
```

Transactions become critical when multiple changes must be treated as one logical operation.

## 6. A Practical Classification

Consider an order system.

Creating the table:

```sql
CREATE TABLE orders (...);
```

is DDL.

Creating an order:

```sql
INSERT INTO orders (...);
```

is DML.

Reading an order:

```sql
SELECT *
FROM orders
WHERE o_id = 10;
```

is DQL.

Protecting a group of changes:

```sql
BEGIN;
...
COMMIT;
```

is TCL.

Giving another database user permission:

```sql
GRANT SELECT ON orders TO analyst;
```

is DCL.

## 7. Why the Categories Matter

The categories provide a mental map.

When a database task is given to you, ask:

```text
Am I changing structure?
        -> DDL

Am I changing rows?
        -> DML

Am I reading data?
        -> DQL

Am I controlling permissions?
        -> DCL

Am I controlling transaction boundaries?
        -> TCL
```

This prevents command memorization from becoming disconnected from database behavior.

## 8. Important PostgreSQL Nuance

SQL terminology is sometimes presented differently across courses and database products. For example, some references classify `SELECT` under DML rather than using a separate DQL category.

For this repository, DQL is used as a convenient learning classification for queries.

The important thing is understanding the operation, not arguing over the label.

## Common Mistakes

- Confusing `ALTER TABLE` with `UPDATE`.
- Thinking `SELECT` changes data.
- Treating `DELETE` as a schema operation.
- Using `COMMIT` without understanding transaction boundaries.
- Memorizing category names without understanding what the commands actually do.

## Engineering Mental Model

Think of SQL as an interface to several classes of database operations:

```text
Schema        -> DDL
Rows          -> DML
Queries       -> DQL
Permissions   -> DCL
Transactions  -> TCL
```

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**PostgreSQL CLI** — using `psql` to connect to PostgreSQL and interact with it efficiently from the terminal.