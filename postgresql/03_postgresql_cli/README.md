# PostgreSQL CLI

## What It Is
`psql` is PostgreSQL's command-line client.

## Why It Matters
CLI fluency makes database development, inspection, scripting, and debugging efficient.

## Key Commands
`\\l` list databases; `\\c` connect; `\\dn` schemas; `\\dt` tables; `\\d table` structure; `\\i file.sql` execute a file; `\\q` quit; `\\?` psql help; `\\h` SQL help.

## Common Mistakes
Do not confuse psql meta-commands beginning with `\\` with SQL statements.

## Engineering Notes
Use CLI scripts for repeatable setup and diagnostics.