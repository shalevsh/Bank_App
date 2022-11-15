from pydantic import BaseModel

class Transaction(BaseModel):
    id: int 
    amount: int
    is_depoist: bool 
