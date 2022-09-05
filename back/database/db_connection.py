from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


class DatabaseConnection:
    def __init__(self) -> None:
        pass


    def assign_engine():
        engine = create_engine("mysql+pymysql://root:mysql12345@localhost:3306/alexandria")
        return engine


    def declare_base():
        Base = declarative_base()
        return Base


    def create_tables():
        engine = DatabaseConnection.assign_engine()
        Base = DatabaseConnection.declare_base()
        Base.metadata.create_all(engine)


    def establish_connection():
        engine = DatabaseConnection.assign_engine()
        conn = engine.connect()
        return conn

    
    def end_connection():
        conn = DatabaseConnection.establish_connection()
        conn.close()
        


if __name__ == "__main__":
    db = DatabaseConnection()
    db.assign_engine()
    db.declare_base()
    db.create_tables()
    db.establish_connection()

