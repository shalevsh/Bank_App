import pymysql
from typing import List
from sql_queries.queries import *
from mock_data.transactions import *
from mock_data.categories import *


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
        amount=transaction.amount, is_depoist=transaction.is_depoist)
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
        cursor.execute(delete_transaction_query)
        cursor.execute(delete_transaction_category_query)
        connection.commit()


def get_all_categories_with_sum_of_amount():
    categories_with_sum_of_amount_quary: str = """ SELECT Category.category, SUM(Bank_Transaction.amount),
                                                    FROM Bank_Transaction JOIN TransactionCategory
                                                    ON Bank_Transaction.id = TransactionCategory.transaction_id
                                                    JOIN Category
                                                    ON Category.id = TransactionCategory.category_id
                                                    GROUP BY Category.category"""
    with connection.cursor() as cursor:
        cursor.execute(categories_with_sum_of_amount_quary)
        result = cursor.fetchall()
        return result


if __name__ == "__main__":
    # add_transaction(transactions[1], categories[1])
    delete_transaction(0)
