from typing import List, Dict
from back.database.db_connection import DatabaseConnection
from back.models.book import Book

db_conn = DatabaseConnection()
conn = db_conn.establish_connection()


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

    **book**: An object used to accesed the parameters needed to create the book.
    These are: title(str), author(str), genre(str), release_year(int).

    Returns:
        Dict with the new book's information.
    """
    query = Book.__tablename__.insert().values(
        title=book.title,
        author=book.author,
        genre=book.genre,
        release_year=book.release_year,
    )
    conn.execute(query)
    return book


def delete_book(id: int) -> Dict:
    """
    **Delete a book by id**

    Parameters:

    **id**: The primary key of the book to be deleted.

    Returns:
        A Dict containing a message telling the user the book has been succesfully deleted.
    """
    result = conn.execute(Book.__tablename__.select().where(Book.__tablename__.c.id == id)).first()
    book_title = result[0][1]
    conn.execute(Book.__tablename__.delete().where(Book.__tablename__.c.id == id))
    return {"message": "Book with title: " + book_title + ", deleted"}


def update_book(id: int, book: Book) -> Dict:
    """
    **Update a book by id**

    Parameters:

    **id**: The id of the book to be updated.
    **book**: An object used to accesed the parameters needed to update the book.
    These are: title(str), author(str), genre(str), release_year(int).

    Returns:
        A Dict containing a message telling the user the book has been succesfully updated.
    """
    exists = conn.execute(Book.__tablename__.select().where(Book.__tablename__.c.id == id)).first()
    query = Book.__tablename__.update().where(Book.__tablename__.c.id == id).values(
            title=book.title if book.title != None else exists.title,
            author=book.author if book.author != None else exists.author,
            genre=book.genre if book.genre != None else exists.genre,
            release_year=book.release_year if book.release_year != None else exists.release_year
        )
    conn.execute(query)
    return {"message": "Book with id: " + id + ", updated succesfully."}
