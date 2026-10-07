# Archives & Compression

Package multiple files into archives and optionally compress the resulting data.

## Architecture

Files → Archive → Compress → Extract

## Commands & Syntax

gzip · gunzip · tar

## Core Concepts

An archive combines files; compression reduces their representation size. .tar is an archive, .gz is gzip compression, and .tar.gz is a gzip-compressed tar archive. tar -cf creates, tar -tf lists, tar -xf extracts, tar -czf creates a gzip-compressed archive, and tar -xzf extracts one.

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
