# TCP and UDP

This module covers transport-layer fundamentals and small Python socket experiments. Work through the theory first, then run the labs locally and explain the observed behavior in your own words.

## Learning checklist

### TCP fundamentals

- [ ] Explain what TCP is and why it is used.
- [ ] Explain connection-oriented communication.
- [ ] Trace the three-way handshake: SYN → SYN-ACK → ACK.
- [ ] Explain reliable delivery through acknowledgements and retransmissions.
- [ ] Explain ordered delivery.
- [ ] Describe connection establishment and termination at a high level.
- [ ] Explain the purpose of TCP flow control.
- [ ] Compare TCP and UDP.

See [TCP notes](01-TCP/README.md).

### UDP fundamentals

- [ ] Explain what UDP is and why it is used.
- [ ] Explain connectionless communication.
- [ ] Explain datagrams and message boundaries.
- [ ] Explain the lack of built-in delivery, ordering, and retransmission guarantees.
- [ ] Compare TCP and UDP use cases and trade-offs.

See [UDP notes](02-UDP/README.md).

### Python socket programming

- [ ] Use `socket.socket()` and distinguish TCP and UDP socket types.
- [ ] Explain a TCP server's `bind()`, `listen()`, and `accept()` calls.
- [ ] Explain a TCP client's `connect()` call.
- [ ] Send and receive data with `sendall()` and `recv()`.
- [ ] Exchange UDP datagrams with `sendto()` and `recvfrom()`.
- [ ] Identify the IP address and port in a socket address tuple.
- [ ] Run a server and client in separate terminal sessions.
- [ ] Test a TCP server with Netcat when it is installed.
- [ ] Explain the request-and-reply flow between client and server.

Start at the [Python socket lab index](03-Python-Sockets/README.md).

### Supporting concepts

- [ ] Explain why blocking calls such as `accept()` and `recv()` can wait.
- [ ] Explain how threads can handle multiple clients concurrently.
- [ ] Explain shared state and when a `threading.Lock()` is needed.
- [ ] Explain how `with` ensures a lock is released after its block.
- [ ] Explain why one TCP `recv()` does not necessarily return one complete application message.
- [ ] Recognize connection-refused errors and client/server configuration mismatches.

See [supporting concepts](03-Python-Sockets/supporting-concepts.md).

## Recommended workflow

1. Read the TCP notes and answer the knowledge checks without looking.
2. Read the UDP notes and compare the guarantees and trade-offs.
3. Run the TCP server and client in separate terminals.
4. Run the threaded TCP server and connect more than one client.
5. Run the UDP server and client.
6. Change one small thing at a time, predict the result, then test it.
7. Mark a checklist item complete only when you can explain it and demonstrate it.

## Completion criteria

You should be able to explain the difference between a reliable byte stream and datagrams, trace the basic client/server call sequence, run the examples, and diagnose the common local errors described in the notes.

## Safety and scope

These scripts are deliberately small learning examples, not production-ready servers. They bind to the loopback address `127.0.0.1` so they accept local connections only by default. Do not expose them to a public network without understanding authentication, input handling, resource limits, concurrency, and operational security.

## References

- [RFC 9293 — Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 — User Datagram Protocol (UDP)](https://www.rfc-editor.org/rfc/rfc768)
- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Python threading documentation](https://docs.python.org/3/library/threading.html)
