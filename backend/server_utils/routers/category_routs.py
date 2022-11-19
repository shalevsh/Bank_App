from fastapi import APIRouter, HTTPException, status
import requests

category_router = APIRouter()


@category_router.get("/category")
def get():
    return 0
