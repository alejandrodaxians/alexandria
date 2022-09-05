from back.api.exceptions import ServerError, BookNotFoundError
from back.models.book import Book
from back.bridges import books_bridge
from back.config import loggers

from fastapi import APIRouter, Query, status
from pydantic import Required

api_logger = loggers.get_logger('main')
router = APIRouter()


@router.get("/book/",
    summary="Get all books", 
    description="Output all books currently in the database, ordered by id.",
    tags=["books"],
    response_model=Book,
    status_code=status.HTTP_200_OK,
    )
async def get_all_books():
    try:
        books_bridge.get_all_books()
        api_logger.info("Collection succesfully retrieved.")
    except ServerError as srve:        
        api_logger.error('{} -> There was an error retrieving the collection, with the following message: {}'\
                        .format(srve.status_code, srve.message))


@router.get("/book/{id}/",
    summary="Get a book by id",
    description="""Get one book by passing its id. If that id is not in the database,
                raise an exception.""",
    tags=["books"],
    response_model=Book,
    status_code=status.HTTP_200_OK,
    )
async def get_book_by_id(id: int = Query(default=Required)):
    try:
        books_bridge.get_book_by_id(id)
        api_logger.info(f"Book with id: '{id}' succesfully found.")
    except ServerError as srve:
        api_logger.error('{} -> There was an error retrieving the book with id {}, with the following message: {}'\
                        .format(srve.status_code, id, srve.message))
    except BookNotFoundError as bnfe:
        api_logger.error('{} -> The book with id: "{}" was not found. Error message: {}'\
                        .format(bnfe.status_code, id, bnfe.message))
        
    
@router.get("/book/{title}/", 
    summary="Get books by title",
    description="""Input a keyword and output all books that contain that keyword in their title.
                If there are no books with that keyword, an error is returned.""",
    tags=["books"],
    response_model=Book,
    status_code=status.HTTP_200_OK,
    )
async def get_book_by_title(title: str = Query(default=Required, min_length=3)):
    try:
        books_bridge.get_book_by_title(title)
        api_logger.info(f"Book with title keyword coincidence: '{title}' succesfully found.")
    except ServerError as srve:
        api_logger.error('{} -> There was an error retrieving the book with search keyword {}, with the following message: {}'\
                        .format(srve.status_code, title, srve.message))
    except BookNotFoundError as bnfe:
        api_logger.error('{} -> The book with title keyword coincidence: "{}" was not found. Error message: {}'\
                        .format(bnfe.status_code, title, bnfe.message))


@router.post("/book/", 
    summary="Create a book",
    description="Input the required data and create a new book. The id will be automatically assigned.",
    tags=["books"],
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    )
async def create_book(book: Book = Query(default=Required)):
    try:
        books_bridge.create_book(book)
        api_logger.info(f"Book created succesfully, with id: '{book.id}'.")
    except ServerError as srve:
        api_logger.error('{} -> There was an error creating he book, with the following message: {}'\
                        .format(srve.status_code, srve.message))
    
    
@router.delete("/book/{id}/",
    summary="Delete a book",
    description="""Input an id and delete the corresponding book. 
                If the id is not on the database, an exception will be raised.""",
    tags=["books"],
    response_model=Book,
    status_code=status.HTTP_200_OK,
    )
async def delete_book(id: int):
    try:
        books_bridge.delete_book(id)
        api_logger.info(f"Book with id: '{id}' deleted.")
    except ServerError as srve:
        api_logger.error('{} -> There was an error deleting he book, with the following message: {}'\
                        .format(srve.status_code, srve.message))


@router.put("/books/{id}/",
    summary="Update a book",
    description="""Input an id and update the book with that id. 
                If the id is not on the database, an exception will be raised.""",
    tags=["books"],
    response_model=Book,
    status_code=status.HTTP_200_OK,
    )
async def update_book(id: int, book: Book):
    try:
        books_bridge.update_book(id, book)
        api_logger.info(f"Book with id: '{id}' succesfully updated.")
    except ServerError as srve:
        api_logger.error('{} -> There was an error updating the book with search keyword {}, with the following message: {}'\
                        .format(srve.status_code, id, srve.message))
    except BookNotFoundError as bnfe:
        api_logger.error('{} -> The book with id: "{}" was not found. Error message: {}'\
                        .format(bnfe.status_code, id, bnfe.message))
        