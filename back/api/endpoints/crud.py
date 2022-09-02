from back.api.exceptions import BookNotFoundException, IdNotFoundException
from back.database.database import conn
from back.models.book import Book
from back.bridges import books_bridge
from back.config import loggers

from fastapi import APIRouter, Query
from pydantic import Required

api_logger = loggers.get_logger('main')
router = APIRouter()


@router.get("/book/",
    summary="Get all books", 
    description="Output all books currently in the database, ordered by id.",
    tags=["books"],
    response_model=Book,
    )
async def get_all_books():
    try:
        books_bridge.get_all_books()
    except exception:
        api_logger.info(message)


@router.get("/book/{id}",
    summary="Get a book by id",
    description="""Get one book by passing its id. If that id is not in the database,
                raise an exception.""",
    tags=["books"],
    response_model=Book,
    )
async def get_book_by_id(id: int = Query(default=Required)):
    try:
        books_bridge.get_book_by_id(id)
    except exception:
        api_logger.info(message)
    

@router.get("/book/{title}", 
    summary="Get books by title",
    description="""Input a keyword and output all books that contain that keyword in their title.
                If there are no books with that keyword, an error is returned.""",
    tags=["books"],
    response_model=Book,
    )
async def get_book_by_title(title: str = Query(default=Required, min_length=3)):
    try:
        books_bridge.get_book_by_title(title)
    except exception:
        api_logger.info(message)


@router.post("/book/", 
    summary="Create a book",
    description="Input the required data and create a new book. The id will be automatically assigned.",
    tags=["books"],
    response_model=Book,
    )
async def create_book(book: Book = Query(default=Required)):
    try:
        books_bridge.create_book(book)
    except exception:
        api_logger.info(message)
    
    

@router.delete("/books/delete_book/{id}",
    summary="Delete a book",
    description="""Input an id and delete the corresponding book. 
                If the id is not on the database, an exception will be raised.""",
    )
async def delete_book(id: int):
    exists = conn.execute(books_table.select().where(books_table.c.id == id)).first()
    if exists == None:
        raise IdNotFoundException(id)
    else:
        result = conn.execute(books_table.select().where(books_table.c.id == id)).fetchall()
        book_title = result[0][1]
        conn.execute(books_table.delete().where(books_table.c.id == id))
        return {"message": "Book with title: " + book_title + ", deleted"}


@router.put("/books/update_book/{id}",
    summary="Update a book",
    description="""Input an id and update the book with that id. 
                If the id is not on the database, an exception will be raised.""",
    )
async def update_book(id: int, book: BookUpdate):
    exists = conn.execute(books_table.select().where(books_table.c.id == id)).first()
    if exists == None:
        raise IdNotFoundException(id)
    else:
        query = books_table.update().where(books_table.c.id == id).values(
            title=book.title if book.title != None else exists.title,
            author=book.author if book.author != None else exists.author,
            genre=book.genre if book.genre != None else exists.genre,
            release_year=book.release_year if book.release_year != None else exists.release_year
        )
        conn.execute(query)
        return conn.execute(books_table.select().where(books_table.c.id == id)).first()
        