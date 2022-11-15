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
    print("the connection is opened")


def get_all_transactions():
    query: str = """   SELECT Bank_Transaction.id, Bank_Transaction.amount, Category.id, Category.vendor, Category.category
                         FROM Bank_Transaction JOIN Transaction_Category
                         ON Bank_Transaction.id = Transaction_Category.transaction_id
                         JOIN Category
                         ON Category.id = Transaction_Category.category_id;"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall
        return result


def add_transaction(transaction: Transaction, category: Category):
    add_bank_transaction_query: str = f"INSERT INTO Bank_Transaction (amount,is_depoist) VALUES ({transaction.amount},{transaction.is_depoist});"
    add_category_query: str = f"INSERT INTO Category (vendor, category) VALUES ('{category.vendor}', '{category.category}');"
    add_transaction_category_query: str = """INSERT INTO Transaction_Category (transaction_id, category_id) VALUES(%s, %s);"""
    with connection.cursor() as cursor:
        cursor.execute(add_bank_transaction_query)
        transaction_id: int = cursor.lastrowid
        cursor.execute(add_category_query)
        category_id: int = cursor.lastrowid
        cursor.execute(add_transaction_category_query,
                       [transaction_id, category_id])
        connection.commit()


def delete_transaction(transaction_id: int, category_id: int):
    delete_by_id_query: str = """DELETE FROM %s WHERE id=%d;"""
    delete_transaction_category_query: str = """DELETE FROM TransactionCategory 
                                                WHERE transaction_id={transaction_id} AND category_id={category_id};"""
    with connection.cursor() as cursor:
        cursor.execute(delete_by_id_query, [
                       "Bank_Transaction", transaction_id])
        cursor.execute(delete_by_id_query, ["Category", category_id])
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
    add_transaction(transactions[0], categories[0])
    pass
