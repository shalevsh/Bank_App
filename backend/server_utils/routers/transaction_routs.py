from fastapi import APIRouter, HTTPException, status
import requests
from server_utils.routers import db_manger
transaction_router = APIRouter()


@transaction_router.get("/transaction")
def get():
    return db_manger.get_all_transactions()
