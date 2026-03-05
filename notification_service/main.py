import asyncio
import json
import os
import aio_pika

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")

async def process_message(message: aio_pika.IncomingMessage):
    async with message.process():
        body = json.loads(message.body.decode())
        event_type = body.get("event_type")
        data = body.get("data")
        
        print(f" [x] Received event: {event_type}")
        if event_type == "order_created":
            order_id = data.get("order_id")
            user_id = data.get("user_id")
            product = data.get("product_name")
            amount = data.get("amount")
            print(f" [!] NOTIFICATION: Order #{order_id} created for User {user_id}: {product} (${amount})")
        else:
            print(f" [?] Unknown event type: {event_type}")

async def main():
    print(f" [*] Connecting to RabbitMQ at {RABBITMQ_URL}")
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)
        
        queue = await channel.declare_queue("order_events", durable=True)
        
        print(" [*] Waiting for messages. To exit press CTRL+C")
        
        await queue.consume(process_message)
        
        # Keep the script running
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Interrupted")
