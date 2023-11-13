from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import (ClothingProductSchema, ClothingReviewSchema,
                     ClothingProductListSchema, ClothingReviewListSchema)
import routers.crud as crud
import app.oauth2 as oauth2
from app.database import get_db

router = APIRouter()

@router.get("/products/", response_model=ClothingProductListSchema)
async def get_clothing_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    products = crud.get_clothing_products(db, skip, limit)
    return {"data": products}

@router.get("/products/{product_id}", response_model=ClothingProductSchema)
async def get_clothing_product(product_id: int = Path(..., title="Product ID"), db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    product = crud.get_clothing_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=ClothingProductSchema)
async def create_clothing_product(product: ClothingProductSchema, db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    return crud.create_clothing_product(db, product)

@router.put("/products/{product_id}", response_model=ClothingProductSchema)
async def update_clothing_product(product_id: int, updated_product: ClothingProductSchema, db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    product = crud.update_clothing_product(db, product_id, updated_product)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{product_id}", response_model=ClothingProductSchema)
async def delete_clothing_product(product_id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    product = crud.delete_clothing_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/reviews/", response_model=ClothingReviewListSchema)
async def get_clothing_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    reviews = crud.get_clothing_reviews(db, skip, limit)
    return {"data": reviews}

@router.get("/reviews/{reviews_id}", response_model=ClothingReviewListSchema)
async def get_clothing_review_by_id(review_id: int = Path(..., title="Review ID"), db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    review = crud.get_clothing_review_by_id(db, review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.post("/reviews/", response_model=ClothingReviewSchema)
async def create_clothing_review(review: ClothingReviewSchema, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    return crud.create_clothing_review(db, review)

@router.put("/reviews/{review_id}", response_model=ClothingReviewSchema)
async def update_clothing_review(review_id: int, updated_review: ClothingReviewSchema, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    review = crud.update_clothing_review(db, review_id, updated_review)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
    