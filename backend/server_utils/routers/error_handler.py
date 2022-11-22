from fastapi import HTTPException, status
import math

BAD_REQUEST_MSG = "General error pls refresh the page"
TRANSACTION_AMOUNT = "Invalid transaction amount"
TYPE_TRANSACTION_AMOUNT = "Invalid transaction type"
TRANSACTION_OPERTATION = "Invalid transaction operation"
CATEGORY_NAME = "Invalid category name"
VENDOR_NAME = "Invalid category vendor"




def post_request(client_data: dict):
    if client_data == None:
        raise ValueError(BAD_REQUEST_MSG)
    if client_data.amount <= 0:
        raise ValueError(TRANSACTION_AMOUNT)
    if math.isnan(client_data.amount):
        raise TypeError(TYPE_TRANSACTION_AMOUNT)
    if (not isinstance(client_data.is_deposit, (bool))):
        raise TypeError(TRANSACTION_OPERTATION)
    if (not isinstance(client_data.category, (str))):
        raise TypeError(CATEGORY_NAME)
    if (not isinstance(client_data.vendor, (str))):
        raise TypeError(VENDOR_NAME)


