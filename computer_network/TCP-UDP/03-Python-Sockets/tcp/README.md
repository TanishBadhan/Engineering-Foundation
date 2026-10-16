# TCP Socket Lab

This lab uses a TCP server and client on the loopback interface.

## Run the basic example

From the repository root, open two terminals.

**Terminal 1 — server**

```bash
python computer_network/TCP-UDP/03-Python-Sockets/tcp/server.py
```

**Terminal 2 — client**

```bash
python computer_network/TCP-UDP/03-Python-Sockets/tcp/client.py
```

The server listens on `127.0.0.1:50000`, accepts one client, prints the received text, and replies. The client connects, sends a short message, then prints the server's reply.

## Call sequence

- `socket.socket(AF_INET, SOCK_STREAM)`: create an IPv4 TCP socket.
- `bind((HOST, PORT))`: associate the server socket with a local address.
- `listen()`: mark the socket as ready to accept incoming connections.
- `accept()`: wait for a client and return a new connected socket plus the peer address.
- `connect((HOST, PORT))`: ask the client socket to establish a connection.
- `sendall(data)`: keep sending until the supplied bytes have been sent or an error occurs.
- `recv(size)`: return up to the requested number of bytes; it may return fewer than expected.

## Try Netcat (optional)

If Netcat is installed, start the server and run this in another terminal:

```bash
nc 127.0.0.1 50000
```

Type a line and press Enter. The basic server accepts one connection and reads once, so restart the server before testing another connection. Netcat options vary by platform.

## Try concurrent clients

Run `threaded_server.py` instead of `server.py`. It starts a separate thread for each accepted client and tracks the active-client count under a lock. This is a teaching example, not a production concurrency model.

```bash
python computer_network/TCP-UDP/03-Python-Sockets/tcp/threaded_server.py
```

Run the client from multiple terminals to observe concurrent handling. Stop the server with Ctrl+C.

## Troubleshooting

- **Connection refused:** make sure the server is running and the host/port match.
- **Address already in use:** stop the earlier server instance, or wait for the port to become available.
- **Client appears to wait:** `accept()` waits for a client; `recv()` waits for data or connection activity. Check which side is waiting.
- **No response or unexpected output:** confirm both programs use the same port and compatible protocol.

## Limitations

TCP is a byte stream. This lab deliberately sends one short message and reads once for simplicity; real protocols need explicit message framing, such as a delimiter or length prefix, and must handle partial reads and disconnects.
