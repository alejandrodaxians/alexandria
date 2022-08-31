from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from back.database import meta, engine

books_table = Table('books', meta, 
    Column("id", Integer, primary_key=True), 
    Column("title", String(255)), 
    Column("author", String(255)), 
    Column("genre", String(255)),
    Column("release_year", Integer)
)

meta.create_all(engine)