# PostgreSQL CLI

The PostgreSQL command-line interface, **psql**, is the fastest way to interact directly with a PostgreSQL server during development, debugging, administration, and learning.

This section focuses on the distinction between SQL statements and psql's own commands.

## 1. What Is psql?

`psql` is PostgreSQL's interactive terminal client.

The flow is:

```text
Terminal
   ↓
psql
   ↓
PostgreSQL server
   ↓
Database
```

When you run:

```bash
psql -U postgres
```

you start the client and attempt to connect as the PostgreSQL user `postgres`.

## 2. Connecting to a Database

A common connection command is:

```bash
psql -U postgres -d mydb
```

Useful connection parameters include:

```text
-U -> database user
-d -> database
-h -> host
-p -> port
```

For example:

```bash
psql -U app_user -d shop_db -h localhost -p 5432
```

The default PostgreSQL port is commonly `5432`.

## 3. SQL vs psql Commands

This distinction is essential.

SQL is sent to PostgreSQL:

```sql
SELECT *
FROM customers;
```

psql meta-commands are interpreted by the client itself and begin with a backslash:

```text
\dt
\d customers
\l
\c shop_db
```

So:

```text
SELECT ... -> SQL
\dt       -> psql command
```

Do not put a semicolon after ordinary psql meta-commands.

## 4. Essential psql Commands

### List databases

```text
\l
```

### Connect to another database

```text
\c database_name
```

### List tables

```text
\dt
```

### Describe a table

```text
\d customers
```

This shows columns, types, indexes, and related information.

### List schemas

```text
\dn
```

### List views

```text
\dv
```

### List functions

```text
\df
```

### Show the current connection

```text
\conninfo
```

### Get help

```text
\?
```

SQL command help:

```text
\h SELECT
```

## 5. Running SQL

SQL statements normally end with a semicolon:

```sql
SELECT *
FROM products;
```

You can run multiple statements:

```sql
SELECT COUNT(*) FROM customers;

SELECT COUNT(*) FROM orders;
```

The semicolon tells psql that the statement is complete.

## 6. Useful Query Workflow

A practical debugging workflow is:

```text
Connect
  ↓
\conninfo
  ↓
\dt
  ↓
\d table_name
  ↓
SELECT ...
  ↓
Inspect result
  ↓
Modify / test
```

For example:

```text
\dt
\d orders

SELECT *
FROM orders
LIMIT 10;
```

This is often faster than repeatedly inspecting database structure through a GUI.

## 7. Running SQL Files

A SQL file can be executed with:

```bash
psql -U postgres -d shop_db -f schema.sql
```

Inside psql, you can also use:

```text
\i schema.sql
```

This is useful for reproducible database setup.

## 8. Output and Inspection

For wide results, expanded output is useful:

```text
\x
```

You can toggle it again with `\x`.

Timing can be enabled with:

```text
\timing
```

This displays query execution time after queries run.

Timing is useful for experimentation, although serious performance analysis requires tools such as `EXPLAIN` and `EXPLAIN ANALYZE`.

## 9. Shell Commands

psql can execute shell commands with:

```text
\! command
```

For example:

```text
\! pwd
```

This is a client feature, not SQL.

## 10. Why CLI Skills Matter

GUI tools are convenient, but production engineering frequently involves:

- SSH sessions
- Containers
- Remote servers
- CI/CD environments
- Minimal Linux machines
- Debugging without a graphical interface

Knowing `psql` means PostgreSQL remains usable in those environments.

## Common Mistakes

- Confusing psql commands with SQL.
- Forgetting that psql commands begin with `\`.
- Adding a semicolon to a meta-command.
- Connecting to the wrong database.
- Assuming a table exists because it exists in another database.
- Running destructive SQL without checking the current connection.

## Safety Habit

Before destructive or production-sensitive commands, verify:

```text
\conninfo
\dt
```

Then inspect the target data before modifying it.

## Engineering Takeaways

You should be able to connect to PostgreSQL, switch databases, inspect schemas and tables, execute SQL files, understand psql meta-commands, and troubleshoot a database without depending on a GUI.

## Practice

The command reference is in `commands.md`; SQL exercises are in `practice.sql`.

## Next Topic

**Database and Table Creation** — translating a data model into PostgreSQL database objects.