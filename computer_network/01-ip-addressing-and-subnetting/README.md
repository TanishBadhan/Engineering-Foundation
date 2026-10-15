# IP Addressing and Subnetting

This note covers the addressing concepts needed to understand how a host identifies a network destination and how IP networks are divided.

## 1. Why IP addressing exists

A network needs a way to identify the source and destination of packets. An IP address is a logical address used by the Internet Protocol to identify an interface in an IP network.

An IP address is not the same as a MAC address, a domain name, or a TCP/UDP port:

- **IP address:** identifies a network-layer destination/interface.
- **MAC address:** identifies a link-layer interface on a local network segment.
- **Domain name:** a human-readable name that DNS can resolve to IP addresses.
- **Port:** identifies an application endpoint associated with a transport protocol on a host.

These identifiers work together but solve different problems.

## 2. IPv4

IPv4 addresses are 32 bits long. They are commonly written as four decimal octets separated by dots, for example:

`192.168.1.25`

Each octet represents 8 bits and ranges from 0 to 255. The address contains network and host portions; the prefix length tells us where that boundary lies.

## 3. IPv6

IPv6 addresses are 128 bits long and are written in hexadecimal groups separated by colons, for example:

`2001:db8::25`

IPv6 provides a much larger address space than IPv4. Consecutive zero groups can be compressed using `::` once in an address. Leading zeros within a group may also be omitted.

The prefix length, such as `/64`, indicates how many leading bits belong to the network prefix.

## 4. Loopback and private addresses

- **IPv4 loopback:** `127.0.0.0/8`, commonly accessed as `127.0.0.1`.
- **IPv6 loopback:** `::1`.
- **Common private IPv4 ranges:** `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.

Loopback traffic stays on the local host. Private IPv4 addresses are intended for private networks and are not globally routed across the public Internet by default. A private address may still reach external services through routing and mechanisms such as network address translation (NAT).

Do not assume that every address beginning with `172` is private: the private range is specifically `172.16.0.0` through `172.31.255.255`.

## 5. CIDR and prefix length

CIDR notation appends a slash and prefix length to an address, for example `192.168.1.0/24`.

For IPv4:

- The address has 32 bits in total.
- A `/24` prefix uses 24 bits for the network prefix.
- The remaining 8 bits are available for host addressing within that block.

For a conventional IPv4 subnet, the total number of addresses in a block is:

`2^(32 - prefix length)`

For example, a `/24` contains `2^8 = 256` addresses. In a typical conventional subnet, the network and broadcast addresses are not assigned to hosts, leaving 254 usual host addresses. Special-purpose and point-to-point cases can differ, so do not apply the 254-host rule blindly to every prefix.

For IPv6, the same prefix arithmetic applies using 128 bits, but IPv6 does not use an IPv4-style broadcast address.

## 6. Subnetting: a practical mental model

Subnetting divides an address block into smaller blocks. Increasing the prefix length leaves fewer bits for host/interface addresses and creates smaller subnets.

Example: splitting `192.168.1.0/24` into two equal IPv4 subnets requires one more network bit:

- `192.168.1.0/25`
- `192.168.1.128/25`

Each `/25` contains 128 IPv4 addresses. In conventional subnets, 126 are normally available for host assignment.

When solving subnet questions:

1. Identify whether the address is IPv4 or IPv6.
2. Read the prefix length.
3. Calculate the host-bit count.
4. Calculate the block size.
5. Find the network boundary and range.
6. Check special-address rules before counting usable hosts.

## 7. What an IP address does not tell you

An IP address alone does not guarantee that a host is reachable. Routing, firewall rules, interface configuration, address translation, and whether a service is listening all matter.

Likewise, an IP address does not identify a particular application process. A transport-layer port helps direct traffic to the appropriate endpoint on the destination host.

## 8. Backend engineering relevance

IP addressing appears in:

- binding a development server to `127.0.0.1`, `0.0.0.0`, or a specific interface;
- configuring containers, private subnets, and cloud virtual networks;
- reading logs that contain client or server addresses;
- diagnosing incorrect routes, unreachable hosts, and address conflicts;
- understanding why localhost inside a container is not the same as localhost on the host machine.

Binding to `0.0.0.0` means listening on all available IPv4 interfaces; it does not mean that `0.0.0.0` is a normal destination address for clients. Exposing a service on all interfaces may make it reachable from other machines, depending on firewall and network configuration.

## 9. Common misconceptions

- **“An IP address identifies an application.”** It identifies a network destination/interface; ports help identify transport endpoints.
- **“Every IP address is public.”** Private, loopback, link-local, and other special-purpose ranges exist.
- **“A /24 always means 254 usable hosts.”** That is the conventional IPv4 subnet case, not a universal rule for every prefix or protocol.
- **“If I know the destination IP, the connection must work.”** Routing, filtering, and service availability can still prevent communication.
- **“IPv6 is just a longer IPv4 address.”** IPv6 has different addressing conventions and operational details, including no broadcast addressing.

## 10. Knowledge check

Try these without looking at the answers first.

1. How many bits are in an IPv4 address? How many are in IPv6?
2. What is the difference between an IP address and a port?
3. Is `172.20.4.5` in a private IPv4 range? What about `172.40.4.5`?
4. How many total IPv4 addresses are in a `/26` block?
5. How does increasing an IPv4 prefix from `/24` to `/25` affect block size?
6. What is the difference between `127.0.0.1` and `0.0.0.0` when configuring a server?

## References

- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 4632 — Classless Inter-domain Routing (CIDR)](https://www.rfc-editor.org/rfc/rfc4632)
- [RFC 4291 — IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291)
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918)
