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

router = APIRouter(prefix="/products", tags=["Products"])

def get_stock_status(quantity: int, min_quantity: int) -> StockStatus:
    if quantity == 0:
        return StockStatus.OUT_OF_STOCK
    elif quantity <= min_quantity:
        return StockStatus.LOW_STOCK
    else:
        return StockStatus.IN_STOCK

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Перевірка унікальності SKU
    if db.query(Product).filter(Product.sku == product.sku).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this SKU already exists"
        )
    
    # Перевірка існування категорії та постачальника
    category = db.query(Category).filter(Category.id == product.category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category not found"
        )
    
    supplier = db.query(Supplier).filter(Supplier.id == product.supplier_id).first()
    if not supplier:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Supplier not found"
        )
    
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductResponse])
def get_products(
    skip: Annotated[int, Query(ge=0, description="Skip records")] = 0,
    limit: Annotated[int, Query(ge=1, le=1000, description="Limit records")] = 100,
    search: Annotated[Optional[str], Query(description="Search in name or SKU")] = None,
    category_id: Annotated[Optional[int], Query(gt=0, description="Filter by category")] = None,
    supplier_id: Annotated[Optional[int], Query(gt=0, description="Filter by supplier")] = None,
    min_price: Annotated[Optional[float], Query(ge=0, description="Minimum price")] = None,
    max_price: Annotated[Optional[float], Query(gt=0, description="Maximum price")] = None,
    stock_status: Annotated[Optional[StockStatus], Query(description="Filter by stock status")] = None,
    is_active: Annotated[Optional[bool], Query(description="Filter by active status")] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    query = db.query(Product)
    
    # Фільтрація за пошуком
    if search:
        query = query.filter(
            or_(
                Product.name.ilike(f"%{search}%"),
                Product.sku.ilike(f"%{search}%")
            )
        )
    
    # Фільтрація за категорією
    if category_id:
        query = query.filter(Product.category_id == category_id)
    
    # Фільтрація за постачальником
    if supplier_id:
        query = query.filter(Product.supplier_id == supplier_id)
    
    # Фільтрація за ціною
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    
    # Фільтрація за статусом активності
    if is_active is not None:
        query = query.filter(Product.is_active == is_active)
    
    products = query.offset(skip).limit(limit).all()
    
    # Фільтрація за статусом запасів (після отримання з БД)
    if stock_status:
        filtered_products = []
        for product in products:
            product_status = get_stock_status(product.quantity, product.min_quantity)
            if product_status == stock_status:
                filtered_products.append(product)
        products = filtered_products
    
    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: Annotated[int, Path(gt=0, description="Product ID")],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: Annotated[int, Path(gt=0)],
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Валідація категорії та постачальника при оновленні
    update_data = product_update.model_dump(exclude_unset=True)
    
    if "category_id" in update_data:
        category = db.query(Category).filter(Category.id == update_data["category_id"]).first()
        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category not found"
            )
    
    if "supplier_id" in update_data:
        supplier = db.query(Supplier).filter(Supplier.id == update_data["supplier_id"]).first()
        if not supplier:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Supplier not found"
            )
    
    for field, value in update_data.items():
        setattr(product, field, value)
    
    db.commit()
    db.refresh(product)
    return product

@router.patch("/{product_id}/quantity")
def update_product_quantity(
    product_id: Annotated[int, Path(gt=0)],
    quantity_data: Annotated[QuantityUpdate, Body()],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    product.quantity = quantity_data.quantity
    db.commit()
    db.refresh(product)
    
    stock_status = get_stock_status(product.quantity, product.min_quantity)
    
    return {
        "message": "Quantity updated successfully",
        "product_id": product.id,
        "new_quantity": product.quantity,
        "stock_status": stock_status
    }

@router.get("/low-stock/", response_model=List[ProductResponse])
def get_low_stock_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    products = db.query(Product).filter(
        and_(
            Product.quantity <= Product.min_quantity,
            Product.is_active == True
        )
    ).all()
    return products

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: Annotated[int, Path(gt=0)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    db.delete(product)
    db.commit()