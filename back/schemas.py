from ast import Str
from typing import List, Optional

from pydantic import BaseModel

from models import BookType


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
