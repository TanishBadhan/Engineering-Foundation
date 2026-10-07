# Environment Variables & PATH

How shells store configuration, export values to child processes, and locate executable commands.

## Architecture

Shell → Variables → Environment → PATH → Executable lookup

## Commands

`printenv` · `env` · `export` · `which` · `command -v` · `source` · `alias`

## Core Concepts

A shell variable exists in the current shell; an exported variable is passed to child processes. $USER commonly identifies the current user. $PATH is a colon-separated list of directories searched for executables. which and command -v locate commands. source ~/.bashrc reloads Bash configuration. alias creates a shortcut. PATH is a list of directories, not commands.

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
