from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    user_id: int
    product_name: str
    amount: float

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    status: str

    class Config:
        from_attributes = True
