from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from back.config.properties import SQL_DB_URL


class DatabaseConnection:

    def assign_engine():
        engine = create_engine(SQL_DB_URL)
        return engine


    def declare_base(self):
        Base = declarative_base()
        return Base


    def create_tables(self):
        engine = DatabaseConnection.assign_engine()
        Base = DatabaseConnection.declare_base()
        Base.metadata.create_all(engine)


    def establish_connection(self):
        engine = DatabaseConnection.assign_engine()
        conn = engine.connect()
        return conn

    
    def end_connection(self):
        conn = DatabaseConnection.establish_connection()
        conn.close()
        


if __name__ == "__main__":
    db = DatabaseConnection()
    db.assign_engine()
    db.declare_base()
    db.create_tables()
    db.establish_connection()

