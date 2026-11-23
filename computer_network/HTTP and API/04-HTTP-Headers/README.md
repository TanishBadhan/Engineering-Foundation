# HTTP Headers

HTTP headers carry metadata about a request or response. They are expressed as field names and values and are distinct from the message body.

## Common Request Headers

| Header | Purpose |
|---|---|
| Host | Identifies the target host in HTTP/1.1 |
| Accept | Media types the client can process |
| Content-Type | Format of the message body being sent |
| Authorization | Authentication or authorization credentials |
| User-Agent | Identifies client software |
| Cookie | Sends applicable stored cookies |
| Cache-Control | Cache directives |

## Common Response Headers

| Header | Purpose |
|---|---|
| Content-Type | Media type of the response representation |
| Content-Length | Body length when applicable |
| Location | Redirect target or location of a created resource |
| Set-Cookie | Instructs the user agent to store a cookie |
| ETag | Representation validator |
| Cache-Control | Response caching policy |
| Access-Control-Allow-Origin | CORS policy response |

## Accept and Content-Type

- **Accept** describes which response media types the client is willing to receive.
- **Content-Type** describes the representation in the current message, whether request or response.
- **Content-Encoding** describes a coding applied to the representation, such as gzip.

## Key Takeaway

Headers help clients and servers interpret message content and control behavior such as authentication, caching and cross-origin access. Do not assume that a header is secret simply because it is metadata.
