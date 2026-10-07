# Environment Variables & PATH

Understand shell variables, exported environment variables, executable lookup, and shell configuration.

## Architecture

Shell → Variables → Environment → PATH → Executable lookup

## Commands & Syntax

printenv · env · export · which · command -v · source · alias

## Core Concepts

A shell variable exists in the current shell; an exported variable is inherited by child processes. $USER commonly identifies the current user. $PATH is a colon-separated list of directories searched for executables. which and command -v locate commands. source ~/.bashrc reloads Bash configuration in the current shell. Aliases provide shortcuts.

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
