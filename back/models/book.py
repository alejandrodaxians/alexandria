from sqlalchemy import Column, Integer, String
from back.database.db_connection import DatabaseConnection

db = DatabaseConnection()
Base = db.declare_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    release_year = Column(Integer)

    


    

