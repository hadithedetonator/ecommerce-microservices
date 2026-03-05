# Mini E-commerce Microservices

A demonstration of a microservices architecture using FastAPI, Docker, and Async SQLAlchemy.

## Services

1.  **User Service**: Manages user registration and profiles. (FastAPI, Async SQLAlchemy, SQLite)
2.  **Order Service**: Manages order creation and tracking. (FastAPI, Async SQLAlchemy, SQLite)
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

### API Endpoints

#### User Service (Port 5001)
- `GET /users`: Retrieve all users.
- `POST /users`: Create a new user.
  - Body: `{"name": "John Doe", "email": "john@example.com"}`

#### Order Service (Port 5002)
- `GET /orders`: Retrieve all orders.
- `POST /orders`: Create a new order.
  - Body: `{"user_id": 1, "product_name": "Laptop", "amount": 999.99}`

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
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── requirements.txt
│   └── Dockerfile
└── notification_service/
```
