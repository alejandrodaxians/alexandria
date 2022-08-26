from typing import List

from sqlalchemy.orm import Session

from exceptions import BookInfoAlreadyExistsError, BookInfoNotFoundError
from models import BookInfo
from schemas import UpdateableBook

class CrudOps:

    def __init__(self) -> None:
        pass

    def get_all_books(session: Session, limit: int, offset: int) -> List[BookInfo]:
        return session.query(BookInfo).offset(offset).limit(limit).all()


    def get_book_by_id(session: Session, _id: int) -> BookInfo:
        book_info = session.query(BookInfo).get(_id)
        
        if book_info is None:
            raise BookInfoNotFoundError
        return book_info


    def create_book(session: Session, book_info: UpdateableBook) -> BookInfo:
        book_details = session.query(BookInfo).filter(BookInfo.title == book_info.title,
        BookInfo.author == book_info.author).first()
        
        if book_details:
            raise BookInfoAlreadyExistsError

        new_book_info = BookInfo(**book_info.dict())
        session.add(new_book_info)
        session.commit()
        session.refresh(new_book_info)
        return new_book_info


    def update_book_info(session: Session, _id: int, info_update: UpdateableBook) -> BookInfo:
        crud_init = CrudOps()
        book_info = crud_init.get_book_by_id(session, _id)

        if book_info is None:
            raise BookInfoNotFoundError

        book_info.title = info_update.title
        book_info.author = info_update.author
        book_info.genre = info_update.genre
        book_info.release_year = info_update.release_year

        session.commit()
        session.refresh(book_info)

        return book_info


    def delete_book(session: Session, _id: int):
        crud_init = CrudOps()
        book_info = crud_init.get_book_by_id(session, _id)

        if book_info is None:
            raise BookInfoNotFoundError

        session.delete(book_info)
        session.commit()

        return

    