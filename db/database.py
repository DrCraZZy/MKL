from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'TheTransporter.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
metadata = MetaData()
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
