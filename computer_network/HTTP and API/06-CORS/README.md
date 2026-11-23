# Cross-Origin Resource Sharing (CORS)

CORS is a browser mechanism that uses HTTP headers to determine whether a webpage may access a response from a different origin.

An **origin** is the combination of scheme, host and port. A different port or scheme creates a different origin.

## How CORS Works

1. The browser identifies a cross-origin request.
2. For requests that require preflight, it sends an OPTIONS request describing the intended method and headers.
3. The server responds with CORS policy headers.
4. The browser enforces whether frontend JavaScript may access the response.

## Common Response Headers

| Header | Purpose |
|---|---|
| Access-Control-Allow-Origin | Allowed origin or origins policy |
| Access-Control-Allow-Methods | Methods allowed for the cross-origin request |
| Access-Control-Allow-Headers | Request headers allowed by the server |
| Access-Control-Allow-Credentials | Whether credentials may be included |

## What CORS Does Not Do

- It is not authentication or authorization.
- It is not a general server-to-server access-control mechanism.
- It does not guarantee that a cross-origin request never reaches the server.

## Troubleshooting

A browser CORS error often means the response did not satisfy the browser's access policy. It does not automatically mean the API is offline. Check the request origin, preflight response and relevant CORS headers.

## Key Takeaway

CORS is enforced by browsers to control frontend access to cross-origin responses. The server must return an appropriate policy, and that policy should be configured deliberately rather than opened broadly without reason.
