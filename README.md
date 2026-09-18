
# The Orc Shack REST API

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







### Objective

Your assignment is to implement a REST API for a restaurant.

### Brief

Frogo Baggins, a hobbit from the Shire, has a great idea. He wants to build a restaurant that serves traditional dishes from the world of Middle Earth. The restaurant will be called "**The Orc Shack**" and will have a cozy atmosphere.

Frogo has hired you to build the website for his restaurant. As payment, he has offered you either a chest of gold or a ring. Choose wisely.

### Tasks (Specifications)

This assignment has 4 tasks, which you can attempt based on your level of experience. We expect candidates applying for a Junior engineer positions to complete at least the first task, Intermediate engineers must also complete the second task, and finally, seniors must also complete the 3rd task. Lastly there are some ideas in the 4th task for engineers who want to go above and beyond.


#### Task 1 (All Candidates):

Deliver a REST API that meets the following requirements:
- An API user must be able to:
    - Create, View, List, Update, and Delete dishes.
    - Dishes must have a name, description, price, and image.

- Customers must be able to take the following actions:
    - Search, View, and Rate dishes

*Junior engineers do not _need_ to worry about users or authentication.*


#### Task 2 (Intermediate & Senior)
- Add user, permission, and authentication support.
- Users must be able to register and login.
- All functionality of the API must require a logged in user (except Registration)
- At a minimum, the system should support password based authentication.
- Users must have a name and email address and password.
- Add validation to the data entities in the API.
- An Evil Orc is attempting to brute force passwords for known email addresses. Add functionality to defend against this. (You can use any methodology that you deem suitable)


#### Task 3 (Senior)

- The API is running on an old Shire Server that is starting to struggle with the load of the now popular website. Implement a solution to improve the performance of the API on the same hardware. 
- Add support for multiple different restaurants to use the product (multi-tenant SaaS)


#### Task 4 (Above and Beyond)

- The evil Orc has created many sockpuppet accounts and has left many bad reviews. Use an AI/ML solution to provide a sentiment score for each review.
- To prevent abuse, add rate-limiting per logged in customer.
- Allow users to login using OAuth2 based SSO (Google, etc)

### Constraints

- At Bash we make extensive use of Golang so first prize will always be to use Golang for your assignment.
- Alternative languages we will accept are Python (preferably fastapi), or JS/Typescript
- Implement a REST API utilizing JSON for request and response bodies where applicable.

### Tips, Advice, Guidance

- You are encouraged to make use of a web framework, SQL ORM, etc. This will help reduce the overhead of writing boilerplate code, and will let you focus on the core requirements.
- You are welcome to make use of AI to help write the code.
- This assessment is open ended, and candidates could spend weeks crafting the perfect API. We encourage you to timebox yourself, and limit the amount of time you spend. When we talk through the assessment, this can be provided as an input, and it is good to talk about the trade-offs made given the time constraint. We recommend about 6-8 hours of focused time.

### Evaluation Criteria

The test will be evaluated based on functional and non-functional requirements.

For functional requirements, your API needs to work, and meet the requirements as provided for your level.

For non-functional requirements, your API needs to be production-ready to a reasonable extent. We are looking for adherence to qualities such as testability, maintainability, observability, and security.

### Supporting Assets

You've been provided with a docker-compose file which will bring up a postgres database and prometheus. These are optional and provided to help get started.

#### Postgres

You can connect to the database via localhost:5432 using the username and password configured in the docker-compose.yml.

#### Prometheus

You can configure prometheus via the provided prometheus.yml file.

### CodeSubmit

Please organise, design, test, and document your code as if it were going into production - then push your changes to the Main branch. After you have pushed your code, you may submit the assignment on the assignment page.

Best of luck, and happy coding!

The Bash Team
