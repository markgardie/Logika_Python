from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    sku = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, default=0)
    min_quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable = False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    update_at = Column(DateTime)

    category = relationship("Category", back_populates="products")