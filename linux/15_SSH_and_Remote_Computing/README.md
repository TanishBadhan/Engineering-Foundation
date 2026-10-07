# SSH & Remote Computing

The foundation for securely accessing and operating another machine from a terminal.

## Architecture

Local client → SSH → Remote server → Remote process

## Commands

`ssh` · `ssh -p`

## Core Concepts

SSH provides encrypted remote shell access. ssh username@server_ip uses conventional port 22; ssh -p 2222 selects another port. Key authentication uses a public/private pair: the private key stays on the client and the public key is installed on the server. Commands after connection execute on the remote machine. Remote access is not automatically distributed computing.

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
