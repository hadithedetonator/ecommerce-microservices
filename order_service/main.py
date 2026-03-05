from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from . import crud, models, schemas, database

app = FastAPI(title="Order Service")

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.get("/orders", response_model=List[schemas.OrderOut])
async def read_orders(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_orders(db)

@app.post("/orders", response_model=schemas.OrderOut)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_order(db=db, order=order)
