from pydantic import BaseModel, Field


class Book(BaseModel):
    id: int
    title: str = Field(min_length=2)
    pages: int = Field(gt=10)
    author_id: int

    class Config:
        from_attributes = True

        

class Author(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=30)
    books: list[Book] = []

    class Config:
        from_attributes = True



