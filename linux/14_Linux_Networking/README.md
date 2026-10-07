# Linux Networking

The command-line foundation for inspecting interfaces, IP addresses, routes, ports, sockets, and HTTP connectivity.

## Architecture

Interface → IP → Route → Port → Socket → Service

## Commands

`ip` · `ip addr` · `ip link` · `ip route` · `ping` · `curl` · `ss`

## Core Concepts

ip addr shows interfaces and addresses; ip link shows interface state; ip route shows routes and the default gateway. ping tests ICMP reachability. curl tests HTTP services. ss -tuln shows listening TCP/UDP sockets. IP identifies a network endpoint; a port identifies a service endpoint; a socket is a communication endpoint. 127.0.0.1 is IPv4 loopback. 0.0.0.0:8000 listens on all IPv4 interfaces; 127.0.0.1:8000 is local-only.

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
