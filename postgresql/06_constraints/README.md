# Constraints

Constraints are database-enforced rules that define which states of the data are valid. They are one of the most important mechanisms for protecting data integrity.

## 1. Why Constraints Exist

Suppose an application accepts:

```text
email = duplicate@example.com
price = -500
customer_id = 999999
```

Application code can validate these values, but the database is the final shared boundary for persisted data.

Constraints allow PostgreSQL to reject invalid states regardless of which application, script, migration, or user attempts the write.

## 2. PRIMARY KEY

A primary key uniquely identifies each row.

```sql
CREATE TABLE customers (
    c_id SERIAL PRIMARY KEY,
    c_name TEXT NOT NULL
);
```

A primary key provides:

- Uniqueness
- Non-nullability
- A stable row identity
- A target that other tables can reference

A table has one primary-key constraint, although that constraint can contain multiple columns.

### Composite Primary Key

```sql
CREATE TABLE order_items (
    o_id INT,
    p_id INT,
    quantity INT,
    PRIMARY KEY (o_id, p_id)
);
```

Here neither column needs to be globally unique by itself. The pair must be unique.

## 3. NOT NULL

`NOT NULL` requires a value.

```sql
email TEXT NOT NULL
```

This is appropriate when the absence of a value is invalid.

It is different from `CHECK` because PostgreSQL handles nullability as a specific column property.

## 4. UNIQUE

`UNIQUE` prevents duplicate non-null values according to the constraint's semantics.

```sql
email TEXT UNIQUE
```

If an email must both exist and be unique:

```sql
email TEXT UNIQUE NOT NULL
```

A unique constraint can also span multiple columns:

```sql
UNIQUE (user_id, provider)
```

This is useful when the combination must be unique even though each individual value may repeat.

## 5. FOREIGN KEY

Foreign keys maintain referential integrity.

```sql
FOREIGN KEY (c_id)
REFERENCES customers(c_id)
```

If `orders.c_id` references `customers.c_id`, PostgreSQL prevents an order from referring to a non-existent customer under the normal foreign-key rules.

Conceptually:

```text
Parent
customers.c_id
      ↑
      |
Child
orders.c_id
```

Foreign keys also define behavior when referenced rows are updated or deleted.

Common actions include:

- `RESTRICT`
- `NO ACTION`
- `CASCADE`
- `SET NULL`
- `SET DEFAULT`

Use cascading actions deliberately. A cascade can remove or modify many dependent rows.

## 6. CHECK

A `CHECK` constraint enforces a Boolean condition.

```sql
price NUMERIC(10,2)
CHECK (price >= 0)
```

Another example:

```sql
CHECK (end_date >= start_date)
```

Checks are useful for rules that depend on values within a row.

## 7. DEFAULT

A default supplies a value when the column is omitted from an insert.

```sql
active BOOLEAN DEFAULT TRUE
```

For example:

```sql
INSERT INTO users (name)
VALUES ('Tanish');
```

If `active` has the default above, PostgreSQL fills it automatically.

A default is not the same as `NOT NULL`. A default provides a value; `NOT NULL` rejects missing values.

## 8. Column vs Table Constraints

Column-level:

```sql
email TEXT UNIQUE NOT NULL
```

Table-level:

```sql
CONSTRAINT valid_dates
CHECK (end_date >= start_date)
```

Table-level constraints are especially useful for multi-column rules and named constraints.

## 9. Named Constraints

Naming constraints improves debugging and migration work.

```sql
CONSTRAINT positive_price
CHECK (price >= 0)
```

When PostgreSQL rejects a row, a meaningful constraint name makes the cause easier to understand.

## 10. Constraints and Application Architecture

A robust system usually validates at multiple layers:

```text
Client validation
      ↓
API validation
      ↓
Business logic
      ↓
Database constraints
```

These layers have different purposes.

Application validation provides fast, user-friendly errors. Database constraints protect the persistent state even when data arrives through another path.

## Common Mistakes

- Using `UNIQUE` without considering null semantics.
- Forgetting foreign keys and relying only on application logic.
- Adding `CASCADE` without understanding its deletion effects.
- Confusing `DEFAULT` with `NOT NULL`.
- Putting every rule into application code.
- Using a `CHECK` constraint for rules that require other rows or complex cross-table logic.

## Engineering Mental Model

Think of constraints as invariants:

```text
Valid database state
       =
state satisfying all declared constraints
```

Every write must preserve those invariants.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**INSERT / UPDATE / DELETE** — changing rows while respecting the schema and its constraints.