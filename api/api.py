from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from crud import CrudOps
from database import Base
from exceptions import BookInfoException
from schemas import Book, PaginatedBookInfo, UpdateableBook

router = APIRouter()
crud_functions = CrudOps()

class Books:
    session: Session = Depends(Base)
