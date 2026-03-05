import json
import os
import aio_pika
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from . import crud, models, schemas, database

app = FastAPI(title="Order Service")

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")

async def publish_event(event_type: str, data: dict):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        await channel.declare_queue("order_events", durable=True)
        
        message_body = {
            "event_type": event_type,
            "data": data
        }
        
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message_body).encode()),
            routing_key="order_events"
        )

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.get("/orders", response_model=List[schemas.OrderOut])
async def read_orders(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_orders(db)

@app.post("/orders", response_model=schemas.OrderOut)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(database.get_db)):
    db_order = await crud.create_order(db=db, order=order)
    
    # Publish event to RabbitMQ
    await publish_event("order_created", {
        "order_id": db_order.id,
        "user_id": db_order.user_id,
        "product_name": db_order.product_name,
        "amount": db_order.amount
    })
    
    return db_order
