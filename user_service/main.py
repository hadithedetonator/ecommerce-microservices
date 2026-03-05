from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from . import crud, models, schemas, database

app = FastAPI(title="User Service")

# Create tables on startup (simple approach for dev)
@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.get("/users", response_model=List[schemas.UserOut])
async def read_users(db: AsyncSession = Depends(database.get_db)):
    users = await crud.get_users(db)
    return users

@app.post("/users", response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(db=db, user=user)
