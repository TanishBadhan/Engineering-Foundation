# Content Negotiation

Content negotiation is the process by which a client and server select a suitable representation of a resource.

## Common Headers

| Header | Purpose |
|---|---|
| Accept | Media types the client can process |
| Content-Type | Media type of the representation in the current message |
| Accept-Language | Preferred natural languages |
| Accept-Encoding | Acceptable content codings, such as compression |

## Example

Request:

```http
GET /products/42 HTTP/1.1
Host: api.example.com
Accept: application/json
```

A JSON response commonly includes:

```http
Content-Type: application/json
```

## Important Distinctions

- `Accept` describes what the client wants in the response.
- `Content-Type` describes the body being sent, whether in a request or response.
- `Content-Encoding` describes a coding applied to the representation, such as gzip; it is not the media type.

If no acceptable response representation is available, a server may return **406 Not Acceptable**. If the request body uses a format the server cannot process, **415 Unsupported Media Type** may be appropriate.

Negotiation behavior depends on the server and API contract. Sending an Accept header does not guarantee that every server supports every requested representation.

## Key Takeaway

Content negotiation lets clients express representation preferences while servers select an available format. Correctly distinguishing Accept, Content-Type and Content-Encoding is essential when debugging HTTP responses.
