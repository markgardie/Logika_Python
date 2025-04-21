from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(min_length=2)
    pages: int = Field(gt=10)

class BookCreate(BookBase):
    author_name: str = Field(min_length=2, max_length=30)

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True

class AuthorBase(BaseModel):
    name: str = Field(min_length=2, max_length=30)

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: list[Book] = []

    class Config:
        from_attributes = True





