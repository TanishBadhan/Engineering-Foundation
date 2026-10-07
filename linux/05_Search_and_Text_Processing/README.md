# Search & Text Processing

The command-line toolkit for locating files, matching content, passing results between commands, and transforming text.

## Architecture

Files → Find → Filter → Transform → Extract → Pipeline

## Commands

`find` · `grep` · `xargs` · `sed` · `awk`

## Core Concepts

`find` searches filesystem objects by conditions such as name and type. `grep` searches content; `grep -i` ignores case and `grep -r` searches recursively. Globbing such as `*.txt` is shell pattern matching. `sed` performs stream transformations. `awk` processes fields, conditions, and actions. `xargs` turns input into command arguments.

**Key distinction:** find answers which files; grep answers which content; `sed` transforms text; `awk` extracts or computes from fields.

## Examples

Hands-on commands are provided in [`examples.sh`](./examples.sh).

## Engineering Relevance

This topic builds practical Linux skills used in servers, cloud systems, containers, CI/CD, backend services, databases, and AI infrastructure.

## Completion Check

You should be able to:

- explain the mental model behind this topic
- use the listed commands without blindly copying them
- interpret normal command output
- recognize common mistakes and failure modes
- explain why the topic matters in real engineering environments

**Next:** Continue to the next numbered Linux topic.
