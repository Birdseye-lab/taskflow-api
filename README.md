# TaskFlow API

A production-oriented REST API for task management built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, **Docker**, and **Pytest**.

TaskFlow provides a clean backend architecture for creating, retrieving, updating, and deleting tasks, with database migrations, automated tests, and containerized development.

## Features

* RESTful API built with FastAPI
* PostgreSQL database
* SQLAlchemy ORM
* Alembic database migrations
* CRUD operations for tasks
* Automatic API documentation with Swagger UI
* Automated tests with Pytest
* Docker containerization
* Docker Compose for API + PostgreSQL
* PostgreSQL healthcheck
* Environment-based configuration
* Git-based version control

## Tech Stack

| Technology     | Purpose                     |
| -------------- | --------------------------- |
| Python 3.13    | Programming language        |
| FastAPI        | Web framework               |
| Uvicorn        | ASGI server                 |
| PostgreSQL 18  | Relational database         |
| SQLAlchemy     | ORM                         |
| Alembic        | Database migrations         |
| Pytest         | Automated testing           |
| Docker         | Containerization            |
| Docker Compose | Multi-container environment |

## Project Structure

```text
taskflow-api/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── test_main.py
└── README.md
```

## API Endpoints

### Create a task

```http
POST /tasks
```

Example request:

```json
{
  "title": "Docker test",
  "description": "TaskFlow running in Docker",
  "completed": false
}
```

Example response:

```json
{
  "id": 1,
  "title": "Docker test",
  "description": "TaskFlow running in Docker",
  "completed": false,
  "created_at": "2026-08-30T06:58:45.049355",
  "updated_at": "2026-08-30T06:58:45.049360"
}
```

### Get tasks

```http
GET /tasks
```

Returns the list of tasks stored in PostgreSQL.

### Get a single task

```http
GET /tasks/{task_id}
```

Returns a task by its ID.

### Update a task

```http
PUT /tasks/{task_id}
```

Updates an existing task.

### Delete a task

```http
DELETE /tasks/{task_id}
```

Deletes a task by its ID.

## API Documentation

After starting the application, interactive API documentation is available at:

```text
http://localhost:8000/docs
```

FastAPI also provides an OpenAPI schema at:

```text
http://localhost:8000/openapi.json
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Birdseye-lab/taskflow-api.git
cd taskflow-api
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=taskflow
```

**Never commit `.env` to Git.**

The `.gitignore` file is configured to keep environment secrets out of the repository.

### 5. Start PostgreSQL

Make sure PostgreSQL is running locally and that the database `taskflow` exists.

### 6. Run the API

```powershell
uvicorn main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

## Running with Docker

The recommended way to run the complete application is Docker Compose.

Start the services:

```powershell
docker compose up -d
```

Check container status:

```powershell
docker compose ps
```

The expected services are:

```text
taskflow-api-api-1
taskflow-api-db-1
```

The PostgreSQL container should show:

```text
healthy
```

Stop the services:

```powershell
docker compose down
```

View API logs:

```powershell
docker compose logs api
```

View PostgreSQL logs:

```powershell
docker compose logs db
```

## Database

TaskFlow uses PostgreSQL as its primary database.

The application connects to PostgreSQL through SQLAlchemy using:

```text
postgresql+psycopg
```

Database schema changes are managed with Alembic.

Create a migration:

```powershell
alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```powershell
alembic upgrade head
```

## Testing

The project uses Pytest for automated testing.

Run the complete test suite:

```powershell
pytest
```

The current test suite covers the main API functionality, including task creation and other task operations.

Example successful test run:

```text
7 passed
```

## Docker Architecture

```text
                    ┌─────────────────────┐
                    │      Client         │
                    │   Swagger / HTTP    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    │      :8000          │
                    └──────────┬──────────┘
                               │
                         SQLAlchemy
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │       :5432         │
                    └─────────────────────┘
```

Both services are managed by Docker Compose and communicate through the internal Docker network.

## Environment Variables

The application uses environment variables for configuration.

| Variable            | Description                        |
| ------------------- | ---------------------------------- |
| `POSTGRES_USER`     | PostgreSQL username                |
| `POSTGRES_PASSWORD` | PostgreSQL password                |
| `POSTGRES_DB`       | PostgreSQL database name           |
| `DATABASE_URL`      | SQLAlchemy database connection URL |

Sensitive configuration is intentionally excluded from Git using `.gitignore`.

## Development

Recommended development workflow:

```powershell
docker compose up -d
pytest
```

After making changes to the application:

```powershell
docker compose build
docker compose up -d
```

Check the API:

```text
http://localhost:8000/docs
```

## Future Improvements

Planned improvements for future versions:

* JWT authentication
* User accounts
* Role-based authorization
* Task filtering and pagination
* Task priorities and deadlines
* Background jobs
* Redis caching
* CI/CD with GitHub Actions
* Production deployment
* API rate limiting
* Structured logging
* Improved error handling

## Author

**Birdseye-lab**

This project was created as a backend portfolio project to demonstrate practical experience with Python, FastAPI, PostgreSQL, SQLAlchemy, testing, Docker, and database migrations.
