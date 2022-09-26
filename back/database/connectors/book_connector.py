from typing import Dict, List

from back.database.connectors.db_connection import DatabaseConnection
from back.bridges.bridge_decorator import db_setup
from back.database.schemas import Book


books = Book()


class BookDBConnector(DatabaseConnection):
    def __init__(self) -> None:
        super().__init__()

    @db_setup
    def get_all_books(db_conn=None) -> List[Book]:
        return db_conn.conn.execute(books.__table__.select()).fetchall()

    @db_setup
    def get_book_by_id(db_conn, id: int) -> Dict:
        return db_conn.conn.execute(books.__table__.select().where(books.__table__.c.id == id)).first()
