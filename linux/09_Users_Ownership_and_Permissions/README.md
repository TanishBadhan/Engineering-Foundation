# Users, Ownership & Permissions

Linux access control is based on users, groups, ownership, and read/write/execute permissions.

## Architecture

User → Group → Owner → rwx → Access

## Commands

`who` · `su` · `sudo` · `passwd` · `chown` · `chmod`

## Core Concepts

Permissions apply to owner, group, and other. r=4, w=2, x=1; 755 means owner rwx and others r-x; 644 means owner rw and others r--. sudo runs authorized commands with elevated privileges; su switches user. chown changes ownership and chmod changes permissions. Practice changes only on files you own.

## Examples
Hands-on commands are provided in the examples.sh file.

## Engineering Relevance

This topic builds practical Linux skills used in servers, cloud systems, containers, CI/CD, backend services, databases, and AI infrastructure.

## Completion Check

- explain the mental model behind this topic
- use the listed commands without blindly copying them
- interpret normal command output
- recognize common mistakes and failure modes
- explain why the topic matters in real engineering environments

**Next:** Continue to the next numbered Linux topic.
