from starlette.exceptions import HTTPException


class CartNotFoundException(HTTPException):
    def __init__(self, cart_id: int):
        super().__init__(status_code=404, detail=f"Cart {cart_id} not found")


class OpenCartAlreadyExistsForUser(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=404, detail=f"An open cart already exists for this user {user_id}.")
