# Stored Procedures

PostgreSQL procedures encapsulate procedural database operations that are invoked with `CALL`. They are related to functions but have a different interface and execution model.

## 1. Basic Procedure

```sql
CREATE OR REPLACE PROCEDURE add_employee(
    p_fname VARCHAR,
    p_lname VARCHAR,
    p_email VARCHAR,
    p_dept department,
    p_salary NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO employees(fname, lname, email, dept, salary)
    VALUES (p_fname, p_lname, p_email, p_dept, p_salary);
END;
$$;
```

Call it:

```sql
CALL add_employee(
    'John',
    'Doe',
    'john@example.com',
    'engineering',
    70000
);
```

## 2. Procedure vs Function

The distinction is important.

### Function

Declared with a return type:

```sql
RETURNS INT
```

Called through an expression:

```sql
SELECT some_function(...);
```

### Procedure

Does not use `RETURNS`.

Called explicitly:

```sql
CALL some_procedure(...);
```

Do not treat `CREATE OR REPLACE PROCEDURE` and `CREATE OR REPLACE FUNCTION` as interchangeable.

## 3. Parameters

Procedure parameters also require a name and type:

```sql
p_dept department
p_salary NUMERIC
```

The type can be a PostgreSQL enum or another database type.

## 4. PL/pgSQL Body

The body is commonly written:

```sql
AS $$
BEGIN
    ...
END;
$$;
```

`$$` is dollar quoting. It marks the boundaries of the procedure body.

It does not permanently change PostgreSQL's statement delimiter.

## 5. Multiple Operations

A procedure can coordinate several database operations.

Conceptually:

```text
CALL procedure
      ↓
validate / transform
      ↓
operation 1
      ↓
operation 2
      ↓
operation 3
```

This can be useful for administrative workflows or database-local operations with a clear boundary.

## 6. Transaction Considerations

Procedures have capabilities that differ from functions around transaction control. PostgreSQL's exact transaction behavior depends on how the procedure is invoked and the statements it contains.

Do not assume that placing `COMMIT` anywhere inside arbitrary database-side code is valid.

For application code, transaction ownership should be designed explicitly between the application and database.

## 7. Exception Handling

PL/pgSQL can handle exceptions:

```sql
BEGIN
    INSERT INTO employees (...);
EXCEPTION
    WHEN unique_violation THEN
        -- handle duplicate
END;
```

Exception handling should be used intentionally. Catching every exception and hiding it can make failures much harder to diagnose.

## 8. When Procedures Make Sense

Procedures can be useful for:

- Database administration workflows
- Reusable multi-step database operations
- Data-processing tasks
- Logic that should be invoked explicitly rather than embedded in a SELECT expression

They are not automatically preferable to application services.

## Common Mistakes

- Using `RETURNS` in a procedure declaration.
- Trying to call a procedure with `SELECT` instead of `CALL`.
- Confusing dollar quoting with statement delimiters.
- Catching exceptions without preserving useful failure information.
- Moving application logic into the database without considering coupling.

## Engineering Takeaways

You should understand how procedures differ from functions, define PL/pgSQL procedures with parameters, call them correctly, and reason about transaction and exception behavior.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**Triggers** — automatically invoking database functions when specified table events occur.