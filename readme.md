# Mini E-commerce Microservices

A demonstration of a microservices architecture using FastAPI, Docker, RabbitMQ, and Async SQLAlchemy.

## Services

1.  **User Service**: Manages user registration and profiles. (FastAPI, Async SQLAlchemy, SQLite)
2.  **Order Service**: Manages order creation and tracking. Publishes events to RabbitMQ. (FastAPI, Async SQLAlchemy, SQLite, aio-pika)
3.  **Notification Service**: Consumes `order_created` events from RabbitMQ and "sends" notifications (logs to console). (Python, aio-pika)
4.  **RabbitMQ**: Message broker used for asynchronous communication between services.

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Running with Docker

To start all services:

```bash
docker-compose up --build
```

Access RabbitMQ Management UI: [http://localhost:15672](http://localhost:15672) (guest/guest)

### API Endpoints

#### User Service (Port 5001)
- `GET /users`: Retrieve all users.
- `POST /users`: Create a new user.
  - Body: `{"name": "John Doe", "email": "john@example.com"}`

#### Order Service (Port 5002)
- `GET /orders`: Retrieve all orders.
- `POST /orders`: Create a new order. 
  - *Publishes `order_created` event to `order_events` queue.*
  - Body: `{"user_id": 1, "product_name": "Laptop", "amount": 999.99}`

#### Notification Service (No Port)
- *Listens for messages on `order_events` queue and logs notifications to the container stdout.*

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
    ├── main.py
    ├── requirements.txt
    └── Dockerfile
```
