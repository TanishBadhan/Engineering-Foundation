# User-Defined Functions

## What It Is
Functions package reusable database-side computation with parameters and explicit return types.

## Why It Matters
These features support structured complex queries and reusable database-side logic.

## Key Concepts
Understand statement scope, row preservation, partitions, ordering, parameters, and return contracts.

## Common Mistakes
Do not expect a CTE to persist, use GROUP BY when row detail must remain, or omit a function return contract.

## Practice
See `practice.sql` for progressive exercises.

## Engineering Notes
Use advanced SQL when it makes the data operation clearer and keeps the abstraction close to the data.