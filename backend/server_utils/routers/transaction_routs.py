from fastapi import APIRouter, HTTPException, status
from fastapi import Request
from server_utils.routers import db_manger
from routers import Transaction, Category, error_handler
from typing import List
import pymysql

transaction_router = APIRouter()

NO_ID_INPUT = -1
NO_ID_ERROR_MESSAGE = "transaction_id - empty"


@transaction_router.get("/transactions", status_code=200)
def get_transactions() -> List[dict]:
    try:
        transactions = db_manger.get_all_transactions()
    except pymysql.MySQLError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    return transactions


@transaction_router.post("/transactions", status_code=201)
async def add_transaction(request: Request) -> None:
    try:
        result: dict = await request.json()
        error_handler.post_request(client_data=result)
        transaction: Transaction = Transaction(
            None, result.amount, result.is_deposit)
        category: Category = Category(None, result.category, result.vendor)
        db_manger.add_transaction(transaction, category)
    except pymysql.MySQLError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=error)
    except TypeError as error:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=error)


@transaction_router.delete('/transactions/', status_code=204)
def delete_transaction(transaction_id: int) -> None:
    try:
        if (transaction_id == -1):
            raise ValueError("transaction_id - empty")
        db_manger.delete_transaction(transaction_id=NO_ID_INPUT)
    except pymysql.MySQLError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    except TypeError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)
