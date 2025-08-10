from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Query, Path, Body
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from database import get_db
from models.database_models import Product, Category, Supplier, User
from models.schemas import (
    ProductCreate, ProductUpdate, ProductResponse, 
    StockStatus, QuantityUpdate
)
from auth import get_current_active_user

router = APIRouter(prefix="/products", tags = ["Products"])

@router.post("/create", 
             response_model=ProductResponse, 
             status_code=status.HTTP_201)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    if db.query(Product).filter(Product.sku == product.sku).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this SKU already exists"
        )
    
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductResponse])
def get_products():
    pass

@router.get("/{product_id}", response_model=ProductResponse)
def get_product():
    pass

@router.put("/update/{product_id}", response_model=ProductResponse)
def update_product():
    pass

@router.delete("/delete/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product():
    pass