from typing import List, Optional

from sqlalchemy.orm.exc import NoResultFound

from cart.utils.services import BaseService
from carts.exceptions import CartNotFoundException, OpenCartAlreadyExistsForUser
from carts.models import CartStatus
from carts.repositories import CartRepository, CartItemRepository
from carts.schmeas import Cart, CartRequest
from carts.vaidators import validate_status_transition


class CartService(BaseService):

    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    def initialise_cart(self, user_id: int) -> Optional[Cart]:
        self._assert_does_not_have_open_cart(user_id)
        return self.cart_repository.create_cart(user_id)

    def _assert_does_not_have_open_cart(self, user_id):
        open_cart_exists = self.cart_repository.search_cart(user_id, [CartStatus.OPEN])
        if len(open_cart_exists):
            raise OpenCartAlreadyExistsForUser(user_id)

    def get_user_carts(self, user_id: int) -> List[Cart]:
        return self.cart_repository.search_cart(user_id)

    def get_cart_by_id(self, cart_id: int) -> Cart:
        try:
            return self.cart_repository.get_cart_by_id(cart_id)
        except NoResultFound:
            raise CartNotFoundException(cart_id)

    def update_cart_status(self, cart_id: int, newStatus: CartStatus) -> Optional[Cart]:
        cart = self.get_cart_by_id(cart_id)
        if cart.status == newStatus:
            return cart
        validate_status_transition(cart.status, newStatus)
        return self.cart_repository.update_cart_status(cart, newStatus)


class CartItemService(BaseService):

    def __init__(self, cart_item_repository: CartItemRepository):
        self.cart_item_repository = cart_item_repository

    def create_cart_item(self, cart_request: CartRequest):
        existing_item = self.cart_item_repository.get_cart_item_by_product_and_cart_id(
            cart_request.product_id, cart_request.cart_id
        )
        if existing_item:
            self.cart_item_repository.add_quantity(existing_item, cart_request.quantity)
            return existing_item

        return self.cart_item_repository.create_cart_item(
            cart_request.product_id,
            cart_request.cart_id,
            cart_request.quantity
        )
