import datetime
import enum

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship

from cart.db.database import Base


class CartStatus(enum.Enum):
    OPEN = 'OPEN'
    CHECKOUT = 'CHECKOUT'
    CLOSED = 'CLOSED'
    REMOVED = 'REMOVED'


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    status = Column(Enum(CartStatus), default=CartStatus.OPEN, nullable=False)
    last_updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Define a one-to-many relationship between Cart and CartItem
    cart_items = relationship('CartItem', back_populates='cart')


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    # Define a many-to-one relationship between CartItem and Cart
    cart = relationship('Cart', back_populates='cart_items')
