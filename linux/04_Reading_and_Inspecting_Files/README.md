# Reading & Inspecting Files

Commands for reading text, inspecting sections, counting content, sorting data, and comparing files.

## Architecture

File → Read → Inspect → Count → Sort → Compare

## Commands

`cat` · `less` · `head` · `tail` · `echo` · `wc` · `sort` · `uniq` · `diff`

## Core Concepts

`cat` prints contents and `cat -n` numbers lines. `less` provides interactive viewing. `head -n 40` shows up to 40 lines; `tail -n 20` shows up to 20 lines. `echo` prints text. `wc -l` counts newline-separated lines; `wc -w` counts words. `sort` orders lines; `uniq` removes adjacent duplicates; `diff` compares files.

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
