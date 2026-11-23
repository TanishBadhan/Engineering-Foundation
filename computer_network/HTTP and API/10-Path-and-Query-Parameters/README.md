# Path and Query Parameters

Path and query parameters both appear in URLs, but they commonly express different kinds of information.

## Path Parameters

A path parameter is part of the URL path and commonly identifies a specific resource.

Example:

`GET /users/42`

Here, `42` identifies the user addressed by this route.

## Query Parameters

Query parameters follow `?` and commonly filter, sort, paginate or modify how a representation is returned.

Example:

`GET /users?role=admin&page=2`

Here, `role` and `page` are query parameters.

## Comparison

| Path parameters | Query parameters |
|---|---|
| Commonly identify the target resource | Commonly filter or shape the requested result |
| Part of the URL path | Begin after `?` |
| Example: `/users/42` | Example: `?page=2&limit=20` |

These are common API design conventions, not strict rules imposed by HTTP. The API contract defines how each parameter is interpreted.

## Encoding and Practical Notes

- Encode values when they contain reserved characters or spaces.
- Query parameters are commonly separated by `&`; key/value pairs commonly use `=`.
- APIs may accept repeated keys, such as `?tag=a&tag=b`; behavior depends on the contract.
- Do not place secrets in query strings because URLs may appear in logs, browser history and referrer data.

## Key Takeaway

Path parameters commonly address a resource; query parameters commonly refine a request. Always follow the endpoint's documented contract.
