from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class ClothingProduct(Base):
    __tablename__ = "clothing_products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    # Tambahkan kolom lain yang diperlukan, seperti ukuran, warna, dll.

    # Hubungan dengan ulasan
    reviews = relationship("ClothingReview", back_populates="product")

class ClothingReview(Base):
    __tablename__ = "clothing_reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("clothing_products.id"))
    rating = Column(Integer)
    review_text = Column(String)

    # Hubungan dengan pengguna
    user = relationship("User", back_populates="reviews")
    # Hubungan dengan produk pakaian
    product = relationship("ClothingProduct", back_populates="reviews")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    reviews = relationship("ClothingReview", back_populates="user")