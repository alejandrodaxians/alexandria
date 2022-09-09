from sqlalchemy import Column, Integer, String, Table

from back.database.db_connection import DatabaseConnection


db = DatabaseConnection()
Base = db.base


class Book(Base):
    __table__ = Table('books', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('title', String(255)),
                      Column('author', String(255)),
                      Column('genre', String(255)),
                      Column('release_year', Integer))
