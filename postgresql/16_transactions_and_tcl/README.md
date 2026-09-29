# Transactions and TCL

Transactions define atomic units of database work. They are essential whenever several operations must either succeed together or fail together.

## 1. The Problem Transactions Solve

Consider placing an order:

```text
1. Create order
2. Add order items
3. Reduce inventory
4. Record payment state
```

If step 3 fails after steps 1 and 2 succeed, the database could be left in an inconsistent state unless the operations are coordinated.

A transaction provides a boundary:

```text
BEGIN
  ↓
operation 1
operation 2
operation 3
  ↓
COMMIT
```

Or:

```text
BEGIN
  ↓
failure
  ↓
ROLLBACK
```

## 2. BEGIN

Start an explicit transaction:

```sql
BEGIN;
```

You can also write:

```sql
START TRANSACTION;
```

## 3. COMMIT

Make the transaction's changes durable and visible according to PostgreSQL's transaction semantics:

```sql
COMMIT;
```

## 4. ROLLBACK

Discard changes made during the current transaction:

```sql
ROLLBACK;
```

## 5. SAVEPOINT

A savepoint creates a point to which part of a transaction can roll back.

```sql
BEGIN;

UPDATE products
SET price = price * 1.10;

SAVEPOINT price_change;

UPDATE products
SET price = price * 2;

ROLLBACK TO SAVEPOINT price_change;

COMMIT;
```

The first update can remain while the second update is undone.

## 6. ACID

Transactions are commonly described using ACID.

### Atomicity

The transaction behaves as one logical unit.

### Consistency

A successful transaction moves the database from one valid state to another, respecting constraints and rules.

### Isolation

Concurrent transactions should not observe intermediate states in ways that violate the selected isolation semantics.

### Durability

After a successful commit, PostgreSQL provides durability guarantees so committed data survives failures according to the database's configuration and storage guarantees.

## 7. Isolation

PostgreSQL supports transaction isolation levels including:

- Read Committed
- Repeatable Read
- Serializable

The isolation level controls what concurrent transactions can observe and which concurrency anomalies are possible.

The default PostgreSQL isolation level is Read Committed.

Do not think of isolation as simply "locking everything." PostgreSQL uses MVCC and other mechanisms to provide concurrency.

## 8. MVCC Mental Model

PostgreSQL uses **Multi-Version Concurrency Control**.

Conceptually, updates create new row versions rather than simply overwriting the version every concurrent reader must use.

This allows readers and writers to operate concurrently in many situations without every read blocking every write.

Understanding MVCC becomes important later when studying PostgreSQL internals, locks, and performance.

## 9. Transactions in Backend Applications

A typical API operation might be:

```text
HTTP request
   ↓
BEGIN
   ↓
validate / update records
   ↓
COMMIT
   ↓
HTTP response
```

If the operation fails:

```text
ROLLBACK
   ↓
error response
```

The application must define the transaction boundary carefully.

A transaction that is too small may not protect the whole logical operation. A transaction that is held open too long can increase contention and resource usage.

## 10. Locking and Concurrency

Some operations acquire locks.

For example:

```sql
SELECT *
FROM products
WHERE p_id = 1
FOR UPDATE;
```

This can be used when application logic needs to lock selected rows while performing related transactional work.

Locking should be designed around actual concurrency requirements. Excessive locking can reduce throughput and cause contention or deadlocks.

## 11. Deadlocks

Two transactions can wait on resources held by each other.

```text
Transaction A holds row 1
      ↓
waits for row 2

Transaction B holds row 2
      ↓
waits for row 1
```

PostgreSQL can detect deadlocks and abort one transaction.

A common mitigation is consistent lock/update ordering.

## Common Mistakes

- Treating every SQL statement as if it automatically represents the application's logical transaction.
- Keeping transactions open unnecessarily long.
- Ignoring concurrent access.
- Assuming isolation means no concurrency.
- Updating multiple resources in inconsistent orders.
- Catching a database error but continuing to use a failed transaction without rolling it back.

## Engineering Mental Model

A transaction is a boundary around a state transition:

```text
Valid state A
    ↓
transaction
    ↓
Valid state B
```

The engineering question is:

> What operations must succeed together to preserve the application's invariant?

That determines the transaction boundary.

## Practice

The corresponding transaction exercises are in `practice.sql`.

## Next Topic

**Views** — defining reusable query-based database interfaces.