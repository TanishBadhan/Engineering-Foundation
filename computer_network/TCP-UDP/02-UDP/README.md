# UDP Fundamentals

## 1. What UDP is

User Datagram Protocol (UDP) is a transport-layer protocol that sends independent datagrams between applications. It has a small protocol header and does not establish a TCP-style connection before sending data.

UDP is useful when an application wants datagram semantics, low protocol overhead, or needs to implement its own delivery behavior. Examples include DNS queries, some real-time media and game traffic, and transport protocols such as QUIC.

## 2. Connectionless communication

UDP does not establish a transport connection with a handshake and does not maintain TCP-style connection state. A sender can transmit a datagram to a destination address without first performing a connection handshake.

Some socket APIs allow `connect()` to be called on a UDP socket. This sets a default peer for that socket and may filter which peer can send datagrams to it, but it does **not** add TCP-style reliability, ordering, or retransmission.

## 3. Datagrams and message boundaries

UDP preserves datagram boundaries. If an application sends one datagram, the receiving socket reads it as a datagram rather than as an arbitrary segment of a continuous byte stream.

The receiving application must provide a buffer large enough for the datagram it expects. If the buffer is too small, excess datagram data may be truncated; it is not returned later as the remainder of the same datagram.

## 4. What UDP does not guarantee

UDP itself does not guarantee:

- that a datagram will arrive;
- that datagrams will arrive in sending order;
- that a datagram will be retransmitted if lost;
- that duplicates will be suppressed;
- that the remote application has processed a datagram.

Datagrams may be lost, duplicated, delayed, or reordered. Applications that require stronger guarantees must implement appropriate mechanisms or use a protocol that provides them.

## 5. TCP and UDP: trade-offs

Choose based on application needs, not a blanket claim that one protocol is better.

| Requirement | Possible fit | Reason |
|---|---|---|
| Reliable ordered stream of bytes | TCP | Built-in delivery and ordering mechanisms |
| Independent messages with boundaries | UDP | Each datagram is a separate unit |
| Real-time data where late delivery may be less useful than timely delivery | Often UDP-based designs | Application can choose how to handle loss and delay |
| Reliable modern transport over UDP | QUIC | Adds transport features above UDP |

UDP does not automatically make an application fast or suitable for real-time use. The application and network conditions still matter, and reliable UDP-based protocols need their own careful design.

## Common misconceptions

- **“Connectionless means no addresses are used.”** Each datagram still has source and destination addressing at the network/transport layers.
- **“UDP preserves datagrams, so they always arrive.”** Boundary preservation applies to datagrams that are received, not to delivery guarantees.
- **“Calling `connect()` makes UDP reliable.”** It does not.
- **“UDP has no congestion concerns.”** Applications still need to behave responsibly on congested networks; protocols built on UDP may implement congestion control.

## Knowledge check

1. What is the key difference between a TCP byte stream and UDP datagrams?
2. What guarantees does UDP provide about delivery and ordering?
3. What does `connect()` on a UDP socket change, and what does it not change?
4. What can happen if the receive buffer is too small?
5. Why might an application choose UDP despite the lack of built-in reliability?

## References

- [RFC 768 — User Datagram Protocol (UDP)](https://www.rfc-editor.org/rfc/rfc768)
- [RFC 9000 — QUIC: A UDP-Based Multiplexed and Secure Transport](https://www.rfc-editor.org/rfc/rfc9000)
- [Python socket documentation](https://docs.python.org/3/library/socket.html)
