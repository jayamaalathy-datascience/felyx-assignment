from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:felyx@host.docker.internal:3306/felyxDB")

meta = MetaData()

conn = engine.connect()
