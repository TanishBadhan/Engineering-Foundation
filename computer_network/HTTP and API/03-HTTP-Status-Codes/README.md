# HTTP Status Codes

An HTTP status code communicates the result of a request. Interpret it together with the response headers and body, which often provide the specific explanation.

## Status Classes

| Class | Meaning |
|---|---|
| 1xx | Informational |
| 2xx | Successful request |
| 3xx | Redirection or further action |
| 4xx | Client request issue |
| 5xx | Server or upstream failure |

## Common Codes

| Code | Meaning | Typical context |
|---|---|---|
| 200 | OK | Successful request |
| 201 | Created | Resource created |
| 202 | Accepted | Processing accepted, not necessarily complete |
| 204 | No Content | Success without a response body |
| 301 / 302 | Redirect | Request redirected |
| 304 | Not Modified | Cached representation remains valid |
| 400 | Bad Request | Invalid request or input |
| 401 | Unauthorized | Authentication is missing or invalid |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Target resource not found |
| 405 | Method Not Allowed | Method unsupported for the target |
| 409 | Conflict | Request conflicts with current state |
| 415 | Unsupported Media Type | Request representation format is unsupported |
| 422 | Unprocessable Content | Content understood but cannot be processed |
| 429 | Too Many Requests | Rate limit reached |
| 500 | Internal Server Error | Unexpected server failure |
| 502 / 503 / 504 | Gateway error / unavailable / timeout | Proxy or upstream issue |

## Important Distinctions

- **401 vs. 403:** authentication and authorization are different. A 401 indicates an authentication challenge or failure; 403 indicates the server refuses the request.
- **404:** does not always reveal whether a resource never existed or is intentionally hidden.
- **202 vs. 200:** accepted processing may still be ongoing after a 202 response.
- **304:** supports cache validation and is not a typical response containing a new representation body.

## Key Takeaway

Status codes provide a standardized summary of request outcome. Robust clients should handle expected codes deliberately rather than treating every non-200 response as the same error.
