# Database and Table Creation

Creating tables is where a logical data model becomes an actual PostgreSQL schema. Good table definitions make later querying, validation, and application development much easier.

## 1. Creating a Database

A database can be created with:

```sql
CREATE DATABASE shop_db;
```

Then connect to it:

```text
\c shop_db
```

A database is a container for schemas and database objects. Tables belong to schemas inside a database.

## 2. Creating a Table

Basic form:

```sql
CREATE TABLE customers (
    c_id SERIAL PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL,
    c_mail VARCHAR(100) UNIQUE NOT NULL
);
```

Each column has a name and a data type, optionally followed by constraints.

The mental model is:

```text
column name
    +
data type
    +
constraints
    =
column definition
```

## 3. Choosing Columns

Before writing SQL, identify the attributes required by the entity.

For a customer:

```text
Customer
├── id
├── name
└── email
```

Then translate them:

```sql
CREATE TABLE customers (
    c_id SERIAL PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL,
    c_mail VARCHAR(100) UNIQUE NOT NULL
);
```

The database design should come before syntax.

## 4. Primary Keys

A primary key gives every row a unique identity.

```sql
c_id SERIAL PRIMARY KEY
```

For PostgreSQL, newer designs may also use identity columns:

```sql
c_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
```

Identity columns are PostgreSQL's standards-oriented mechanism for generated numeric values. `SERIAL` remains common legacy PostgreSQL syntax and is useful to recognize.

## 5. Data Types

A column's type determines what kind of values PostgreSQL accepts.

Examples:

```sql
name VARCHAR(100),
age INT,
price NUMERIC(10,2),
created_at TIMESTAMP,
active BOOLEAN
```

Choose types according to the semantics of the data, not merely what happens to work for today's sample values.

For example, monetary values generally should not be modeled using floating-point types when exact decimal arithmetic is required.

## 6. Constraints During Table Creation

Constraints can be attached directly to columns:

```sql
email VARCHAR(100) UNIQUE NOT NULL
```

or defined at table level:

```sql
CONSTRAINT positive_price CHECK (price >= 0)
```

Table-level constraints become especially useful for multi-column rules.

Example:

```sql
CREATE TABLE memberships (
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    CHECK (end_date >= start_date)
);
```

## 7. Relationships During Creation

Tables can reference one another:

```sql
CREATE TABLE orders (
    o_id SERIAL PRIMARY KEY,
    c_id INT NOT NULL,
    o_date DATE NOT NULL,
    FOREIGN KEY (c_id)
        REFERENCES customers(c_id)
);
```

The referenced table normally needs to exist before the foreign key can be created this way.

This creates:

```text
customers.c_id
      ↑
      |
orders.c_id
```

## 8. Naming

Consistent names reduce cognitive overhead.

Good database naming should make it obvious:

- What an object represents
- Which table a column belongs to
- Which columns are identifiers
- Which columns are relationships

For this repository, the existing schema uses names such as `c_id`, `o_id`, and `p_id`. In a real project, choose a convention and apply it consistently.

## 9. CREATE TABLE IF NOT EXISTS

Useful during repeatable development setup:

```sql
CREATE TABLE IF NOT EXISTS customers (
    c_id SERIAL PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL
);
```

This avoids an error when the table already exists.

However, it should not be treated as a replacement for proper migrations. Production schema changes need controlled migration processes.

## 10. Temporary Tables

PostgreSQL also supports temporary tables:

```sql
CREATE TEMP TABLE recent_orders AS
SELECT *
FROM orders
WHERE o_date >= CURRENT_DATE - INTERVAL '7 days';
```

Temporary tables are session-oriented and are useful for intermediate processing.

## 11. Design Example

Suppose an application needs customers and orders.

Start with entities:

```text
Customer
Order
```

Identify attributes:

```text
Customer -> id, name, email
Order    -> id, customer_id, date
```

Identify relationship:

```text
Customer 1 -> N Orders
```

Then implement:

```sql
CREATE TABLE customers (...);

CREATE TABLE orders (
    ...,
    customer_id INT REFERENCES customers(c_id)
);
```

This is the correct direction of reasoning: model first, SQL second.

## Common Mistakes

- Using a vague data type simply because it accepts the sample data.
- Forgetting primary keys.
- Creating relationships without foreign keys.
- Allowing required fields to remain nullable.
- Creating child tables before referenced tables.
- Treating `IF NOT EXISTS` as a migration system.

## Engineering Takeaways

You should be able to translate an entity model into tables, choose appropriate column types, define primary keys and constraints, create relationships, and recognize the difference between development setup and production schema migrations.

## Practice

The corresponding SQL exercises are in `practice.sql`.

## Next Topic

**Data Types** — choosing PostgreSQL types based on the meaning, precision, range, and behavior of the data.