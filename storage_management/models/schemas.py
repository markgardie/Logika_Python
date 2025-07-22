
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    is_active: bool
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class CategoryResponse(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime

class SupplierBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    contact_person: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=500)

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    contact_person: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None

class SupplierResponse(SupplierBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    is_active: bool
    created_at: datetime

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=200)
    sku: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=1000)
    quantity: int = Field(..., ge=0)
    min_quantity: int = Field(0, ge=0)
    price: float = Field(..., gt=0)
    category_id: int = Field(..., gt=0)
    supplier_id: int = Field(..., gt=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    quantity: Optional[int] = Field(None, ge=0)
    min_quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, gt=0)
    category_id: Optional[int] = Field(None, gt=0)
    supplier_id: Optional[int] = Field(None, gt=0)
    is_active: Optional[bool] = None

class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    category: CategoryResponse
    supplier: SupplierResponse

class StockStatus(str, Enum):
    IN_STOCK = "in_stock"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"

class ProductFilter(BaseModel):
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    stock_status: Optional[StockStatus] = None
    is_active: Optional[bool] = None

class QuantityUpdate(BaseModel):
    quantity: int = Field(..., ge=0)