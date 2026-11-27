# FastAPI Blog Application

A tutorial-driven backend application developed while learning
FastAPI and Python backend engineering.

The application will evolve incrementally as new concepts are
introduced throughout the learning process.

## Technology Stack

- Python
- FastAPI
- Uvicorn
- uv for dependency and environment management

## Prerequisites

- Python version specified in `.python-version`
- uv installed
- Git

## Setup

From the application directory:

```bash
uv sync
```

## Run the Development Server

```bash
uv run fastapi dev main.py
```

The development server provides automatic reload during development.

## Available Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Application home |
| GET | `/posts` | HTML posts view |
| GET | `/api/posts` | Retrieve posts as JSON |
| GET | `/docs` | Interactive API documentation |

## Development Notes

The application currently uses an in-memory collection of posts.
Persistent database storage, authentication, validation, and
additional backend features will be introduced as the learning
progresses.

This is a learning application, not yet a production deployment.
