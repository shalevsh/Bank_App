from typing import List
from database.mock_data import Category
from database.mock_data import constant
categories: List[Category] = [
    Category(id=1, category=constant.TRANSPORT, vendor=constant.BUS), Category(id=2, category=constant.FOOD, vendor=constant.CAT_FOOD)]
