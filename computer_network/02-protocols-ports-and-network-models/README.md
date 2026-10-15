# Protocols, Ports, Network Models, and Encapsulation

This note explains how network communication is organized: protocols define rules, ports identify application endpoints on a host, network models divide responsibilities into layers, and encapsulation wraps data with the information each layer needs.

## 1. Protocols: shared rules for communication

A **protocol** is an agreed set of rules for how communicating systems format, send, receive, and interpret information.

Examples:
- **IP** handles addressing and forwarding packets between networks.
- **TCP** provides a reliable, ordered byte stream between endpoints.
- **UDP** sends independent datagrams without TCP's delivery guarantees.
- **DNS** helps resolve domain names to records such as IP addresses.
- **HTTP** defines request and response semantics for web communication.
- **TLS** provides encryption and peer authentication when correctly configured.

Protocols solve different problems. HTTP does not replace TCP or IP; they operate at different layers and cooperate.

## 2. IP addresses and ports answer different questions

An **IP address** identifies a network interface's address for IP communication. A **port number** identifies a transport-layer endpoint on a host.

A useful simplified model:
- IP address: which host/interface should receive the packet?
- Port: which application endpoint should receive the transport data?

For example, a client might connect to `203.0.113.10:443`: the IP address identifies the destination address, while port `443` conventionally serves HTTPS traffic. `203.0.113.0/24` is reserved for documentation and is not an example of a real public server.

Ports range from `0` through `65535`. The commonly used ranges are:
- **System ports:** `0–1023`
- **User ports:** `1024–49151`
- **Dynamic/private ports:** `49152–65535`

These ranges describe IANA port assignments; actual operating-system behavior and service configuration can vary. A familiar port number is a convention, not proof of which service is running there.

A TCP connection is commonly identified by its source IP, source port, destination IP, and destination port, together with the transport protocol. UDP communication also uses source and destination addressing information, but it does not establish a TCP-style connection.

## 3. The OSI model

The **OSI model** is a seven-layer reference model. It is useful for organizing responsibilities and troubleshooting, but real implementations do not always map neatly to one layer.

| Layer | Name | Main responsibility | Examples or concepts |
|---|---|---|---|
| 7 | Application | Network-facing services and application protocols | HTTP, DNS |
| 6 | Presentation | Data representation, encoding, and transformation | Character encoding, serialization |
| 5 | Session | Managing dialog/session concepts | Session coordination |
| 4 | Transport | Communication between application endpoints | TCP, UDP, ports |
| 3 | Network | Logical addressing and routing between networks | IP, routers |
| 2 | Data Link | Delivery over a local link and framing | Ethernet, Wi-Fi, MAC addresses |
| 1 | Physical | Signaling and transmission of bits | Radio, copper, fiber |

The OSI model is a learning and diagnostic framework, not a requirement that every protocol implement a separate layer.

## 4. The TCP/IP model

The TCP/IP model groups the real-world Internet protocol suite into fewer layers. A common four-layer version is:

| TCP/IP layer | Main responsibility | Examples |
|---|---|---|
| Application | Application-level communication and data formats | HTTP, DNS, SSH |
| Transport | Process-to-process communication | TCP, UDP |
| Internet | Addressing and routing across networks | IP, ICMP |
| Link / Network access | Communication on the local network and physical transmission | Ethernet, Wi-Fi |

Some curricula use a five-layer teaching model by separating the link and physical responsibilities. The names and exact grouping can vary; focus on each layer's job.

## 5. Encapsulation and decapsulation

As data travels down the network stack, each layer adds information needed by its peer layer at the receiver. This is called **encapsulation**. The receiver processes the headers in reverse order; this is called **decapsulation**.

A simplified web-request path:
1. The HTTP layer creates request data.
2. TCP may add a TCP header, producing a TCP segment.
3. IP adds an IP header, producing an IP packet.
4. The link layer adds its frame information for the local link.
5. The receiver processes the link, IP, and transport information, then passes the application data upward.

The names *segment*, *packet*, and *frame* are common terms for data units at different layers. Terminology can vary by protocol and context.

Conceptual view:

```text
Application data
      ↓ TCP header added
[TCP header | Application data]
      ↓ IP header added
[IP header | TCP header | Application data]
      ↓ Link-layer framing
[Link header | IP header | TCP header | Application data | Link trailer]
```

This is a conceptual diagram, not a byte-accurate format for every network. Headers and trailers differ by protocol, and segmentation, fragmentation, tunneling, or offloading can change what is observed at a particular point.

## 6. How the layers cooperate

When a browser sends an HTTPS request, several protocols cooperate rather than one protocol doing everything:
- DNS may resolve the hostname.
- IP routes packets toward the destination.
- TCP commonly provides the transport connection for HTTP/1.1 and HTTP/2.
- TLS protects the application communication.
- HTTP defines the request and response semantics.
- Link-layer protocols carry frames across each local link.

HTTP/3 is an important exception to the common TCP-based path: it uses QUIC over UDP. Therefore, do not assume all HTTPS traffic uses TCP.

## 7. Backend engineering relevance

These concepts help you:
- Distinguish a routing/addressing issue from a port or application-listener issue.
- Understand why a service can be reachable by IP but fail by hostname.
- Interpret connection errors and packet captures without treating all networking failures as equivalent.
- Understand why a server listening on one port does not automatically mean the application protocol is healthy.
- Follow a request across application, transport, network, and link responsibilities.

## 8. Common misconceptions

- **“An IP address and a port are the same thing.”** They identify different parts of a destination.
- **“Port 443 guarantees HTTPS.”** It is a convention; the actual service must be verified.
- **“Each OSI layer is a separate physical device.”** Layers describe responsibilities, not necessarily separate hardware.
- **“HTTP is the same layer as IP.”** They solve different problems at different levels.
- **“Every HTTPS request uses TCP.”** HTTP/3 uses QUIC over UDP.
- **“Encapsulation means encrypting data.”** Encapsulation adds protocol information; encryption is a separate security operation.

## 9. Knowledge check

Try answering these without looking at the note:
1. What question does an IP address answer, and what question does a port answer?
2. Why can two applications on one host use different ports?
3. What responsibility does TCP have that IP does not provide by itself?
4. What is the purpose of encapsulation?
5. Name the seven OSI layers in order.
6. Give one example of a protocol commonly associated with the application, transport, and internet layers.
7. Why is it incorrect to assume that all HTTPS traffic uses TCP?
8. A server's IP responds, but a connection to the expected port fails. Name two plausible causes.

## 10. References

- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 9293 — Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 — User Datagram Protocol (UDP)](https://www.rfc-editor.org/rfc/rfc768)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 9000 — QUIC: A UDP-Based Multiplexed and Secure Transport](https://www.rfc-editor.org/rfc/rfc9000)
- [IANA Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

---

**Completion note:** This document records the concepts studied. Mark the stage as complete only after you can answer the knowledge checks and explain the responsibilities of the layers in your own words.
