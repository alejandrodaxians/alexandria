from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import InvalidRequestError, DisconnectionError, ResourceClosedError

from back.config.properties import SQL_DB_URL
from back.config import loggers
from back.config.singleton import SingletonMeta

db_logger = loggers.get_logger('database')


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.engine = create_engine(SQL_DB_URL)
        self.base = declarative_base()

    def connect(self):
        try:
            self.conn = self.engine.connect()
        except InvalidRequestError as ire:
            db_logger.error('{} -> There was an error connecting to the database, \
                         with the following message: {}'
                            .format(ire.status_code, ire.message))
            raise ire
        return self.conn

    def is_up(self):
        try:
            self.connect()
            print("Connected to database.")
            self.disconnect()
            print("Disconnected.")
        except DisconnectionError as de:
            db_logger.error('{} -> The connection to the database was lost, \
                         with the following message: {}'
                            .format(de.status_code, de.message))
            raise de
        return True

    def disconnect(self):
        try:
            self.conn.close()
        except ResourceClosedError as rce:
            db_logger.error('{} -> Database connection already closed.'
                            .format(rce.status_code))
            raise rce
