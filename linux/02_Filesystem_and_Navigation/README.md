# Filesystem & Navigation

The core model for understanding Linux paths and moving through the filesystem.

## Architecture

Filesystem → `/` → Directory → Path → Navigation

## Commands

`pwd` · `ls` · `cd`

## Core Concepts

Absolute paths start at `/`; relative paths start from the current directory. `.` is current, `..` is parent, and `~` is home. Linux paths are case-sensitive and hidden names normally begin with `.`.

- `pwd` prints the working directory.
- `ls` lists directory contents.
- `cd` changes the current directory.

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
