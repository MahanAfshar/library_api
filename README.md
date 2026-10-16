# Library API

A simple RESTful API for managing books, built with **FastAPI** and **Pydantic**. Data is stored in memory.

## Features

- Create, read, update, and delete books (CRUD)
- Request validation using Pydantic
- HTTP status codes and error handling
- Automatic API documentation

## Installation & Run

```bash
uv sync
uv run uvicorn library_api.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Get all books |
| GET | `/books/{book_id}` | Get a book |
| POST | `/books` | Create a book |
| PATCH | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## API Documentation

After starting the server, visit:

- Swagger UI: http://localhost:8000/docs

**Note:** Data is stored in memory and resets when the application restarts.