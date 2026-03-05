from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def get_users(db: AsyncSession):
    result = await db.execute(select(models.User))
    return result.scalars().all()

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
