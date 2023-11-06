from pydantic import BaseModel
from typing import List

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

class UserSchema(BaseModel):
    id: int
    username: str
    email: str

class ClothingProductListSchema(BaseModel):
    data: List[ClothingProductSchema]

class ClothingReviewListSchema(BaseModel):
    data: List[ClothingReviewSchema]

class UserListSchema(BaseModel):
    data: List[UserSchema]
