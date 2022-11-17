import pymysql
from typing import List
from sql_queries.queries import *
from mock_data.transactions import *
from mock_data.categories import *
from constants.constans import *

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="bank_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print(CHECK_CONNECTION)


def get_all_transactions() -> List[dict]:
    query: str = GET_TRANSACTIONS
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def add_transaction(transaction: Transaction, category: Category) -> None:
    add_bank_transaction_query: str = ADD_TRANSACTION_TO_TABLE.format(
        amount=transaction.amount, is_deposit=transaction.is_deposit)
    add_category_query: str = ADD_CATAGORY_TO_TABLE.format(
        vendor=category.vendor, category=category.category)
    add_transaction_category_query: str = ADD_TRANSACTION_CATAGORY_TO_TABLE
    with connection.cursor() as cursor:
        cursor.execute(add_bank_transaction_query)
        transaction_id: int = cursor.lastrowid
        cursor.execute(add_category_query)
        category_id: int = cursor.lastrowid
        cursor.execute(add_transaction_category_query,
                       [transaction_id, category_id])
        connection.commit()


def delete_transaction(transaction_id: int) -> None:
    delete_transaction_query: str = DELETE_TRANSACTION_FROM_TABLE.format(
        transaction_id=transaction_id)
    delete_transaction_category_query: str = DELETE_TRANSACTION_CATEGORY_FROM_TABLE.format(
        transaction_id=transaction_id)
    with connection.cursor() as cursor:
        cursor.execute(delete_transaction_category_query)
        cursor.execute(delete_transaction_query)
        connection.commit()


def get_all_categories_with_sum_of_amount() -> List[dict]:
    categories_deposite_sum_query: str = GET_CATEGORIES_WITH_SUM.format(
        is_deposit=TRUE)
    categories_withdraw_sum_query: str = GET_CATEGORIES_WITH_SUM.format(
        is_deposit=FALSE)
    with connection.cursor() as cursor:
        cursor.execute(categories_deposite_sum_query)
        deposite_categories: List[dict] = cursor.fetchall()
        cursor.execute(categories_withdraw_sum_query)
        withdraw_categories = cursor.fetchall()
        categories_with_sum: List[dict] = calculate_balance(
            deposite_categories, withdraw_categories)
        return categories_with_sum


def calculate_balance(deposite_categories: List[dict], withdraw_categories: List[dict]) -> List[dict]:
    for income_category in deposite_categories:
        deposite_category = income_category["category"]
        if any(withdraw_category['category'] == deposite_category for withdraw_category in withdraw_categories):
            index, withdraw_amount = [(index, withdraw_category['sum'])
                                      for index, withdraw_category
                                      in withdraw_categories
                                      if withdraw_category['category'] == deposite_category]
        income_category["sum"] -= withdraw_amount
        withdraw_categories.remove(index)
        add_categories_without_deposit(
            deposite_categories, withdraw_categories)
    return deposite_categories


def add_categories_without_deposit(deposite_categories: List[dict], withdraw_categories: List[dict]) -> None:
    for category in withdraw_categories:
        category.sum = - category.sum
        deposite_categories.push(category)


if __name__ == "__main__":
    # methods for check db functinality :

    # add_transaction(transactions[0], categories[0])
    # add_transaction(transactions[1], categories[1])
    # delete_transaction(1)
    get_all_categories_with_sum_of_amount()
