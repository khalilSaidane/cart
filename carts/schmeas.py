from enum import Enum
from typing import List

from pydantic import BaseModel, validator
from pydantic.datetime_parse import datetime
from starlette.exceptions import HTTPException

from carts.models import CartStatus


class CartItem(BaseModel):
    quantity: int
    product_id: int

    @validator("quantity")
    def validate_quantity(cls, value):
        if value <= 0:
            raise HTTPException(detail="Quantity must be greater than 0", status_code=400)
        return value

    class Config:
        orm_mode = True


class CartRequest(BaseModel):
    product_id: int
    cart_id: int
    quantity: int


class Cart(BaseModel):
    creation_date: datetime
    user_id: int
    cart_items: List[CartItem]
    status: CartStatus
    last_updated_at: datetime

    class Config:
        orm_mode = True
        use_enum_values = True


class CartStatusUpdate(Enum):
    OPEN = 'OPEN'
    CHECKOUT = 'CHECKOUT'
    CLOSED = 'CLOSED'
