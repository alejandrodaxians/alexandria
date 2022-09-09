from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from back.config.properties import SQL_DB_URL


class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine(SQL_DB_URL)
        self.base = declarative_base()
        self.tables = self.base.metadata.create_all(self.engine)
        self.conn = self.engine.connect()

    def end_connection(self):
        self.conn.close()
