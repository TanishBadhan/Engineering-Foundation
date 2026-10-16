# TCP Fundamentals

## 1. What TCP is

Transmission Control Protocol (TCP) is a transport-layer protocol that provides a reliable, ordered **byte stream** between applications communicating across a network. Applications use TCP when they need bytes to arrive in order and want the protocol to handle loss recovery.

Examples include many web connections, SSH sessions, and database connections.

## 2. Connection-oriented communication

TCP endpoints establish connection state before application data is exchanged. A connection is identified by endpoint information, including source and destination IP addresses and ports, alongside the protocol. “Connection-oriented” does not mean a dedicated physical path is reserved through the network.

## 3. The three-way handshake

A typical TCP connection begins with these steps:

1. **SYN:** the client asks to start a connection and communicates its initial sequence number.
2. **SYN-ACK:** the server acknowledges the client's SYN and sends its own SYN.
3. **ACK:** the client acknowledges the server's SYN.

After this exchange, both sides can begin sending application data. The handshake synchronizes sequence-number state and confirms that both endpoints can participate in the connection.

## 4. Reliable delivery

TCP uses sequence numbers, acknowledgements, timers, and retransmission to recover from packet loss and deliver a reliable stream to the application. The application normally does not have to implement packet-level retransmission itself.

Reliability does not mean a connection can never fail. A peer may disconnect, a network may become unavailable, or an application may stop responding. Applications still need sensible error handling.

## 5. Ordered delivery

TCP presents received bytes to an application in stream order. If later data arrives before an earlier missing segment, TCP can wait for the missing data to be recovered before delivering the ordered stream.

This is useful for applications that need a coherent sequence of bytes, but it can also mean later data waits behind lost earlier data.

## 6. Establishment and termination

The handshake establishes the connection. A graceful close commonly uses FIN and ACK exchanges as each side finishes sending. Each direction can be closed independently, so one endpoint may finish sending while still receiving data.

RST is used to reset/abort a connection in certain situations. Do not assume every connection ends with a neat four-message close; failures and resets can change the sequence.

## 7. Flow control

TCP flow control helps prevent a sender from overwhelming the receiving endpoint's available receive buffer. The receiver advertises a receive window that constrains how much unacknowledged data the sender may have in flight.

**Flow control is not congestion control.** Flow control protects the receiver; congestion control responds to conditions in the network.

## 8. TCP vs UDP

| Property | TCP | UDP |
|---|---|---|
| Communication model | Connection-oriented | Connectionless |
| Application abstraction | Ordered byte stream | Individual datagrams |
| Built-in reliable delivery | Yes, using acknowledgements and retransmissions | No |
| Ordering guarantee | Yes, for bytes delivered to the application | No |
| Message boundaries | Not preserved | Datagram boundaries are preserved |
| Typical fit | Web/API connections, SSH, database sessions | Real-time media, games, DNS and protocols built on UDP |

The right choice depends on application requirements. Some protocols built over UDP implement their own reliability and congestion-control mechanisms; QUIC is one example.

## Common misconceptions

- **“TCP sends messages.”** TCP sends a byte stream. Application message boundaries must be defined by the application protocol.
- **“One `sendall()` equals one `recv()`.”** There is no such guarantee. A receive may return fewer bytes than the application expects.
- **“TCP guarantees the application succeeds.”** TCP handles transport delivery while a connection is functioning; it cannot guarantee the remote application processed a request.
- **“UDP is always faster.”** UDP has less built-in machinery, but performance depends on the network and application design.
- **“HTTP/3 runs directly over TCP.”** HTTP/3 uses QUIC, which runs over UDP.

## Knowledge check

1. What does the three-way handshake establish?
2. Why is TCP called a byte stream rather than a message protocol?
3. How are flow control and congestion control different?
4. What does TCP do when data is lost?
5. Name a situation where UDP may be a better fit.

## References

- [RFC 9293 — Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 5681 — TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681)
- [Python socket documentation](https://docs.python.org/3/library/socket.html)
