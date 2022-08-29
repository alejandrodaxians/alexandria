from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:mysql12345@localhost:3306/alexandria")

meta = MetaData()

conn = engine.connect()