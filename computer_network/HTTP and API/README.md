# HTTP and API Fundamentals

A structured reference to HTTP and introductory web API concepts covered in this learning milestone.

## HTTP

| Topic | Coverage |
|---|---|
| [HTTP Versions](./01-HTTP-Versions/README.md) | HTTP/1.1, HTTP/2, HTTP/3 and transport differences |
| [HTTP Methods](./02-HTTP-Methods/README.md) | Method semantics, safety and idempotency |
| [HTTP Status Codes](./03-HTTP-Status-Codes/README.md) | Status classes and common response codes |
| [HTTP Headers](./04-HTTP-Headers/README.md) | Request and response metadata |
| [Cookies](./05-Cookies/README.md) | Browser state and cookie attributes |
| [CORS](./06-CORS/README.md) | Browser cross-origin access policy |
| [HTTP Caching](./07-HTTP-Caching/README.md) | Freshness, validation and cache directives |

## API Fundamentals

| Topic | Coverage |
|---|---|
| [What Is an API?](./08-What-is-an-API/README.md) | Interfaces, contracts and client-provider interaction |
| [URL Structure](./09-URL-Structure/README.md) | Scheme, authority, path, query and fragment |
| [Path and Query Parameters](./10-Path-and-Query-Parameters/README.md) | Resource paths and request options |
| [Content Negotiation](./11-Content-Negotiation/README.md) | Selecting a representation through HTTP |

## Request Overview

A client sends an HTTP request containing a method, target, headers and, when applicable, a body. The server responds with a status code, headers and optionally a representation. An API defines the contract that gives this exchange application-specific meaning.

## Scope

This milestone covers HTTP fundamentals and introductory API request concepts. REST principles, resource modelling, URI design, endpoint naming, versioning, HATEOAS and other API-design topics remain separate learning items.
