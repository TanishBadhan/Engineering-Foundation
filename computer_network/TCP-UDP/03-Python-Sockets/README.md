# Python Socket Labs

These small programs demonstrate TCP streams, UDP datagrams, and the basic client/server call sequence using Python's standard library.

## Prerequisites

- Python 3 installed and available as `python` (on some systems, use `python3`).
- Two terminal sessions for running a server and its client.
- Basic familiarity with functions, exceptions, and imports.

Run commands from the repository root unless a section says otherwise.

## Labs

- [TCP client and server](tcp/README.md): `bind()`, `listen()`, `accept()`, `connect()`, `sendall()`, and `recv()`.
- [UDP client and server](udp/README.md): `SOCK_DGRAM`, `sendto()`, and `recvfrom()`.
- [Supporting concepts](supporting-concepts.md): blocking calls, threads, shared state, TCP message framing, and common errors.

## Suggested workflow

1. Read the relevant lab README before running code.
2. Start the server in terminal 1.
3. Start the client in terminal 2.
4. Compare the observed output with the expected behavior.
5. Change one variable or one line, predict the outcome, and test the prediction.
6. Stop long-running servers with Ctrl+C.

## Scope

The examples are for local learning, not production use. They bind to `127.0.0.1` by default. They intentionally omit many production concerns, including authentication, robust protocol framing, resource limits, and structured logging.
