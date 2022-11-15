
from constants import *
from typing import List
from Recipe import Recipe
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def remove_recipes(recipes: List[Recipe],table_name:str):
    ingredients = get_ingredients(table_name)
    diary_set = set(map(lambda ingredient: ingredient["ingredient_name"],ingredients))
    return list(filter(lambda recipe: set(recipe.ingredients).isdisjoint(diary_set), recipes))


def get_ingredients(table_name: str):
    try:
        with connection.cursor() as cursor:
            query = SELECT_FROM_DAIRY if table_name == DIARY else SELECT_FROM_GLUTEN
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    except TypeError as exception:
        return (exception)
