# Supporting Concepts for Socket Programming

## 1. Blocking calls

A blocking call waits until it can make progress or an error/timeout occurs.

- `accept()` typically waits until a client connection arrives.
- `recv()` typically waits until data is available, the peer closes the connection, or an error occurs.
- A UDP `recvfrom()` waits for a datagram unless a timeout or non-blocking mode changes that behavior.

This is why a server can appear idle while it is waiting normally. A timeout can make some waits bounded, but it does not replace proper protocol design.

## 2. Threading and concurrent clients

A basic server that handles a client inline may not accept and process another client until the current handler finishes. A threaded server can give each accepted client its own thread so one client's wait does not block the main accept loop.

Threads introduce complexity: exceptions, shutdown, shared data, resource limits, and coordination must be considered. The included threaded server is a learning demonstration, not a production design.

## 3. Shared state and locks

If multiple threads read and modify the same mutable state, operations can interleave. For example, a shared active-client counter could be updated by several threads. A `threading.Lock()` lets a thread enter a critical section while excluding other threads using the same lock.

Keep the critical section short. Do not hold a lock while waiting on slow network I/O unless there is a specific reason.

## 4. The `with` statement and lock release

Using `with lock:` acquires the lock on entry and releases it when the block exits, including when an exception occurs. This is safer than manually acquiring a lock and then needing to remember every release path.

## 5. TCP `recv()` and application message framing

TCP exposes a continuous byte stream, not a sequence of application messages. If a sender calls `sendall()` once, the receiver's `recv()` may return only part of that data, or it may return data from more than one application-level write.

Applications define framing explicitly. Common approaches include:

- a delimiter, such as a newline, with rules for escaping delimiter characters;
- a fixed-size message;
- a length prefix followed by that many bytes.

The small TCP lab uses a short message and a single receive to keep the first experiment understandable. That simplification is not suitable for arbitrary or large messages.

## 6. Common socket errors

### Connection refused

Usually means no process is accepting connections at the target address and port, or a host/network device actively rejected the connection. Confirm that the server is running and the client uses the correct host, port, and protocol.

### Client/server mismatch

If the server is listening on one port while the client connects to another, the connection will not reach the intended listener. TCP and UDP are also separate protocol choices: a TCP client cannot communicate with a UDP server merely by using the same port number.

### Address already in use

Another process may already be bound to the address and port. Stop the duplicate server or choose a different port for both sides of the exercise. The TCP examples set `SO_REUSEADDR` to help with common restart behavior; it does not mean two active servers can freely own the same endpoint.

## Knowledge check

1. Why can `accept()` wait without indicating a bug?
2. What does a thread allow the server to do while another client handler is waiting?
3. Why might a shared counter need a lock?
4. What does `with lock:` do if an exception leaves the block?
5. Why must a TCP application define message framing?
6. What are the first things to check after “connection refused”?

## References

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Python threading documentation](https://docs.python.org/3/library/threading.html)
- [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
