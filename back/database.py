from sqlite3 import OperationalError
from urllib.error import HTTPError
from sqlalchemy import create_engine, MetaData

try:
    engine = create_engine("mysql+pymysql://root:mysql12345@localhost:3306/alexandria")
    meta = MetaData()
    conn = engine.connect()
except OperationalError as err:
    print(err)