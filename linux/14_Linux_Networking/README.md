# Linux Networking

Inspect interfaces, addresses, routes, ports, sockets, and basic HTTP connectivity from Linux.

## Architecture

Interface → IP → Route → Port → Socket → Service

## Commands & Syntax

ip · ip addr · ip link · ip route · ping · curl · ss

## Core Concepts

ip addr shows interfaces and addresses; ip link shows interface state; ip route shows routes and the default gateway. ping tests ICMP reachability. curl tests HTTP services. ss -tuln shows listening TCP/UDP sockets. An IP identifies a network endpoint, a port identifies a service endpoint, and a socket represents a communication endpoint. 127.0.0.1 is IPv4 loopback; 0.0.0.0:8000 means listen on all IPv4 interfaces while 127.0.0.1:8000 is local-only.

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
