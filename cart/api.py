from fastapi import APIRouter

from carts.routers import cart_router, cart_item_router

api_router = APIRouter()

api_router.include_router(cart_router, tags=["Carts"], prefix="/carts")
api_router.include_router(cart_item_router, tags=["Cart Items"], prefix="/cart-items")