from fastapi import HTTPException, status
import math


def post_request(client_data: dict):
    if client_data == None:
        raise ValueError("General error pls refresh the page")
    if client_data.amount <= 0:
        raise ValueError("Invalid transaction amount")
    if math.isnan(client_data.amount):
        raise TypeError("Invalid transaction type")
    if (not isinstance(client_data.is_deposit, (bool))):
        raise TypeError("Invalid transaction type")
    if (not isinstance(client_data.category, (str))):
        raise TypeError("Invalid category name")
    if (not isinstance(client_data.vendor, (str))):
        raise TypeError("Invalid category vendor")


