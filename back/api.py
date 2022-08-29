from urllib import response
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from back.crud import CrudOps
from back.database import Base
from back.exceptions import BookInfoException
from back.schemas import Book, PaginatedBookInfo, UpdateableBook

router = APIRouter()
crud_functions = CrudOps()

@cbv(router)
class Books:
    session: Session = Depends(Base)

    @router.get("/books", response_model=PaginatedBookInfo)
    def list_books(self, limit: int = 10, offset: int = 0):
        books_list = crud_functions.get_all_books(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": books_list}
        return response

    @router.post("/books")
    def add_book(self, book_info: UpdateableBook):
        try:
            book_info = crud_functions.create_book(self.session, book_info)
            return book_info
        except BookInfoException as bie:
            raise HTTPException(**bie.__dict__)


@router.get("/books/{book_id}", response_model=Book)
def get_book_info(book_id: int, session: Session = Depends(Base)):
    try:
        book_info = crud_functions.get_book_by_id(session, book_id)
        return book_info
    except BookInfoException as bie:
        raise HTTPException(**bie.__dict__)


@router.put("cars/{book_id}", response_model=Book)
def update_book(book_id: int, new_info: UpdateableBook, session: Session = Depends(Base)):
    try:
        book_info = crud_functions.update_book_info(session, book_id, new_info)
        return book_info
    except BookInfoException as bie:
        raise HTTPException(**bie.__dict__)


@router.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(Base)):
    try:
        return crud_functions.delete_book(session, book_id)
    except BookInfoException as bie:
        raise HTTPException(**bie.__dict__)

