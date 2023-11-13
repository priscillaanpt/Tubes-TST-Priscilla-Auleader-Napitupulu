from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ClothingProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: int

class ClothingReviewSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    rating: int
    review_text: str

class ClothingProductListSchema(BaseModel):
    data: List[ClothingProductSchema]

class ClothingReviewListSchema(BaseModel):
    data: List[ClothingReviewSchema]

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config():
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None