from fastapi import APIRouter, HTTPException, status
import requests

transaction_router = APIRouter()


@transaction_router.get("/transaction")
def get():
    return 0