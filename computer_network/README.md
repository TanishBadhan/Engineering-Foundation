# Computer Networking

A structured, practical record of computer networking fundamentals, transport protocols, networked programming, and the concepts needed to build and troubleshoot backend systems.

## Learning goals

- Explain how devices address and communicate with one another.
- Understand network models, encapsulation, protocols, and ports.
- Reason about TCP and UDP, including their trade-offs and socket APIs.
- Trace a web request from name resolution through transport and application protocols.
- Use basic tools to inspect connections and diagnose networking failures.
- Validate understanding through small, reproducible experiments.

## Roadmap

Topics are ordered by dependency. A topic is marked as covered based on study progress; notes and practical verification will be added incrementally.

| Stage | Topic | Status |
|---|---|---|
| 00 | Foundations: networking basics, network types, and topologies | Studied; documentation pending |
| 01 | IP addressing and subnetting: IPv4, IPv6, loopback, subnetting, CIDR | Basics studied; depth to verify |
| 02 | Protocols, ports, OSI/TCP-IP models, encapsulation | Studied; documentation pending |
| 03 | Transport layer: TCP, UDP, sockets, datagrams | Notes and local Python labs documented; practical verification pending |
| 04 | DNS and name resolution | Planned |
| 05 | HTTP and APIs | Planned |
| 06 | HTTPS, TLS, and certificates | Planned |
| 07 | Client-server architecture and connection lifecycle | Planned |
| 08 | Proxies and load balancing | Planned |
| 09 | Network troubleshooting and diagnostic commands | Planned |
| 10 | SSH and remote access revision | Revision planned |

## Practical labs

Practical work will be kept separate from conceptual notes as the module grows. Current and planned labs include:

- Local network inspection
- TCP socket communication in Python
- UDP message communication in Python
- HTTP request inspection
- Network troubleshooting

The [TCP/UDP module](TCP-UDP/README.md) contains transport-layer notes and Python socket labs.

Each lab should document its purpose, prerequisites, run instructions, expected behavior, limitations, and cleanup steps. Learning experiments will be identified as such rather than presented as production-ready software.

## Documentation standard

Topic notes will cover:

1. Definition and purpose
2. The problem the concept solves
3. A mental model and step-by-step explanation
4. Practical examples
5. Common misconceptions and trade-offs
6. Relevance to backend engineering
7. Knowledge-check questions
8. References

## Completion criteria

The goal is practical understanding, not memorization. By the end of this roadmap, I should be able to explain the lifecycle of a web request, distinguish TCP from UDP, run and reason about basic socket programs, and use common diagnostic commands to investigate connection problems.

## Working principles

- Keep explanations technically accurate and revise misconceptions when found.
- Prefer small, reproducible experiments over unsupported claims.
- Keep conceptual notes, labs, and exercises separate.
- Add files when meaningful content exists; do not create empty placeholders.
- Use focused commits that describe one coherent change.
