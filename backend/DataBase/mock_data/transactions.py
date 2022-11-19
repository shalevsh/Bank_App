from typing import List
from database.mock_data import Transaction
transactions: List[Transaction] = [
    Transaction(id=1, amount=10, is_deposit=False), Transaction(id=2, amount=100, is_deposit=True)]
