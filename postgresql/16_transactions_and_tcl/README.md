# Transactions and TCL

## What It Is
Transactions group related changes into an atomic unit using transaction control commands.

## Why It Matters
These patterns support reusable queries, safe state changes, and application reporting.

## Key Concepts
Understand evaluation behavior, transaction boundaries, NULL semantics, and whether data is stored or computed.

## Common Mistakes
Do not confuse WHERE with aggregate filtering, leave transactions open, or assume a normal view stores result rows.

## Practice
See `practice.sql` for progressive exercises.

## Engineering Notes
Keep abstractions explicit and transaction boundaries focused.