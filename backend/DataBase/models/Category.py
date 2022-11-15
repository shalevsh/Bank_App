from pydantic import BaseModel

class Category(BaseModel):
    id: int 
    category: str
    vender: str
