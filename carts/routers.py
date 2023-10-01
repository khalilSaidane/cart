from typing import List

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from carts.models import CartStatus
from carts.schmeas import Cart, CartItem, CartRequest, CartStatusUpdate
from carts.services import CartService, CartItemService
from cart.dependencies.service import get_service

cart_router = APIRouter()
cart_item_router = APIRouter()


@cbv(cart_router)
class CartView:
    cart_service: CartService = Depends(get_service(CartService))

    @cart_router.post("/{user_id}", response_model=Cart)
    def init_cart(self, user_id: int):
        return self.cart_service.initialise_cart(user_id)

    @cart_router.get("/{user_id}", response_model=List[Cart])
    def get_user_carts(self, user_id: int):
        return self.cart_service.get_user_carts(user_id)

    @cart_router.put("/{cart_id}", response_model=Cart)
    def update_status(self, cart_id: int, status: CartStatusUpdate):
        return self.cart_service.update_cart_status(cart_id, CartStatus[status.value])

    @cart_router.delete("/{cart_id}", response_model=Cart)
    def remove_cart(self, cart_id: int):
        return self.cart_service.update_cart_status(cart_id, CartStatus.REMOVED)


@cbv(cart_item_router)
class CartItemView:
    cart_item_service: CartItemService = Depends(get_service(CartItemService))

    @cart_item_router.post("/", response_model=CartItem)
    async def create_cart_item(self, cart_request: CartRequest):
        return self.cart_item_service.create_cart_item(cart_request)
