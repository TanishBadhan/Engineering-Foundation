# Basic Bash Scripting

Turn repeated command-line work into automation with Bash variables, arguments, conditions, loops, functions, and exit codes.

## Architecture

Script → Inputs → Logic → Commands → Exit status

## Commands & Syntax

#!/bin/bash · variables · $1 · $2 · $@ · if · elif · else · case · arrays · for · while · functions · exit · $?

## Core Concepts

#!/bin/bash selects Bash. Variables use $name; $1, $2, etc. are positional arguments and $@ represents all arguments. if/elif/else handles conditions; case handles branches; arrays hold multiple values; for and while provide loops; functions group reusable logic. exit N sets a script's exit status and $? reads the previous command's status. Bash scripting can combine grep, sed, and awk into repeatable automation.

## Examples

Hands-on practice is provided in examples.sh.

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
