# SSH & Remote Computing

Access and operate another machine securely through a remote terminal.

## Architecture

Local SSH client → Encrypted connection → Remote SSH server → Remote process

## Commands & Syntax

ssh · ssh -p

## Core Concepts

SSH provides encrypted remote shell access. ssh username@server_ip normally targets port 22; ssh -p 2222 username@server_ip selects another port. Key authentication uses a public/private key pair: the private key stays on the client and the public key is installed on the server. Commands run after login execute on the remote machine. Remote access does not itself mean distributed computing.

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
