# Disk & System Resources

Inspect filesystem capacity, directory usage, memory, and open files.

## Architecture

Filesystem capacity ↔ Directory usage ↔ RAM/Swap ↔ Open files

## Commands & Syntax

`du` `df` `free` `lsof`

## Core Concepts

`df -h` reports filesystem capacity and free space. `du -sh` reports space consumed by a path. `free -h` summarizes RAM and swap. `lsof` lists files opened by processes. The important distinction is **df = filesystem capacity** versus **du = what is consuming space**.

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
