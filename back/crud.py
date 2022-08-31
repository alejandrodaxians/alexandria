from fastapi import APIRouter
from back.database import conn
from back.exceptions import BookNotFoundException, IdNotFoundException
from back.models import books_table
from back.schemas import Book, BookUpdate

library = APIRouter()


@library.get("/books",
    summary="Get all books", 
    description="Output all books currently in the database, ordered by id."
    )
async def get_all_books():
    return conn.execute(books_table.select()).fetchall()


@library.get("/books/get_book_by_title/{keyword}", 
    summary="Get books by title",
    description="""Input a keyword and output all books that contain that keyword in their title.
                If there are no books with that keyword, an error is returned.""",
    )
async def get_book_by_title(keyword: str):
    result = conn.execute(books_table.select().where(books_table.c.title.contains(keyword))).fetchall()
    if result == []:
        raise BookNotFoundException(keyword)
    else:
        return result


@library.post("/books/create_book/", 
    summary="Create a book",
    description="Input the required data and create a new book. The id will be automatically assigned."
    )
async def create_book(book: Book):
    query = books_table.insert().values(
        title=book.title,
        author=book.author,
        genre=book.genre,
        release_year=book.release_year,
    )
    conn.execute(query)
    return book
    

@library.delete("/books/delete_book/{id}",
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


@library.put("/books/update_book/{id}",
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
        