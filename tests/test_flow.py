import asyncio
import httpx
import uuid

USER_SERVICE_URL = "http://localhost:5001"
ORDER_SERVICE_URL = "http://localhost:5002"

async def test_create_user():
    user_email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    user_data = {"name": "Test User", "email": user_email}
    
    async with httpx.AsyncClient() as client:
        print(f"Creating user with email: {user_email}...")
        response = await client.post(f"{USER_SERVICE_URL}/users", json=user_data)
        if response.status_code != 200:
            print(f"Fail: {response.text}")
        assert response.status_code == 200
        user = response.json()
        print(f" [✓] User created with ID: {user['id']}")
        return user

async def test_create_order(user_id: int):
    order_data = {
        "user_id": user_id,
        "product_name": "Test Product",
        "amount": 49.99
    }
    
    async with httpx.AsyncClient() as client:
        print(f"Creating order for user ID: {user_id}...")
        response = await client.post(f"{ORDER_SERVICE_URL}/orders", json=order_data)
        if response.status_code != 200:
            print(f"Fail: {response.text}")
        assert response.status_code == 200
        order = response.json()
        print(f" [✓] Order created with ID: {order['id']}")
        return order

async def run_integration_test():
    print("=== Starting Integration Test Flow ===")
    try:
        user = await test_create_user()
        order = await test_create_order(user['id'])
        
        print("\n[!] IMPORTANT: Verifying Notification Service")
        print("The Notification Service logs to its console when an event is received.")
        print("Please run the following command to see the tail of the notification logs:")
        print("  docker-compose logs notification_service")
        print("\n=== Integration Test Successful! ===")
        
    except Exception as e:
        print(f"\n [✗] Test Flow Failed: {e}")

if __name__ == "__main__":
    asyncio.run(run_integration_test())
