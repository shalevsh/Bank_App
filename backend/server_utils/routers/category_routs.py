from fastapi import APIRouter, HTTPException, status
from server_utils.routers import db_manger
from typing import List
import pymysql
category_router = APIRouter()


@category_router.get("/categories", status_code=200)
def get_categories() -> List[dict]:
    try:
        categories = db_manger.get_all_categories_with_sum_of_amount()
    except pymysql.MySQLError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = error)
    return categories
