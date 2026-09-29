# PostgreSQL Data Types

A PostgreSQL data type is not merely a storage label. It defines which values are valid, how PostgreSQL stores and compares them, and which operations can be performed efficiently and correctly.

Choosing types deliberately is a core database-engineering skill.

## 1. Numeric Types

### Integer Types

Common integer types include:

- `SMALLINT`
- `INTEGER` / `INT`
- `BIGINT`

Use them when values are whole numbers.

```sql
age INT,
quantity INT,
employee_id BIGINT
```

Choose based on expected range rather than habit.

### NUMERIC / DECIMAL

Use exact decimal arithmetic when precision matters.

```sql
price NUMERIC(10,2)
```

This can represent values with up to 10 total digits and 2 digits after the decimal point.

For financial or monetary calculations, exact numeric representation is generally preferable to floating-point arithmetic.

### REAL and DOUBLE PRECISION

These are floating-point types.

They are appropriate for measurements and scientific-style values where approximate representation is acceptable.

They should not automatically be chosen for values where exact decimal arithmetic is required.

## 2. Character Types

### TEXT

```sql
description TEXT
```

PostgreSQL's `TEXT` type stores variable-length text.

### VARCHAR(n)

```sql
name VARCHAR(100)
```

It limits the maximum length.

### CHAR(n)

```sql
code CHAR(5)
```

This is fixed-length character storage and has different padding behavior.

For ordinary variable-length text in PostgreSQL, `TEXT` and unconstrained `VARCHAR` are often simpler choices. Use a length constraint when the length itself is a meaningful business rule.

## 3. Boolean

Boolean values are:

```sql
TRUE
FALSE
NULL
```

Example:

```sql
active BOOLEAN NOT NULL DEFAULT TRUE
```

Remember that `NULL` introduces a third state: the value is absent/unknown.

## 4. Date and Time

Important temporal types include:

- `DATE`
- `TIME`
- `TIMESTAMP`
- `TIMESTAMPTZ`
- `INTERVAL`

Example:

```sql
birth_date DATE,
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
```

### DATE

Stores a calendar date without a time.

### TIMESTAMP

Stores date and time without time-zone semantics.

### TIMESTAMPTZ

PostgreSQL's timestamp-with-time-zone type stores an instant in time and displays it according to the session time zone.

For distributed applications, timestamps representing real-world instants are commonly modeled with `timestamptz`.

### INTERVAL

Represents a duration:

```sql
CURRENT_TIMESTAMP - INTERVAL '7 days'
```

## 5. UUID

UUIDs provide large, globally unique identifiers.

```sql
id UUID PRIMARY KEY
```

They can be useful when identifiers must be generated across multiple services or systems without relying on a single centralized sequence.

However, UUIDs are not automatically superior to integer IDs. Their size, index behavior, generation strategy, and operational requirements should be considered.

## 6. ENUM

PostgreSQL supports enumerated types.

```sql
CREATE TYPE department AS ENUM (
    'engineering',
    'sales',
    'hr',
    'finance',
    'marketing'
);
```

Then:

```sql
dept department
```

Enums are useful when the allowed set is small and relatively stable.

They are less convenient when values change frequently or need additional metadata. In those cases, a lookup table can be more flexible.

## 7. Arrays

PostgreSQL supports arrays:

```sql
tags TEXT[]
```

Example value:

```text
{'backend','postgresql','api'}
```

Arrays are useful for naturally multi-valued attributes, but they should not be used automatically to avoid proper relational modeling.

If each tag needs independent querying, metadata, relationships, or lifecycle management, a separate table may be more appropriate.

## 8. JSON and JSONB

PostgreSQL supports `JSON` and `JSONB`.

Example:

```sql
metadata JSONB
```

`JSONB` stores JSON in a binary representation optimized for processing and indexing.

It is useful for semi-structured attributes where a rigid relational schema would be unnecessarily restrictive.

Example:

```json
{
  "theme": "dark",
  "notifications": true
}
```

But putting an entire relational model into JSON usually sacrifices useful constraints and relational querying. Use JSONB because the data is genuinely semi-structured, not because SQL tables seem inconvenient.

## 9. Network and Specialized Types

PostgreSQL provides specialized types such as:

- `INET` for IP addresses
- `CIDR` for network addresses
- `MACADDR` for MAC addresses
- `RANGE` types for ranges

Example:

```sql
ip_address INET
```

Using a native type can provide better validation and operators than storing the same information as arbitrary text.

## 10. Type Choice Mental Model

Choose a type by asking:

```text
What does this value mean?
        ↓
What values are valid?
        ↓
What range / precision is required?
        ↓
How will it be queried?
        ↓
Does PostgreSQL have a native type?
        ↓
Do constraints belong on the column?
```

Examples:

```text
Age          -> INT
Price        -> NUMERIC
Name         -> TEXT / VARCHAR
Active       -> BOOLEAN
Birthday     -> DATE
Event instant-> TIMESTAMPTZ
Identifier   -> INT / BIGINT / UUID
IP address   -> INET
Flexible data-> JSONB
```

## Common Mistakes

- Using floating point for exact monetary values.
- Storing dates as text.
- Storing Boolean states as strings such as `"yes"`.
- Using JSONB for data that should have relational structure.
- Choosing an unnecessarily small numeric type.
- Assuming `VARCHAR(255)` is universally the correct text type.

## Engineering Takeaways

A strong schema uses types to encode meaning and valid states. Good types reduce invalid data, simplify queries, and make the database easier for application code to reason about.

## Practice

The corresponding examples and exercises are in `practice.sql`.

## Next Topic

**Constraints** — using PostgreSQL to enforce data-integrity rules at the database boundary.