<!-- # Library API

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

**Note:** Data is stored in memory and resets when the application restarts. -->







# Library API

A simple RESTful API for managing books, built with **FastAPI**, **Pydantic**, and **PostgreSQL**.

## Features

- Create, read, update, and delete books (CRUD)
- Request validation using Pydantic
- PostgreSQL database integration
- HTTP status codes and error handling
- Automatic API documentation

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- uv
- PostgreSQL

You must have a running PostgreSQL server and a database configured for the application.

## Installation & Setup

### 1. Install Dependencies

Install the project dependencies using `uv`:

```bash
uv sync
```

### 2. Configure Environment Variables

Rename the `.env.example` file to `.env`.

Open the `.env` file and set `DATABASE_URL` to match your PostgreSQL configuration:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/library_db
```

Update the connection URL with your own PostgreSQL credentials and database details:

- `postgres`: Your PostgreSQL username
- `password`: Your PostgreSQL password
- `localhost`: Your PostgreSQL server host
- `5432`: Your PostgreSQL port
- `library_db`: Your database name

**Note:** Make sure the `library_db` database exists before starting the application, unless your application creates it automatically.

### 3. Run the Application

Start the application using the following command:

```bash
uv run uvicorn library_api.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Get all books |
| GET | `/books/{book_id}` | Get a book by ID |
| POST | `/books` | Create a new book |
| PATCH | `/books/{book_id}` | Update an existing book |
| DELETE | `/books/{book_id}` | Delete a book |

## API Documentation

After starting the server, access the interactive API documentation using the following URL:

- **Swagger UI:** http://localhost:8000/docs

## Important Notes

- PostgreSQL must be installed and running before starting the application.
- Make sure your `.env` file contains the correct `DATABASE_URL`.
- The `.env.example` file serves as a template for configuring environment variables.
- Ensure the `library_db` database exists before running the application.
- The `--reload` option automatically restarts the server when code changes are detected. It is intended for development.