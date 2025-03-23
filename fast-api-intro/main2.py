from fastapi import FastAPI, HTTPException, Query, Path, Body, Depends
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Annotated
from fastapi.responses import JSONResponse

app = FastAPI(title="Book Catalog API")

class Book(BaseModel):
    title: str
    author: str
    pages: int

library: Dict[str, Dict[str, Book]] = {}


def validate_author(
        author: Annotated[
            str, 
            Query(min_length=2, max_length=30, description="Ім'я повинно бути від 2 до 30")
        ]
    ):
    return author

def check_author_exists(author: str):
    if author not in library:
        raise HTTPException(
            status_code=404,
            detail=f"Автор {author} не знайдений"
        )

    return author

@app.post("/books/", status_code=201)
async def create_book(
    title: Annotated[str, Body(gt=2)],
    author: Annotated[str, Body(min_length=2, max_length=30)],
    pages: Annotated[int, Body(gt=10)]  
):
    pass

@app.get("/books/author/{author}")
async def get_books_by_author(
    author: Annotated[str, Path(min_length=2, max_length=30)] = Depends(check_author_exists)
):
    pass

@app.get("/books/")
async def get_all_books( ):
    pass

@app.put("/books/{title}")
async def update_book():
    pass

@app.delete("/books/{title}")
async def delete_book(
    title: Annotated[str, Path(gt=2)],
    author: Annotated[str, Query(min_length=2, max_length=30)] = Depends(validate_author)
):
    pass

@app.get("/authors/")
async def get_all_authors():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)