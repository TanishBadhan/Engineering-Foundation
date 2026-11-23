# HTTP Versions

HTTP is an application-layer protocol for exchanging requests and responses. Its versions preserve HTTP semantics while evolving message framing and transport.

## Version Comparison

| Version | Main characteristics |
|---|---|
| HTTP/1.0 | Early web protocol; commonly used separate connections for requests |
| HTTP/1.1 | Persistent connections by default and standardized host handling |
| HTTP/2 | Binary framing, multiplexed streams and header compression over TCP |
| HTTP/3 | HTTP over QUIC, which runs over UDP |

## Important Distinctions

- HTTP defines application-level request and response semantics.
- TCP is the transport commonly used by HTTP/1.1 and HTTP/2.
- QUIC provides transport features for HTTP/3 over UDP.
- HTTPS means HTTP protected with TLS; it is not an HTTP version.

HTTP/2 multiplexes multiple streams over one TCP connection. HTTP/3 avoids TCP-level head-of-line blocking between its QUIC streams.

## Key Takeaway

HTTP version and transport protocol are related, but they are not interchangeable concepts. HTTP/3 uses QUIC; it does not mean every version of HTTP uses UDP.
