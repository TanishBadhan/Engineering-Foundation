# Archives & Compression

How Linux packages multiple files into archives and optionally compresses the resulting data.

## Architecture

Files → Archive → Compress → Extract

## Commands

`gzip` · `gunzip` · `tar`

## Core Concepts

Archiving combines files into one container; compression reduces data size. .tar is an archive, .gz is gzip compression, and .tar.gz is a tar archive compressed with gzip. tar -cf creates, tar -tf lists, tar -xf extracts, tar -czf creates gzip-compressed archives, and tar -xzf extracts them.

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
