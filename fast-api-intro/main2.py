from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, field_validator
from typing import Dict, List, Optional

app = FastAPI(title="Book Catalog API")

class Book(BaseModel):
    title: str
    author: str
    pages: int

library: Dict[str, Dict[str, Book]] = {}


@app.post("/books/", status_code=201)
async def create_book():
    pass

@app.get("/books/author/{author}")
async def get_books_by_author():
    pass

@app.get("/books/")
async def get_all_books():
    pass

@app.put("/books/")
async def update_book():
    pass

@app.delete("/books/")
async def delete_book():
    pass

@app.get("/authors/")
async def get_all_authors():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)