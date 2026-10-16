# UDP Socket Lab

This lab exchanges one UDP datagram from a client to a local server, then sends a reply datagram.

## Run the example

From the repository root, open two terminals.

**Terminal 1 — server**

```bash
python computer_network/TCP-UDP/03-Python-Sockets/udp/server.py
```

**Terminal 2 — client**

```bash
python computer_network/TCP-UDP/03-Python-Sockets/udp/client.py
```

The server binds to `127.0.0.1:50001` and waits for datagrams. The client sends one datagram and waits up to three seconds for a reply.

## Important calls

- `socket.socket(AF_INET, SOCK_DGRAM)`: create an IPv4 UDP socket.
- `bind((HOST, PORT))`: associate the server socket with a local address.
- `sendto(data, address)`: send one datagram to the destination address.
- `recvfrom(size)`: receive one datagram and return its data and sender address.

## What to observe

UDP preserves datagram boundaries, but the protocol does not guarantee delivery, ordering, or retransmission. The client timeout is a local way to avoid waiting forever for a reply; it does not make UDP reliable.

## Troubleshooting

- **No reply before timeout:** check that the server is running and both programs use the same port.
- **Address already in use:** stop another process using the same local port.
- **Unexpected response:** verify that you are running the intended server and client scripts.

## Limitations

This is a small local exercise. Real applications may need message validation, retry policies, duplicate handling, congestion-aware behavior, and security controls.
