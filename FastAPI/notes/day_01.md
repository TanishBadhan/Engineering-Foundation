# Day 01 — FastAPI Application Setup and Fundamentals

## Objective

Establish a working FastAPI development environment and understand
the basic structure of an HTTP application.

## Concepts Covered

### 1. FastAPI Application Instance

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()` creates the application instance. This instance is
used to register routes and configure application behavior.

### 2. Route Registration

A route connects an HTTP method and URL path to a Python function.

```python
@app.get("/api/posts")
def get_posts():
    return posts
```

When a client sends a GET request to `/api/posts`, FastAPI
executes the associated function.

### 3. HTTP Responses

FastAPI can return Python data structures that are converted
into JSON responses.

For HTML responses, `HTMLResponse` can be used:

```python
from fastapi.responses import HTMLResponse
```

The response class determines how the returned content is
interpreted by the client.

### 4. API Documentation

FastAPI automatically generates interactive API documentation.

- `/docs` — Swagger UI
- `/redoc` — ReDoc documentation

These interfaces help inspect and test registered API endpoints.

### 5. Development Environment

The project uses `uv` to manage dependencies and the Python
environment.

```bash
uv sync
uv run fastapi dev main.py
```

`uv sync` synchronizes the environment with the project
dependencies and lockfile.

The development command starts the application with automatic
reload support.

## Implementation

The application currently includes:

- A FastAPI application instance.
- A collection of sample posts stored in memory.
- HTML routes for the home and posts views.
- A JSON endpoint for retrieving posts.
- Automatically generated API documentation.

## Important Limitation

The posts collection is stored in memory.

Consequently:

- Data is not persisted in a database.
- Changes to the collection are lost when the process restarts.
- The current implementation is suitable for learning,
  not production data storage.

## Development and Debugging

The project was configured using `uv`.

The package structure was verified through a Python import test,
and the development server was started successfully.

The application endpoints were tested and returned successful
HTTP responses during development.

## Key Takeaways

- A route is an HTTP method and path mapped to a function.
- FastAPI uses decorators to register routes.
- JSON responses are useful for API clients.
- HTML responses are useful for browser-facing pages.
- The development server and API documentation simplify testing.
- Dependency management and application code should remain
  clearly separated.

## Next Steps

- Continue the tutorial and extend the existing application.
- Introduce request parameters and request validation.
- Improve the posts endpoint.
- Add automated tests as the application becomes more complex.

## Reflection

The goal is not merely to reproduce tutorial code. Each concept
should be understood well enough to explain its purpose,
behavior, and limitations independently.
