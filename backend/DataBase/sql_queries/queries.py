GET_TRANSACTIONS = "SELECT BT.id, BT.amount, BT.is_deposit, C.category, C.vendor  FROM Bank_Transaction as BT JOIN Transaction_Category as TC ON BT.id = TC.transaction_id JOIN Category as C ON C.id = TC.category_id;"
ADD_TRANSACTION_TO_TABLE = """INSERT INTO Bank_Transaction (amount,is_deposit) VALUES ({amount},{is_deposit});"""
ADD_CATAGORY_TO_TABLE = """INSERT INTO Category (vendor, category) VALUES ('{vendor}', '{category}');"""
ADD_TRANSACTION_CATAGORY_TO_TABLE = """INSERT INTO Transaction_Category (transaction_id, category_id) VALUES(%s, %s);"""
DELETE_TRANSACTION_FROM_TABLE = """DELETE FROM Bank_Transaction WHERE id= {transaction_id};"""
DELETE_TRANSACTION_CATEGORY_FROM_TABLE = """DELETE FROM Transaction_Category WHERE transaction_id ={transaction_id}"""
GET_CATEGORIES_WITH_SUM = """SELECT Category.category,Bank_Transaction.is_deposit, SUM(Bank_Transaction.amount) as sum FROM Bank_Transaction  JOIN Transaction_Category ON Bank_Transaction.id = Transaction_Category.transaction_id  JOIN Category ON Category.id = Transaction_Category.category_id WHERE Bank_Transaction.is_deposit = '{is_deposit}' GROUP BY Category.category;"""
