# What Is an API?

An **Application Programming Interface (API)** is a defined interface and contract that allows one software component to interact with another.

An API describes available operations, inputs, outputs, rules and expected errors. A consumer can use the provider without needing to understand its internal implementation.

## Web API Request Model

1. The client constructs a request to an endpoint.
2. The request includes an HTTP method, URL, headers and sometimes a body.
3. The server validates and processes the request.
4. The server returns an HTTP status, headers and often a representation.

The API contract determines how the request is interpreted and what the response means.

## APIs Are Not Limited to HTTP

APIs can be exposed through libraries, operating-system interfaces, RPC systems, messaging and web protocols. A web API is one category of API, not the definition of every API.

## Why APIs Matter

- Separate frontend and backend responsibilities.
- Enable systems to integrate without sharing implementation details.
- Define boundaries between services and teams.
- Make behavior testable through explicit inputs and outputs.

An endpoint is one addressable part of an API; it is not synonymous with the entire API.

## Key Takeaway

An API is a contract between software components. HTTP supplies request/response mechanics for HTTP APIs, while the API contract defines the application-level behavior.
