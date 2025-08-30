
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime
from enum import Enum

class ProductBase(BaseModel):
    name: str =  Field(min_length=2, max_length=200)
    sku: str = Field(min_length=3, max_length=50)
    description: Optional[str] = Field(max_length=1000)
    quantity: int = Field(ge=0)
    min_quantity: int = Field(ge=0)
    price: float = Field(ge=0)
    category_id: int = Field(gt=0)
    supplier_id: int = Field(gt=0)

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    created_at: datetime
    update_at: Optional[datetime]
    category: CategoryResponse
    supplier: SupplierResponse

class ProductUpdate(BaseModel):
    name: Optional[str] =  Field(min_length=2, max_length=200)
    sku: Optional[str] = Field(min_length=3, max_length=50)
    description: Optional[str] = Field(max_length=1000)
    quantity: Optional[int] = Field(ge=0)
    min_quantity: Optional[int] = Field(ge=0)
    price: Optional[float] = Field(ge=0)
    category_id: Optional[int] = Field(gt=0)
    supplier_id: Optional[int] = Field(gt=0)
    is_active: Optional[bool] = None