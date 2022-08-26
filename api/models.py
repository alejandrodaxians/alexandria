from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum

import enum

from database import Base

class BookType(str, enum.Enum):
    book = "Book"
    ebook = "E-Book"

class BookInfo(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    release_year = Column(Integer)