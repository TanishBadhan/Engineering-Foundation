# Services & System Logs

The basic model for managing long-running services and reading system logs during troubleshooting.

## Architecture

Service/Daemon → Lifecycle → Logs → Troubleshooting

## Commands

`systemctl` · `journalctl`

## Core Concepts

A service or daemon is a long-running background process. systemctl status inspects state; start, stop, and restart change runtime state when authorized. journalctl reads systemd journal logs and journalctl -u filters by service. Logs provide evidence for startup failures, crashes, permissions, ports, and configuration problems. WSL or minimal environments may not run systemd.

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
