from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from schemas import (ClothingProductSchema, ClothingReviewSchema, UserSchema,
                     ClothingProductListSchema, ClothingReviewListSchema, UserListSchema)
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products/", response_model=ClothingProductListSchema)
async def get_clothing_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_clothing_products(db, skip, limit)
    return {"data": products}

@router.get("/products/{product_id}", response_model=ClothingProductSchema)
async def get_clothing_product(product_id: int = Path(..., title="Product ID"), db: Session = Depends(get_db)):
    product = crud.get_clothing_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=ClothingProductSchema)
async def create_clothing_product(product: ClothingProductSchema, db: Session = Depends(get_db)):
    return crud.create_clothing_product(db, product)

@router.put("/products/{product_id}", response_model=ClothingProductSchema)
async def update_clothing_product(product_id: int, updated_product: ClothingProductSchema, db: Session = Depends(get_db)):
    product = crud.update_clothing_product(db, product_id, updated_product)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{product_id}", response_model=ClothingProductSchema)
async def delete_clothing_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_clothing_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Tambahkan rute untuk ClothingReview dan User di sini dengan pola yang sama seperti produk di atas.

@router.get("/reviews/", response_model=ClothingReviewListSchema)
async def get_clothing_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reviews = crud.get_clothing_reviews(db, skip, limit)
    return {"data": reviews}

# Lengkapi rute untuk ClothingReview dan User dengan operasi CRUD yang sesuai.

@router.get("/users/", response_model=UserListSchema)
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return {"data": users}

# Lengkapi rute untuk User dengan operasi CRUD yang sesuai.
@router.get("/users/", response_model=UserListSchema)
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return {"data": users}

@router.get("/users/{user_id}", response_model=UserSchema)
async def get_user(user_id: int = Path(..., title="User ID"), db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.put("/users/{user_id}", response_model=UserSchema)
async def update_user(user_id: int, updated_user: UserSchema, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, updated_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", response_model=UserSchema)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
