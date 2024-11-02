from pydantic import BaseModel


from sqlalchemy.orm import Mapped




class ProductBase(BaseModel):

    name: str
    description: str
    price: int


class ProductCreate(BaseModel):
    pass



class Product(ProductBase):
    id: int