# Mini E-commerce Microservices

A demonstration of a microservices architecture using FastAPI, Docker, and Async SQLAlchemy.

## Services

1.  **User Service**: Manages user registration and profiles. (FastAPI, Async SQLAlchemy, SQLite)
2.  **Order Service**: (Placeholder) Manages orders.
3.  **Notification Service**: (Placeholder) Sends notifications.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

### Running with Docker

To start all services:

```bash
docker-compose up --build
```

### API Endpoints (User Service)

- `GET /users`: Retrieve all users.
- `POST /users`: Create a new user.
  - Body: `{"name": "John Doe", "email": "john@example.com"}`

## Project Structure

```text
.
├── docker-compose.yml
├── user_service/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── requirements.txt
│   └── Dockerfile
├── order_service/
└── notification_service/
```
