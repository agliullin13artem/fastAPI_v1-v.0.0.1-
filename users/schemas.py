from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr

from typing import Annotated




class CreateUser(BaseModel):
    username: Annotated[str, MinLen(5), MaxLen(20)]
    email: EmailStr
