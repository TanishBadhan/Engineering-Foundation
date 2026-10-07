# Processes & Job Control

Observe running programs and control foreground and background processes.

## Architecture

Program → Process → PID → Signal → Foreground/Background

## Commands & Syntax

`ps` `top` `pgrep` `kill` `pkill` `killall` `jobs` `bg` `fg`

## Core Concepts

A program is executable code; a process is a running instance with its own PID and resources. `ps` provides a process snapshot and `top` provides live monitoring. `pgrep` finds PIDs. `kill` sends signals; `pkill` and `killall` target processes by name. `jobs`, `bg`, and `fg` control shell jobs. Prefer graceful termination before forceful termination.

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
