from typing import Optional
from pydantic import BaseModel



class Produto(BaseModel):
    id : Optional[int]=None
    name : str
    price : float













