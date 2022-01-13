from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_NAME

engine = create_engine(DATABASE_NAME)
metadata = MetaData()
database = Database()


def create_db():
    metadata.create_all(bind=engine)
