# PostgreSQL CLI Command Reference

## Connection
`psql -U <user> -d <database>`

## Navigation
- `\\l` — list databases
- `\\c <database>` — connect
- `\\dn` — list schemas
- `\\dt` — list tables

## Inspection
- `\\d <table>` — describe a table
- `\\du` — list roles

## Execution
- `\\i file.sql` — execute a SQL file
- `\\o file.txt` — redirect output
- `\\q` — quit

## Help
- `\\?` — psql commands
- `\\h SELECT` — SQL help