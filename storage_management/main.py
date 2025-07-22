from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
from models.database_models import Base
from views import auth_views, category_views, supplier_views, product_views
from models.schemas import UserResponse
from auth import get_current_active_user

# Створення таблиць
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Warehouse Management API",
    description="API для управління інвентаризацією складу",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутерів
app.include_router(auth_views.router)
app.include_router(category_views.router)
app.include_router(supplier_views.router)
app.include_router(product_views.router)

@app.get("/")
def read_root():
    return {"message": "Warehouse Management API", "version": "1.0.0"}

@app.get("/me", response_model=UserResponse)
def read_users_me(current_user = Depends(get_current_active_user)):
    return current_user

@app.get("/health")
def health_check():
    return {"status": "healthy"}
