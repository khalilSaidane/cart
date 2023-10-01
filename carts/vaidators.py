from starlette.exceptions import HTTPException

from carts.models import CartStatus


def validate_status_transition(old_status: CartStatus, new_status: CartStatus):
    valid_transitions = {
        CartStatus.OPEN: [CartStatus.CHECKOUT, CartStatus.CLOSED, CartStatus.REMOVED],
        CartStatus.CHECKOUT: [CartStatus.CLOSED, CartStatus.REMOVED],
    }

    if new_status not in valid_transitions.get(old_status, []):
        raise HTTPException(detail="Invalid status transition", status_code=400)
