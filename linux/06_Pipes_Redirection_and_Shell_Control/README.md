# Pipes, Redirection & Shell Control

Connect commands, redirect streams, and control execution using shell operators.

## Architecture

stdin (0) → Command → stdout (1) / stderr (2) → File or Pipeline

## Commands & Syntax

`|` `>` `>>` `2>` `2>&1` `&` `&&` `||` `$?` `true` `false`

## Core Concepts

A pipe sends stdout from one command to another. `>` overwrites a file; `>>` appends. `2>` redirects stderr and `2>&1` sends stderr to the current stdout destination. `&&` continues after success, `||` provides a fallback after failure, while `&` starts a command in the background. `$?` contains the previous exit status: `0` normally means success and non-zero means failure.

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
