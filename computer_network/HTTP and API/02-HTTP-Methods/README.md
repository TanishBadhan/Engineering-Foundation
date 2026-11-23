# HTTP Methods

HTTP methods define the intended action of a request. They communicate how a client wants to interact with a resource and influence how the server processes the request.

## Common Methods

| Method | Purpose | Safe | Idempotent |
|---|---|---|---|
| GET | Retrieve a resource | Yes | Yes |
| HEAD | Retrieve headers without the response body | Yes | Yes |
| POST | Submit data or trigger processing | No | Not inherently |
| PUT | Create or replace a resource | No | Yes |
| PATCH | Apply partial modifications | No | Not inherently |
| DELETE | Remove a resource's association | No | Yes |
| OPTIONS | Identify supported communication options | Yes | Yes |

## Method Semantics

**Safe methods** do not request a change to the server's state. They are primarily used to retrieve information.

**Idempotent methods** have the same intended effect when repeated. The response itself does not have to remain identical.

### GET and HEAD

GET requests a representation of a resource. It should not be used to perform operations that intentionally modify server state.

HEAD behaves like GET, but the server does not return the response body. It is useful when a client needs response metadata without downloading the representation.

### POST

POST submits data to a resource for processing. Common uses include creating a resource when the server assigns its identifier, submitting form data, or initiating a resource-specific operation.

### PUT

PUT creates or replaces the state of a resource at the target URI. Repeating the same PUT request should have the same intended effect.

### PATCH

PATCH applies partial modifications to a resource. Its idempotency depends on the patch operation and API implementation.

### DELETE

DELETE requests removal of a resource's association. Successful deletion does not necessarily mean every underlying record or historical copy has been physically erased.

## Practical Usage

- Use GET for retrieval.
- Use POST for submission or processing.
- Use PUT for replacement.
- Use PATCH for partial updates.
- Use DELETE for removal.
- Use HEAD when only response metadata is required.
- Use OPTIONS to inspect communication options.

## Key Takeaway

HTTP methods are not interchangeable. Their semantics affect API design, caching, retries and client behavior. POST and PATCH are not inherently idempotent; an application may provide additional safeguards for particular operations.
