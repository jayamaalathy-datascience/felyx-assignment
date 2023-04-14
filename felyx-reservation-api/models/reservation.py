from config.db import meta, engine
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, DateTime, Float

reservations = Table(
    "reservations",
    meta,
    Column("ID", Integer, primary_key=True),
    Column("CUSTOMER_ID", Integer),
    Column("START_RESERVATION_TIME", DateTime),
    Column("END_RESERVATION_TIME", DateTime),
    Column("START_LONGITUDE", Float),
    Column("START_LATITUDE", Float)
)

meta.create_all(engine)
