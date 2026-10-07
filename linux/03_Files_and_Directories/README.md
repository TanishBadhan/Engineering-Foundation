# Files & Directories

How to create, copy, move, link, rename, and remove filesystem objects.

## Architecture

Path → File/Directory → Create → Copy → Move → Link → Remove

## Commands

`mkdir` · `touch` · `rmdir` · `rm` · `mv` · `cp` · `ln` · `open`

## Core Concepts

`mkdir` creates directories; `touch` creates files; `mv` moves or renames; `cp` copies and `cp -r` copies directories recursively; `rm` removes files; `rmdir` removes empty directories. `ln -s` creates symbolic links. `open` is platform-dependent and commonly associated with macOS. A hard link references the same inode; a symbolic link stores a path reference.

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
