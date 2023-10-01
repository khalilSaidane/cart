from operator import and_
from typing import Optional, List

from carts.models import Cart, CartItem, CartStatus
from cart.utils.repositories import BaseRepository


class CartRepository(BaseRepository):

    def create_cart(self, user_id: int) -> Optional[Cart]:
        cart = Cart(user_id=user_id)
        self.session.add(cart)
        self.session.commit()
        return cart

    def search_cart(self, user_id, status_list: Optional[List[CartStatus]] = None) -> List[Cart]:
        query = self.session.query(Cart).filter(Cart.user_id == user_id)

        if status_list:
            query = query.filter(Cart.status.in_(status_list))

        return query.all()

    def update_cart_status(self, cart: Cart, newStatus: CartStatus) -> Cart:
        cart.status = newStatus
        self.session.commit()
        return cart

    def get_cart_by_id(self, cart_id) -> Optional[Cart]:
        return self.session.query(Cart) \
            .filter(Cart.id == cart_id) \
            .one()


class CartItemRepository(BaseRepository):
    def create_cart_item(self, product_id: int, cart_id: int, quantity: int) -> Optional[CartItem]:
        cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
        self.session.add(cart_item)
        self.session.commit()
        return cart_item

    def get_cart_item_by_product_and_cart_id(self, product_id: int, cart_id: int) -> CartItem:
        return self.session.query(CartItem) \
            .filter(
            and_(CartItem.cart_id == cart_id, CartItem.product_id == product_id)
        ).first()

    def add_quantity(self, existing_item: CartItem, quantity: int):
        existing_item.quantity += quantity
        self.session.commit()
