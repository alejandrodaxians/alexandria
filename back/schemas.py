from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int]
    title: str
    author: str
    genre: str
    release_year: int

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    genre: Optional[str]
    release_year: Optional[int]