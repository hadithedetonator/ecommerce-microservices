from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def get_orders(db: AsyncSession):
    result = await db.execute(select(models.Order))
    return result.scalars().all()

async def create_order(db: AsyncSession, order: schemas.OrderCreate):
    db_order = models.Order(
        user_id=order.user_id,
        product_name=order.product_name,
        amount=order.amount,
        status="pending"
    )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order
