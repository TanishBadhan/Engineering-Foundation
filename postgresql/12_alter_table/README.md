# ALTER TABLE

Real databases evolve. Columns are added, constraints change, names are corrected, and schemas are extended as applications grow. PostgreSQL uses `ALTER TABLE` for many of these structural changes.

## 1. Adding a Column

```sql
ALTER TABLE customers
ADD COLUMN phone TEXT;
```

Existing rows initially receive `NULL` unless a default or other rule applies.

## 2. Adding a Column with a Default

```sql
ALTER TABLE customers
ADD COLUMN active BOOLEAN DEFAULT TRUE;
```

A default controls future inserts and, depending on the PostgreSQL operation/version and expression, the existing table's physical treatment can differ. Schema changes should therefore be evaluated for production impact rather than assumed to be free.

## 3. Renaming a Column

```sql
ALTER TABLE customers
RENAME COLUMN c_name TO customer_name;
```

Renaming can affect application queries, views, functions, reports, and migrations. A schema change is therefore an API change for database consumers.

## 4. Renaming a Table

```sql
ALTER TABLE customers
RENAME TO users;
```

All dependent application code must be considered.

## 5. Changing a Data Type

```sql
ALTER TABLE products
ALTER COLUMN price TYPE NUMERIC(12,2);
```

Some conversions are straightforward; others require an explicit `USING` expression.

Example:

```sql
ALTER TABLE products
ALTER COLUMN price TYPE NUMERIC
USING price::NUMERIC;
```

Always check whether existing data can be converted.

## 6. Adding and Dropping Constraints

Add:

```sql
ALTER TABLE products
ADD CONSTRAINT positive_price
CHECK (price >= 0);
```

Drop:

```sql
ALTER TABLE products
DROP CONSTRAINT positive_price;
```

Constraints should be changed deliberately because they alter which database states are legal.

## 7. Adding a Foreign Key

```sql
ALTER TABLE orders
ADD CONSTRAINT orders_customer_fk
FOREIGN KEY (c_id)
REFERENCES customers(c_id);
```

Before adding the constraint, existing data must satisfy the relationship or the operation can fail.

## 8. Dropping a Column

```sql
ALTER TABLE customers
DROP COLUMN phone;
```

Dropping a column is destructive. Verify dependencies and data requirements first.

PostgreSQL also supports `CASCADE` for some dependency-related operations:

```sql
ALTER TABLE customers
DROP COLUMN phone CASCADE;
```

Use this only when the dependency removal is explicitly understood.

## 9. Schema Evolution in Production

A production migration should be treated as a deployment problem:

```text
New application code
        +
Database migration
        +
Existing data
        +
Existing application instances
```

A dangerous migration may lock a large table, rewrite data, invalidate dependencies, or make old application instances incompatible.

For this reason, production migrations often use staged changes:

```text
Add new structure
      ↓
Backfill / migrate data
      ↓
Deploy code using it
      ↓
Remove old structure later
```

## 10. ALTER TABLE vs UPDATE

This distinction is fundamental.

```sql
ALTER TABLE ...
```

changes the schema.

```sql
UPDATE ...
```

changes stored rows.

Mental model:

```text
ALTER TABLE -> shape of data
UPDATE      -> contents of data
```

## Common Mistakes

- Treating schema changes as harmless local edits.
- Dropping columns without checking dependencies.
- Changing types without testing existing data.
- Adding constraints before cleaning incompatible data.
- Using `CASCADE` without inspecting what will be removed.
- Forgetting that application code depends on schema names and types.

## Engineering Takeaways

You should understand how PostgreSQL schemas evolve and why database migrations must consider existing data, dependencies, locking, compatibility, and deployment order.

## Practice

The corresponding examples are in `practice.sql`.

## Next Topic

**Relationships and Foreign Keys** — modeling connections between entities and enforcing referential integrity.