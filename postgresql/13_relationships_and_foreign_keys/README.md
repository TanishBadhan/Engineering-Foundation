# Relationships and Foreign Keys

Relational databases become powerful when separate tables represent connected entities. Foreign keys turn those conceptual relationships into enforceable database relationships.

## 1. Entity vs Relationship

Suppose an application has:

```text
Customer
Order
Product
```

These are entities.

Relationships describe how they connect:

```text
Customer -> places -> Order
Order    -> contains -> Product
```

The database represents these relationships through keys.

## 2. One-to-Many

The most common relationship is one-to-many.

```text
Customer 1
   |
   +---- Order 1
   +---- Order 2
   +---- Order 3
```

Implementation:

```sql
CREATE TABLE orders (
    o_id SERIAL PRIMARY KEY,
    c_id INT NOT NULL REFERENCES customers(c_id)
);
```

The foreign key belongs on the many side.

## 3. Many-to-Many

Suppose an order can contain many products and a product can appear in many orders.

Directly storing a list of product IDs inside an order is usually not the relational design.

Instead:

```text
orders
   |
order_items
   |
products
```

The junction table contains the relationship:

```sql
CREATE TABLE order_items (
    o_id INT REFERENCES orders(o_id),
    p_id INT REFERENCES products(p_id),
    quantity INT NOT NULL,
    PRIMARY KEY (o_id, p_id)
);
```

The composite primary key prevents the same product from appearing twice within the same order, assuming that is the chosen model.

## 4. One-to-One

A one-to-one relationship can be enforced using a foreign key plus uniqueness.

```sql
CREATE TABLE user_profiles (
    user_id INT PRIMARY KEY REFERENCES users(id)
);
```

Because `user_id` is itself unique, each user can have at most one profile.

## 5. Referential Integrity

Suppose:

```text
customers.c_id = 10
orders.c_id = 10
```

The foreign key guarantees that the referenced customer must exist under the configured constraint rules.

This prevents orphaned child records.

## 6. ON DELETE Behavior

PostgreSQL supports different behaviors when a referenced parent row is deleted.

### CASCADE

Delete dependent rows too.

```sql
ON DELETE CASCADE
```

Useful when child data has no independent meaning.

### SET NULL

Set the foreign key to null.

```sql
ON DELETE SET NULL
```

The column must permit nulls.

### RESTRICT / NO ACTION

Prevent the parent deletion when dependent rows exist, subject to the exact constraint semantics.

Choose behavior based on business meaning, not convenience.

## 7. Foreign Keys and Indexes

A foreign key protects referential integrity, but it does not automatically mean the referencing column has the index needed for every workload.

For frequently joined or parent-deletion-sensitive relationships, indexing the child foreign-key column can be important.

Example:

```sql
CREATE INDEX idx_orders_customer_id
ON orders(c_id);
```

Whether an index is useful depends on query patterns and table sizes.

## 8. Relationship Design Process

Use this sequence:

```text
Identify entities
      ↓
Identify relationships
      ↓
Determine cardinality
      ↓
Choose primary keys
      ↓
Place foreign keys
      ↓
Define delete/update behavior
      ↓
Add useful indexes
```

## 9. Example: E-Commerce Model

```text
Customer
   |
   +---- Orders
             |
             +---- Order Items ---- Products
```

This model separates:

- Customer identity
- Order identity
- Product identity
- Quantity purchased
- Relationship between orders and products

That separation avoids duplicating product and customer data unnecessarily.

## Common Mistakes

- Putting the foreign key on the wrong side of a one-to-many relationship.
- Modeling many-to-many data without a junction table.
- Using `CASCADE` without considering deletion consequences.
- Assuming foreign keys automatically solve query performance.
- Duplicating parent data in child tables instead of referencing it.

## Engineering Takeaways

You should be able to identify relationship cardinality, implement one-to-one/one-to-many/many-to-many models, choose foreign-key behavior, and understand the integrity/performance roles of keys and indexes.

## Practice

The corresponding exercises are in `practice.sql`.

## Next Topic

**JOINs** — retrieving related data across these tables.