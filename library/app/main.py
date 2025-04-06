from fastapi import FastAPI, Depends, HTTPException, Path, Body, Query
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db
from . import models, schemas

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Catalog API")

@app.post("/books/", status_code=201, response_model=models.Book)
async def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
   
    author = db.query(schemas.Author).filter(schemas.Author.name == book.author_name).first()
    if not author:
       author = schemas.Author(name = book.author_name)
       db.add(author)
       db.commit()

    new_book = schemas.Book(
        title = book.title,
        pages = book.pages,
        author_id = author.id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@app.get("/books/author/{author}", response_model=List[models.Book])
async def get_books_by_author(
    author: str = Path(min_length=2, max_length=30), 
    db: Session = Depends(get_db)
):
    author = db.query(schemas.Author).filter(schemas.Author.name == author).first()
    if not author:
        raise HTTPException(status_code=404, detail=f"Автор {author} не знайдений")
    
    return author.books

@app.get("/books/", response_model=List[models.Book])
async def get_all_books(db: Session = Depends(get_db)):
    return db.query(schemas.Book).all()

@app.put("/books/{title}", response_model=models.Book)
async def update_book(
    title: str = Path(min_length=2), 
    book_update: models.BookCreate = Body(...), 
    db: Session = Depends(get_db)
):
    db_book = db.query(schemas.Book).filter(schemas.Book.title == title).first()
    if not db_book:
        raise HTTPException(status_code=404, detail=f"Книга {title} не знайдена")
    
    # Оновлення або створення автора
    author = db.query(schemas.Author).filter(schemas.Author.name == book_update.author_name).first()
    if not author:
        author = schemas.Author(name=book_update.author_name)
        db.add(author)
        db.commit()
    
    # Оновлення книги
    db_book.title = book_update.title
    db_book.pages = book_update.pages
    db_book.author_id = author.id
    
    db.commit()
    db.refresh(db_book)
    
    return db_book

@app.delete("/books/{title}")
async def delete_book(
    title: str = Path(min_length=2), 
    db: Session = Depends(get_db)
):
    db_book = db.query(schemas.Book).filter(schemas.Book.title == title).first()
    if not db_book:
        raise HTTPException(status_code=404, detail=f"Книга {title} не знайдена")
    
    db.delete(db_book)
    db.commit()
    
    return {"detail": f"Книга {title} видалена"}

@app.get("/authors/", response_model=List[models.Author])
async def get_all_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)