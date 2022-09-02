from turtle import title
from typing import List, Dict
from back.database.database import conn
from back.models.book import Book


def get_all_books() -> List[Dict]:
    """
    **Display all books currently in the database**

    Parameters: None

    Returns:
        List of dicts with every book recorded.
    """
    return conn.execute(Book.__tablename__.select()).fetchall()


def get_book_by_id(id: int) -> Dict:
    """
    **Display the book with the given id**

    Parameters:

    **id**: id, primary key of the book to get.

    Returns:
        Dict with the book information.
    """
    query_result = conn.execute(Book.__tablename__.select().where(Book.__tablename__.c.id == id)).first()
    return query_result


def get_book_by_title(title: str) -> List[Dict]:
    """
    **Display all the books which names contain the keyword passed**

    Parameters:

    **title**: The keyword with which to search for the book title.
    Must be at least 3 char long.

    Returns:
        List of dicts with every book concurrent to the keyword.
    """
    query_result = conn.execute(Book.__tablename__.select().where(Book.__tablename__.c.title.contains(title))).fetchall()
    return query_result


def create_book(book: Book) -> Dict:
    """
    **Create a new book**

    Parameters:

    **book: Book**: An object used to accesed the parameters needed to create the book.
    These are: title(str), author(str), genre(str), release_year(int).

    Returns:
        Dict with the new book's information.
    """
    book = Book()
    query = Book.__tablename__.insert().values(
        title=book.title,
        author=book.author,
        genre=book.genre,
        release_year=book.release_year,
    )
    conn.execute(query)
    return book