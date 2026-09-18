
# The Orc Shack REST API

## Table of Contents

1. [Overview](#overview)
2. [Technology Stack](#technology-stack)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Quick Start](#quick-start)
   - [Environment Configuration](#environment-configuration)
   - [Database](#database)
   - [Manual Setup](#manual-setup)
   - [Development Commands](#development-commands)
   - [Application URLs](#application-urls)
4. [Troubleshooting](#troubleshooting)
   - [PostgreSQL Container Fails to Start](#postgresql-container-fails-to-start)
5. [Architecture & Design Decisions](#architecture--design-decisions)
   - [Application Structure](#application-structure)
   - [Request Flow](#request-flow)
6. [API Documentation & Interactive Exploration](#api-documentation--interactive-exploration)
   - [Swagger UI](#swagger-ui)
   - [Authentication Flow](#authentication-flow)
   - [ReDoc](#redoc)
7. [Testing & Quality Assurance](#testing--quality-assurance)
   - [Running the Tests](#running-the-tests)
   - [Code Quality](#code-quality)
8. [Observability](#observability)
   - [Prometheus Metrics and Viewing Metrics in Prometheus](#prometheus-metrics-and-viewing-metrics-in-prometheus)
   - [Viewing Metrics in Prometheus](#viewing-metrics-in-prometheus)


### Overview

The Orc Shack REST API is a RESTful backend for a Middle-earth restaurant.

The API allows authenticated users to interact with the restaurant's dishes and ratings. It provides user registration and login, role-based authorization, dish management, dish search, customer ratings, input validation, brute-force protection, centralized error handling, application logging, automated testing, and Prometheus metrics.

The application was developed as part of the Bash Software Engineer take-home assignment, with a focus on **maintainability, testability, security, observability, and reasonable production readiness**.

### Technology Stack

- **Python 3.11+**
- **FastAPI** — REST API framework
- **PostgreSQL** — relational database
- **SQLAlchemy** — ORM and database access
- **Pydantic** — request and response validation
- **Pydantic Settings** — application configuration
- **Alembic** — database migrations
- **Argon2** — password hashing
- **PyJWT** — JWT authentication
- **Pytest** — automated testing
- **Ruff** — linting and formatting
- **Prometheus** — application metrics
- **Docker / Docker Compose** — local infrastructure


### Getting Started

#### Prerequisites

The following tools are required to run the application locally:

- Python 3.11+
- Docker
- Docker Compose
- Make

Docker Compose is used to run the PostgreSQL database and Prometheus locally.

#### Quick Start

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Start the application:

```bash
make run
```

The startup process will:

1. Create the Python virtual environment if it does not already exist.
2. Install the required Python dependencies.
3. Create `.env` from `.env.example` if `.env` does not already exist.
4. Start PostgreSQL using Docker Compose.
5. Run the latest Alembic database migrations.
6. **Create the default admin user if one does not already exist.**
   - **Email:** `admin@admin.com`
   - **Password:** `admin`
   - **Role:** `ADMIN`
7. Start the FastAPI application.

Once started, the API will be available at:

`http://localhost:8000`

Interactive API documentation is available through Swagger UI:

`http://localhost:8000/docs`

#### Environment Configuration

The application uses environment variables for configuration.

For local development, create a `.env` file from the provided example:

```bash
cp .env.example .env
```

The `.env` file contains environment-specific configuration and secrets and should not be committed to Git.

The `.env.example` file contains placeholder values and is committed to the repository.

The main configuration values include:

- `DATABASE_URL` — PostgreSQL connection URL
- `JWT_SECRET_KEY` — secret used to sign JWT access tokens
- `JWT_ALGORITHM` — JWT signing algorithm
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` — access token lifetime
- `LOG_LEVEL` — application logging level
- `ENVIRONMENT` — application environment

#### Database

PostgreSQL is provided through Docker Compose.

To start PostgreSQL independently:

```bash
docker compose up -d postgres
```

Database schema changes are managed using Alembic.

To apply the current migrations:

```bash
alembic upgrade head
```

The `make run` command performs this step automatically.

#### Manual Setup

If `make run` is unavailable or does not work in a particular environment, the application can be started manually.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create the environment configuration:

```bash
cp .env.example .env
```

Start PostgreSQL:

```bash
docker compose up -d postgres
```

Run the database migrations:

```bash
alembic upgrade head
```

Create the **default admin user**:

```bash
python -m scripts.create_admin
```

**Default admin credentials:**

- **Email:** `admin@admin.com`
- **Password:** `admin`
- **Role:** `ADMIN`


Start the FastAPI application:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Development Commands

TThe following Make commands are available:

| Command | Description |
|---|---|
| `make venv` | Create the Python virtual environment if it does not already exist |
| `make install` | Install the required Python dependencies |
| `make run` | Start the application and required services |
| `make test` | Run the automated test suite |
| `make migrate` | Apply any pending Alembic database migrations |
| `make lint` | Run Ruff linting |
| `make format` | Format the code using Ruff |
| `make check` | Run Ruff linting and the automated test suite |
| `make metrics` | Open the FastAPI Prometheus metrics endpoint |
| `make prometheus` | Start Prometheus and open its web interface |
| `make db-up` | Start the PostgreSQL Docker service |
| `make db-down` | Stop the PostgreSQL Docker service |
| `make clean` | Remove the test database container and Python virtual environment |

#### Application URLs

Once the application is running:

| URL | Description |
|---|---|
| `http://localhost:8000/docs` | Swagger UI |
| `http://localhost:8000/redoc` | ReDoc |
| `http://localhost:8000/health` | Application health check |
| `http://localhost:8000/metrics` | Prometheus metrics |
| `http://localhost:9090` | Prometheus web interface |

### Troubleshooting

If `make metrics` is run before the FastAPI application is running, the command will exit with an error and instruct the developer to run `make run` first.

If PostgreSQL is unavailable, check the status of the Docker services:

```bash
docker compose ps
```

PostgreSQL can be started with:

```bash
docker compose up -d postgres
```

If the application cannot connect to PostgreSQL, verify that the `DATABASE_URL` in `.env` matches the PostgreSQL configuration in `docker-compose.yml`.

#### PostgreSQL container fails to start

If `make run` fails during the Alembic migration step with a PostgreSQL connection error such as:

```text
sqlalchemy.exc.OperationalError: connection failed:
connection to server at "localhost", port 5432 failed:
Connection refused
```

check the PostgreSQL container:

```bash
docker compose ps
```

If the `postgres` container is restarting, inspect its logs:

```bash
docker logs postgres
```

If the logs contain an error indicating that the PostgreSQL data directory format is incompatible with PostgreSQL 18+, the issue is caused by using the `postgres:latest` image with the PostgreSQL data volume.

For a reproducible development environment, PostgreSQL should be pinned to version 17 and the obsolete Compose `version` field should be removed.

Replace the contents of `docker-compose.yml` with:

```yaml
services:
  postgres:
    image: postgres:17
    container_name: postgres
    environment:
      POSTGRES_USER: dancingponysvc
      POSTGRES_PASSWORD: password
      POSTGRES_DB: dancingpony
    volumes:
      - postgres_data_2:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    restart: unless-stopped

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    depends_on:
      - postgres
    restart: unless-stopped

volumes:
  postgres_data_2:
  prometheus_data:
```

Then recreate the PostgreSQL container and volume:

```bash
docker compose down -v
```

After that, start the application normally:

```bash
make run
```

`make run` will start PostgreSQL, apply the pending Alembic migrations, create the default admin user if one does not already exist, and start the FastAPI application.

**Note:** `docker compose down -v` removes the PostgreSQL Docker volume and therefore deletes the local development database. Do not use this command if you need to preserve existing local data.


### Architecture & Design Decisions

#### Application Structure

The application follows a layered structure that separates HTTP handling, business logic, database access, and infrastructure concerns.

```text
app/
├── api/
│   ├── dependencies.py
│   ├── exception_handlers.py
│   ├── health.py
│   └── v1/
│       ├── auth.py
│       ├── dishes.py
│       ├── ratings.py
│       └── router.py
│
├── core/
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   └── security.py
│
├── db/
│   └── database.py
│
├── models/
│   ├── dish.py
│   ├── rating.py
│   └── user.py
│
├── repositories/
│   ├── dish_repository.py
│   ├── rating_repository.py
│   └── user_repository.py
│
├── schemas/
│   ├── dish.py
│   ├── rating.py
│   └── user.py
│
└── services/
    ├── auth_service.py
    ├── dish_service.py
    └── rating_service.py
```

The main responsibilities are:

| Directory | Responsibility |
|---|---|
| `api/` | HTTP routes, request handling, dependencies, and exception handlers |
| `core/` | Cross-cutting concerns such as configuration, logging, security, and application exceptions |
| `db/` | SQLAlchemy engine, sessions, declarative base, and database connectivity |
| `models/` | SQLAlchemy ORM models representing database entities |
| `repositories/` | Database queries and persistence operations |
| `schemas/` | Pydantic models for request validation and API responses |
| `services/` | Business logic and application rules |
| `tests/` | Automated tests for the application's behaviour |

The separation allows each layer to have a focused responsibility. API routes handle HTTP concerns, services handle business rules, repositories handle database operations, and SQLAlchemy handles communication with PostgreSQL.

This keeps the implementation easier to test and change without introducing additional abstraction layers that are not necessary for the scope of the assignment.

#### Request Flow

Requests flow through the application from the API layer to the service layer, repository layer, and database.

Authentication and authorization are handled by FastAPI dependencies before the protected route handler executes.

For example, when an authenticated admin creates a new dish:

```text
HTTP Request
    ↓
API Route Dependency
    ↓
Authentication
    ↓
Authorization
    ↓
API Route Handler
    ↓
Service
    ↓
Repository
    ↓
SQLAlchemy
    ↓
PostgreSQL
    ↓
Repository
    ↓
Service
    ↓
API Response
```

The responsibilities at each stage are:

1. **API Route Dependency** — FastAPI resolves the dependencies required by the endpoint.
2. **Authentication** — The authentication dependency extracts the bearer token, validates the JWT, identifies the user, and retrieves the corresponding user from the database. If authentication fails, the request is rejected with `401 Unauthorized`.
3. **Authorization** — For endpoints that require specific permissions, an authorization dependency checks the authenticated user's role. For example, dish creation requires an admin user. If the user is authenticated but does not have the required role, the request is rejected with `403 Forbidden`.
4. **API Route Handler** — Once authentication and authorization succeed, the route handler receives the authenticated user and validated request data and calls the appropriate service.
5. **Service** — Applies the application's business rules and coordinates the operation.
6. **Repository** — Performs the required database operation using SQLAlchemy.
7. **PostgreSQL** — Stores or retrieves the data.
8. **Repository / Service** — Returns the database result to the service layer.
9. **API Route** — Converts the result into the appropriate Pydantic response schema and returns the HTTP response.

Public endpoints such as registration and login do not require an existing authentication token. Login instead authenticates the supplied credentials and returns a JWT access token that can be used for subsequent protected requests.

Errors are handled centrally rather than being converted into HTTP responses independently by each service. Application-specific exceptions are raised from the appropriate layer and handled by the centralized exception handlers in `api/exception_handlers.py`.

This separation keeps authentication, authorization, HTTP concerns, business logic, and database operations clearly separated while allowing the individual components to be tested independently.


### API Documentation & Interactive Exploration

The API provides interactive OpenAPI documentation through FastAPI.

#### Swagger UI

Swagger UI is available at:

`http://localhost:8000/docs`

Swagger UI can be used to:

- View available API endpoints.
- Inspect request and response schemas.
- View validation requirements.
- Authenticate using a JWT access token.
- Execute API requests directly against the running application.
- Inspect HTTP responses and status codes.

#### Authentication Flow

Protected endpoints require a valid JWT access token.

To explore the authenticated API:

1. Register a user using the registration endpoint.
2. Log in using the user's email and password.
3. Copy the returned access token.
4. Use the **Authorize** button in Swagger UI.
5. Enter the bearer token when prompted.
6. Execute protected endpoints using the authenticated session.

Administrative operations, such as creating, updating, and deleting dishes, require an authenticated user with the appropriate role.

The application creates a default **admin user** during startup if one does not already exist.

Default development admin credentials:
- **Email:** `admin@admin.com`
- **Password:** `admin`
- **Role:** `ADMIN`

#### ReDoc

Alternative API documentation is available through ReDoc:

`http://localhost:8000/redoc`

ReDoc provides a read-only view of the generated OpenAPI specification.


### Testing & Quality Assurance

The application includes an automated test suite using **pytest** to verify API behaviour, business logic, database operations, and security-critical functionality.

The tests are organized around the main application layers:

- **API tests** — Verify HTTP endpoints, request validation, authentication, authorization, responses, and error handling.
- **Service tests** — Verify business rules and application logic independently of the HTTP layer.
- **Repository tests** — Verify database queries and operations against PostgreSQL.
- **Database tests** — Verify database connectivity and infrastructure.
- **Security tests** — Verify password hashing, password verification, JWT creation and validation, and authentication-related behaviour.

#### Running the Tests

Run the complete test suite with:

```bash
make test
```

Alternatively:

```bash
./venv/bin/python -m pytest
```

The test suite should complete successfully before changes are considered ready.

#### Code Quality

Ruff is used for linting and code formatting.

Run the linter with:

```bash
make lint
```

Format the code with:

```bash
make format
```

This provides automated checks for common Python issues and helps maintain consistent code quality throughout the project.


### Observability

The application includes basic observability through **application logging** and **Prometheus metrics**.

Application logs provide information about authentication events, application operations, and unexpected errors, while Prometheus metrics provide visibility into HTTP request activity and application performance.

#### Prometheus Metrics and Viewing Metrics in Prometheus

The application exposes Prometheus metrics through the `/metrics` endpoint.

Start the FastAPI application:

```bash
make run
```

The metrics endpoint is available at:

`http://localhost:8000/metrics`

To open the metrics endpoint:

```bash
make metrics
```

Prometheus runs through Docker Compose and is available at:

`http://localhost:9090`

To start Prometheus and open its web interface:

```bash
make prometheus
```

#### Viewing Metrics in Prometheus

Once both the FastAPI application and Prometheus are running, open:

`http://localhost:9090`

Prometheus collects metrics from the FastAPI application every 10 seconds.

To verify that Prometheus can reach the application:

1. Open the Prometheus web interface.
2. Navigate to **Status → Target health**.
3. Under **Select scrape pool**, select `orc-shack-api`.
4. Confirm that the target state is **UP**.

To query application metrics:

1. Navigate to the **Query** tab.
2. In the **Expression** field, enter:

   ```text
   http_requests_total
   ```

3. Click **Execute**.
4. Select **Table** to view the current metric values.
5. Select **Graph** to visualize the metric over time.

The `/metrics` endpoint provides the raw Prometheus exposition format, while the Prometheus web interface can be used to query and explore the collected metrics.


##### Prometheus Monitoring

The Prometheus target is configured and reporting application metrics successfully.

**Figure 1 — Prometheus target health showing the `orc-shack-api` target as UP.**

![Prometheus target health](docs/images/prometheus-targe-health.png)

**Figure 2 — Prometheus query displaying HTTP request metrics collected from the application.**

![Prometheus HTTP metrics](docs/images/prometheus-http-metrics.png)
