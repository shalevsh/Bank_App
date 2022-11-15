import pymysql
from typing import List
from sql_queries.queries import *
from mock_data.transactions import *
from mock_data.categories import *


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")
    
def insert_to_table(ingredients: List[str],table_name:str):
    query = INSERT_INTO_DAIRY if table_name == DIARY else INSERT_INTO_GLUTEN
    with connection.cursor() as cursor:
         data = list([(ingredient_name) for ingredient_name in ingredients])
         cursor.executemany(query, data)
         connection.commit()

def init_tables():
    insert_to_table(ingredients = dairy_ingredients, table_name = DIARY)
    insert_to_table(ingredients = gluten_ingredients, table_name = GLUTEN)

if __name__ == "__main__":
     init_tables()