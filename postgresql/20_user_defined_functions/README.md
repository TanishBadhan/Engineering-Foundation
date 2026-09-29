# User-Defined Functions

PostgreSQL functions encapsulate reusable logic inside the database. Unlike procedures, functions are designed to return a value or result and can be used in SQL expressions when their definition permits it.

## 1. Basic Function

Example:

```sql
CREATE OR REPLACE FUNCTION add_numbers(
    a INT,
    b INT
)
RETURNS INT
LANGUAGE SQL
AS $$
    SELECT a + b;
$$;
```

Call it:

```sql
SELECT add_numbers(10, 20);
```

Result:

```text
30
```

## 2. RETURNS

A function declares what it returns.

Examples:

```sql
RETURNS INT
RETURNS TEXT
RETURNS BOOLEAN
RETURNS TABLE (...)
```

The return type is part of the function contract.

## 3. SQL vs PL/pgSQL

Simple functions can use SQL:

```sql
LANGUAGE SQL
```

More procedural logic can use:

```sql
LANGUAGE plpgsql
```

PL/pgSQL supports variables, conditionals, loops, exception handling, and multiple statements.

## 4. Parameters

Parameters have names and types:

```sql
p_dept department
p_salary NUMERIC
```

Naming conventions such as `p_` can make parameter references easier to distinguish from column names.

## 5. Function with Conditional Logic

```sql
CREATE OR REPLACE FUNCTION salary_band(
    p_salary NUMERIC
)
RETURNS TEXT
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_salary >= 100000 THEN
        RETURN 'high';
    ELSIF p_salary >= 50000 THEN
        RETURN 'medium';
    ELSE
        RETURN 'low';
    END IF;
END;
$$;
```

The function can then be used in a query:

```sql
SELECT fname, salary_band(salary)
FROM employees;
```

## 6. Set-Returning Functions

Functions can return multiple rows.

A table-returning function might define:

```sql
RETURNS TABLE (
    emp_id INT,
    fname TEXT
)
```

Such functions can participate in SQL queries and can be useful when a reusable database-side result has a clear contract.

## 7. Dollar Quoting

PL/pgSQL bodies commonly use:

```sql
$$
...
$$
```

This is dollar quoting. It is a delimiter for the function body and is not a permanent replacement for SQL syntax.

Tagged dollar quotes are also possible:

```sql
$func$
...
$func$
```

## 8. Function Volatility

PostgreSQL classifies functions according to how their results behave:

- IMMUTABLE
- STABLE
- VOLATILE

The classification communicates whether a function can depend on changing database state or external effects.

Do not mark a function `IMMUTABLE` merely because it "usually returns the same thing." The declaration must match the function's actual behavior.

## 9. Function vs Procedure

A useful distinction:

```text
Function
  -> returns a value/result
  -> can be used in SQL expressions when appropriate

Procedure
  -> called with CALL
  -> designed for procedural operations
```

A procedure does not use `RETURNS` in its declaration.

## 10. When Functions Make Sense

Database functions are useful when:

- Logic is naturally data-local
- Multiple database clients need the same computation
- A reusable SQL interface is valuable
- The logic benefits from running close to the data

They are not automatically better than application code. Business logic placed inside the database can increase coupling and complicate testing/deployment if used indiscriminately.

## Common Mistakes

- Confusing functions with procedures.
- Declaring the wrong return type.
- Marking volatility incorrectly.
- Putting large application workflows into database functions without a clear reason.
- Ignoring the deployment/versioning implications of database-side code.

## Engineering Takeaways

You should be able to create SQL and PL/pgSQL functions, define parameters and return types, use control flow, understand dollar quoting, and decide when database-side logic is appropriate.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**Stored Procedures** — database-side procedural operations invoked explicitly with `CALL`.