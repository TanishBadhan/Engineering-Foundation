# Users, Ownership & Permissions

Understand Linux users, groups, ownership, and read/write/execute access control.

## Architecture

User → Group → Owner → rwx → Access decision

## Commands & Syntax

`who` `su` `sudo` `passwd` `chown` `chmod`

## Core Concepts

Permissions are evaluated for owner, group, and other. `r=4`, `w=2`, `x=1`; therefore `755` means owner `rwx` and others `r-x`, while `644` means owner `rw-` and others `r--`. `sudo` runs authorized commands with elevated privileges; `su` switches identity; `chown` changes ownership; `chmod` changes permissions. Practice permission changes only on files you own.

## Examples

Hands-on practice is provided in [examples.sh](./examples.sh).

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
