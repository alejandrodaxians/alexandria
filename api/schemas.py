from ast import Str
from pydantic import BaseModel
from models import BookType
from typing import Optional, List

class UpdateableBook(BaseModel):
    title: str
    author: str
    genre: str
    release_year = int
    book_type: BookType

class Book(UpdateableBook):
    id: int

    class Config:
        orm_mode = True

class PaginatedBookInfo(BaseModel):
    limit: int
    offset: int
    data: List[Book]