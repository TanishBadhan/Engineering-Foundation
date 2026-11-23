# HTTP Caching

HTTP caching stores reusable response representations to reduce latency, network traffic and server work. Cache behavior depends on request and response directives, freshness information and validators.

## Common Cache-Control Directives

| Directive | Meaning |
|---|---|
| `max-age` | Response is fresh for the specified number of seconds |
| `no-cache` | Validate before reusing a stored response |
| `no-store` | Do not store the response |
| `public` | Shared caches may store the response, subject to other rules |
| `private` | Intended for private caches rather than shared caches |

## Freshness and Validation

**Freshness** determines whether a stored response can be reused without contacting the origin.

**Validation** checks whether a stored representation is still current. A server may provide an ETag validator; a later request can include `If-None-Match`.

- If the representation has not changed, the server can return **304 Not Modified**.
- If it has changed, the server returns the updated representation, commonly with a 200 response.

## Important Distinction

`no-cache` does not mean “never store.” It means a stored response must be validated before reuse. `no-store` is the directive that prohibits storage.

For authenticated or user-specific responses, understand private/shared cache rules and cache keys before enabling caching.

## Key Takeaway

Caching can improve performance substantially, but incorrect cache policy can expose stale or user-specific data. Choose directives according to the sensitivity and update behavior of the representation.
