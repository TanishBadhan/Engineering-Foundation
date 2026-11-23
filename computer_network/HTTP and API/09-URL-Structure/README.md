# URL Structure

A URL (Uniform Resource Locator) identifies a resource and describes how to locate it.

## Example

`https://api.example.com:443/v1/users/42?include=posts#profile`

| Component | Example | Purpose |
|---|---|---|
| Scheme | `https` | Protocol scheme |
| Host | `api.example.com` | Hostname |
| Port | `443` | Optional explicit port |
| Path | `/v1/users/42` | Resource path |
| Query | `?include=posts` | Query parameters |
| Fragment | `#profile` | Client-side or document location identifier |

The authority generally contains the host and optional port. In ordinary API URLs, credentials should not be embedded in the URL.

## URI and URL

URI is the broader identifier term. A URL identifies a resource by describing its location or access mechanism. In everyday API documentation, URL is commonly used for the complete request address.

## Practical Considerations

- Encode reserved characters when they are data rather than URL delimiters.
- Fragments are not included in the HTTP request target sent to the server.
- HTTPS protects the connection; it does not make every endpoint or returned value trustworthy.
- Avoid putting secrets in URLs because they may appear in logs, browser history or referrer data.

## Key Takeaway

Understanding URL components helps you read API endpoints, distinguish path from query data and debug requests accurately.
