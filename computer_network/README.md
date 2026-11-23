# Computer Networking

A structured, practical record of networking fundamentals, transport protocols, networked programming, and the concepts needed to build and troubleshoot backend systems.

## Learning Goals

- Explain how devices address and communicate with one another.
- Understand network models, encapsulation, protocols, and ports.
- Reason about TCP and UDP, including their trade-offs and socket APIs.
- Trace a web request from name resolution through transport and application protocols.
- Use basic tools to inspect connections and diagnose networking failures.
- Validate understanding through small, reproducible experiments.

## Roadmap

Topics are ordered by dependency. Completion reflects the concepts studied; practical verification and documentation are tracked separately where appropriate.

| Stage | Topic | Status |
|---|---|---|
| 00 | Networking basics, network types, and topologies | Studied; documentation pending |
| 01 | IP addressing and subnetting: IPv4, IPv6, loopback, subnetting, CIDR | Basics studied; depth to verify |
| 02 | Protocols, ports, OSI/TCP-IP models, and encapsulation | Studied; documentation pending |
| 03 | Transport layer: TCP, UDP, sockets, and datagrams | Notes and local Python labs documented; practical verification pending |
| 04 | DNS and name resolution | Planned |
| 05 | HTTP and API fundamentals | **Completed and documented** |
| 06 | HTTPS, TLS, and certificates | Planned |
| 07 | Client-server architecture and connection lifecycle | Planned |
| 08 | Proxies and load balancing | Planned |
| 09 | Network troubleshooting and diagnostic commands | Planned |
| 10 | SSH and remote access revision | Revision planned |

## Completed Module: HTTP and API Fundamentals

The HTTP and introductory API topics are grouped in one module:

[**HTTP and API Fundamentals →**](./HTTP%20and%20API/README.md)

Covered topics:

- HTTP versions
- HTTP methods
- HTTP status codes
- HTTP headers
- Cookies
- CORS
- HTTP caching
- What an API is
- URL structure
- Path and query parameters
- Content negotiation

This completion covers the fundamentals listed above. REST principles, resource modelling, URI design, endpoint naming, versioning, HATEOAS, and other API-design topics remain separate roadmap items.

## Practical Labs

Practical work is kept separate from conceptual notes. Current and planned labs include:

- Local network inspection
- TCP socket communication in Python
- UDP message communication in Python
- HTTP request inspection
- Network troubleshooting

The [TCP/UDP module](./TCP-UDP/README.md) contains transport-layer notes and Python socket labs.

Each lab should document its purpose, prerequisites, run instructions, expected behavior, limitations, and cleanup steps. Learning experiments are identified as such rather than presented as production-ready software.

## Documentation Standard

Topic notes aim to include:

1. Definition and purpose
2. The underlying mechanism or mental model
3. Structured explanations and examples
4. Important distinctions and common misconceptions
5. Practical relevance
6. A concise takeaway

## Completion Criteria

The goal is practical understanding, not memorization. By the end of this roadmap, I should be able to explain the lifecycle of a web request, distinguish TCP from UDP, run and reason about basic socket programs, and use common diagnostic commands to investigate connection problems.

## Working Principles

- Keep explanations technically accurate and revise misconceptions when found.
- Prefer small, reproducible experiments over unsupported claims.
- Keep conceptual notes, labs, and exercises separate.
- Add files when meaningful content exists; do not create empty placeholders.
- Use focused commits that describe one coherent change.
