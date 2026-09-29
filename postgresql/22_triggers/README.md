# Triggers

Triggers automatically invoke a PostgreSQL function when a specified database event occurs. They are powerful because they enforce or automate behavior at the database boundary, but they can also make application behavior less obvious.

## 1. Trigger Architecture

A PostgreSQL trigger generally involves two objects:

```text
Trigger
   ↓
Trigger function
   ↓
Database operation
```

The trigger defines **when** the function runs. The trigger function defines **what** happens.

## 2. Trigger Function

A trigger function returns the special type `TRIGGER`.

Example:

```sql
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;
```

For row-level INSERT/UPDATE triggers, `NEW` represents the new row.

`OLD` represents the previous row where applicable.

## 3. CREATE TRIGGER

```sql
CREATE TRIGGER customers_updated_at
BEFORE UPDATE ON customers
FOR EACH ROW
EXECUTE FUNCTION set_updated_at();
```

The pieces mean:

```text
BEFORE UPDATE
    -> event/timing

ON customers
    -> target table

FOR EACH ROW
    -> row-level execution

EXECUTE FUNCTION
    -> function invoked
```

## 4. BEFORE vs AFTER

### BEFORE

Runs before the operation is completed.

Useful when the trigger needs to modify or validate the row.

Example:

```text
UPDATE
  ↓
BEFORE trigger
  ↓
row modification
```

### AFTER

Runs after the row operation has occurred.

Useful for actions that should happen after the primary change succeeds.

The correct timing depends on the required semantics.

## 5. INSERT, UPDATE, DELETE

Triggers can respond to:

```text
INSERT
UPDATE
DELETE
```

For example:

```sql
CREATE TRIGGER audit_customer
AFTER UPDATE ON customers
FOR EACH ROW
EXECUTE FUNCTION audit_customer_change();
```

For DELETE operations, `OLD` is available while `NEW` is not. For INSERT, `NEW` is available while `OLD` is not.

## 6. Row-Level vs Statement-Level

### FOR EACH ROW

Runs once for every affected row.

If an UPDATE modifies 1,000 rows, the trigger function may execute 1,000 times.

### FOR EACH STATEMENT

Runs once for the entire SQL statement.

```sql
FOR EACH STATEMENT
```

Choose based on whether the logic needs individual row values or only statement-level behavior.

## 7. Common Use Cases

Triggers can be appropriate for:

- Audit logging
- Maintaining derived metadata
- Automatic timestamps
- Enforcing specialized invariants
- Recording database-level changes

Example audit flow:

```text
UPDATE customer
     ↓
AFTER UPDATE trigger
     ↓
audit table
     ↓
old/new change recorded
```

## 8. Trigger Side Effects

Triggers are implicit.

An application may execute:

```sql
UPDATE customers
SET c_name = 'Tanish'
WHERE c_id = 1;
```

but that statement may also cause trigger functions to modify other tables.

This can be powerful, but it increases the amount of behavior hidden behind a simple statement.

## 9. Performance

A row-level trigger can run once per affected row.

Therefore:

```text
UPDATE 1 row
 -> trigger once

UPDATE 1,000,000 rows
 -> potentially 1,000,000 trigger executions
```

Trigger logic must be designed and measured accordingly.

## 10. Trigger vs Application Logic

A trigger can be valuable when a rule must hold regardless of which client changes the data.

However, application logic may be clearer when the behavior is part of a broader business workflow.

A useful question is:

> Does this invariant belong to the database regardless of who writes the data?

If yes, database-level enforcement may be appropriate.

## 11. Common Trigger Hazards

### Hidden behavior

Developers may forget that a write invokes additional logic.

### Recursive behavior

A trigger can indirectly cause another trigger to fire, potentially producing unexpected recursion.

### Performance overhead

Large bulk writes can execute trigger code many times.

### Debugging complexity

The original SQL statement may not reveal every side effect.

## Common Mistakes

- Confusing trigger definitions with trigger functions.
- Forgetting to return the correct value from a row-level trigger function.
- Using row-level triggers for expensive operations over huge datasets.
- Creating hidden side effects without documenting them.
- Assuming triggers are always better than explicit application logic.

## Engineering Takeaways

You should understand the two-part trigger model, `NEW` and `OLD`, trigger timing, row vs statement execution, common use cases, and the operational tradeoffs of implicit database behavior.

## Practice

The corresponding exercises are in `practice.sql`.

## Completion

This is the final topic in the PostgreSQL learning sequence. After completing the section, the next step is to apply these concepts through larger SQL exercises and backend projects rather than continuing indefinitely into DBA-specialization topics.