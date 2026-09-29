# Database Fundamentals

Databases are the persistence layer behind most backend systems. This section builds the relational mental model needed to understand PostgreSQL rather than treating SQL as a collection of commands.

## 1. Database, DBMS, and RDBMS

A **database** is organized persistent data. A **DBMS** is software that stores, retrieves, protects, and manages that data. An **RDBMS** is a DBMS based on the relational model.

PostgreSQL is an open-source RDBMS. It stores structured data in tables and provides SQL, transactions, constraints, indexes, concurrency control, and database programming features.

A useful distinction is:

```
Database  -> the stored data
DBMS      -> the software managing it
RDBMS     -> a DBMS using the relational model
```

## 2. The Relational Model

A relational database represents information using relations, commonly exposed as tables.

Example:

```text
customers
+------+----------------+----------------------+
| c_id | c_name         | c_mail               |
+------+----------------+----------------------+
| 1    | Tanish Badhan  | tanish@example.com   |
| 2    | Priya          | priya@example.com    |
+------+----------------+----------------------+
```

A **row** represents one record. A **column** represents an attribute. A table defines the structure that rows must follow.

The important engineering idea is that tables are not isolated spreadsheets. Keys allow them to represent relationships.

```text
customers
    |
    | c_id
    v
orders
```

## 3. Database Structure

PostgreSQL organizes objects roughly as:

```text
PostgreSQL server
  └── Database
       └── Schema
            ├── Tables
            │    ├── Columns
            │    └── Rows
            ├── Views
            ├── Functions
            ├── Procedures
            └── Triggers
```

A database is a logical container. A schema is a namespace inside a database. The default PostgreSQL schema is commonly `public`.

## 4. Primary Keys

A primary key identifies a row uniquely.

```sql
CREATE TABLE customers (
    c_id SERIAL PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL
);
```

The primary key gives the application a stable identity:

```text
c_id = 1 -> one customer
c_id = 2 -> another customer
```

A primary key cannot contain `NULL` and must be unique.

## 5. Foreign Keys and Relationships

A foreign key connects one table to another.

```sql
CREATE TABLE orders (
    o_id SERIAL PRIMARY KEY,
    c_id INT REFERENCES customers(c_id),
    o_date DATE NOT NULL
);
```

Now `orders.c_id` refers to a customer.

A common relationship is one-to-many:

```text
Customer 1
   |
   +---- Order 1
   +---- Order 2
   +---- Order 3
```

Many-to-many relationships are normally represented with an intermediate table.

```text
students <- student_courses -> courses
```

## 6. Constraints and Data Integrity

Constraints make the database enforce business rules.

Common constraints:

- `PRIMARY KEY` — row identity
- `FOREIGN KEY` — referential integrity
- `NOT NULL` — value is required
- `UNIQUE` — duplicate values are disallowed
- `CHECK` — a Boolean condition must hold

Example:

```sql
CREATE TABLE products (
    p_id SERIAL PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) CHECK (price >= 0)
);
```

Database-level constraints matter because application code is not the only path by which data may be written.

## 7. NULL Is Not Zero or an Empty String

`NULL` represents missing or unknown information.

These are different:

```text
NULL   -> no value / unknown
0      -> numeric value zero
''     -> empty text
FALSE  -> Boolean false
```

Use:

```sql
WHERE c_mail IS NULL;
```

not:

```sql
WHERE c_mail = NULL;
```

This becomes important when filtering, joining, aggregating, and using expressions.

## 8. Why Databases Beat Plain Files

CSV or JSON files can work for small scripts, but production applications need capabilities such as:

- Concurrent access
- Transactions
- Constraints
- Efficient querying
- Indexes
- Recovery
- Access control
- Consistent updates

For example, placing an order may require several operations to succeed together:

```text
Create order
   ↓
Create order items
   ↓
Update inventory
   ↓
Commit transaction
```

If a later operation fails, transactions can prevent the system from leaving partially applied state.

## 9. Backend Engineering Connection

A typical backend request follows:

```text
Client
  ↓
HTTP request
  ↓
API
  ↓
Business logic
  ↓
SQL
  ↓
PostgreSQL
  ↓
Result
  ↓
HTTP response
```

Understanding database structure lets you reason about what the backend should query, what relationships exist, and which rules should be enforced by PostgreSQL.

## 10. Mental Model

When given a new application domain, reason in this order:

```text
Entities
  ↓
Tables
  ↓
Attributes
  ↓
Primary keys
  ↓
Relationships / foreign keys
  ↓
Constraints
  ↓
Queries and transactions
```

Do not start with SQL syntax. Start with the data model.

## Common Mistakes

- Treating a database as a collection of unrelated tables.
- Using duplicated data where a relationship should exist.
- Confusing `NULL` with zero or an empty string.
- Relying only on application validation.
- Choosing identifiers without considering uniqueness and stability.

## Engineering Takeaways

You should be able to explain what a relational database is, how tables represent entities, how primary and foreign keys create identity and relationships, why constraints matter, and how PostgreSQL fits into a backend architecture.

## Practice

The exercises are in `practice.sql`. The shared database is created and seeded from `../00_setup/`.

## Next Topic

**SQL Command Categories** — how SQL statements are classified and why those categories matter.