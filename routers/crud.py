from sqlalchemy.orm import Session
from app.models import ClothingProduct, ClothingReview, Order
from app.schemas import ClothingProductSchema, ClothingReviewSchema, Order
from app.database import engine

# Operasi CRUD untuk ClothingProduct


def get_clothing_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ClothingProduct).offset(skip).limit(limit).all()


def get_clothing_product_by_id(db: Session, product_id: int):
    return db.query(ClothingProduct).filter(ClothingProduct.id == product_id).first()


def create_clothing_product(db: Session, product: ClothingProductSchema):
    _product = ClothingProduct(**product.dict())
    db.add(_product)
    db.commit()
    db.refresh(_product)
    return _product


def update_clothing_product(db: Session, product_id: int, updated_product: ClothingProductSchema):
    _product = get_clothing_product_by_id(db=db, product_id=product_id)
    for field, value in updated_product.dict().items():
        setattr(_product, field, value)
    db.commit()
    db.refresh(_product)
    return _product


def delete_clothing_product(db: Session, product_id: int):
    _product = get_clothing_product_by_id(db=db, product_id=product_id)
    db.delete(_product)
    db.commit()

# Operasi CRUD untuk ClothingReview


def get_clothing_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ClothingReview).offset(skip).limit(limit).all()


def get_clothing_review_by_id(db: Session, review_id: int):
    return db.query(ClothingReview).filter(ClothingReview.id == review_id).first()


def create_clothing_review(db: Session, review: ClothingReviewSchema):
    _review = ClothingReview(**review.dict())
    db.add(_review)
    db.commit()
    db.refresh(_review)
    return _review


def update_clothing_review(db: Session, review_id: int, updated_review: ClothingReviewSchema):
    _review = get_clothing_review_by_id(db=db, review_id=review_id)
    for field, value in updated_review.dict().items():
        setattr(_review, field, value)
    db.commit()
    db.refresh(_review)
    return _review


def delete_clothing_review(db: Session, review_id: int):
    _review = get_clothing_review_by_id(db=db, review_id=review_id)
    db.delete(_review)
    db.commit()

# Operasi CRUD untuk Order


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()


def create_order(db: Session, order: Order):
    _order = Order(**order.dict())
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order


def update_order(db: Session, order_id: int, updated_order: Order):
    _order = get_order_by_id(db=db, order_id=order_id)
    for field, value in updated_order.dict().items():
        setattr(_order, field, value)
    db.commit()
    db.refresh(_order)
    return _order


def delete_order(db: Session, order_id: int):
    _order = get_order_by_id(db=db, order_id=order_id)
    db.delete(_order)
    db.commit()
